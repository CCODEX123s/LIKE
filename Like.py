import telebot
import requests
import json
import time
from datetime import datetime, timedelta
import os
from threading import Lock
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#==============LK-TEAM==============#
# MADE BY LK-TEAM

BOT_TOKEN = "8089176693:AAEm3JN6Lu9xgjJSZUBJIG20Yiz0u7VKmRg"  
ADMIN_IDS = [8276114868]

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")

ALLOWED_GROUPS_FILE = "allowed_groupss.json"
USAGE_DATA_FILE = "usage_dataa.json"

file_lock = Lock()

API_BASE_URL = "https://likes-api-lkteam-iorq.onrender.com/like"
SUPPORTED_REGIONS = ["ME", "SG", "BD", "TH", "VN"]
UNSUPPORTED_REGIONS = ["IND", "US", "BR", "SAC", "NA"]

# ================== JSON UTILS ================== #
def load_json_file(filename, default_data=None):
    if default_data is None:
        default_data = {}
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        else:
            with open(filename, 'w') as f:
                json.dump(default_data, f, indent=2)
            return default_data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return default_data

def save_json_file(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False

# ================== CHECKS ================== #
def is_admin(user_id):
    return user_id in ADMIN_IDS

def is_group_allowed(chat_id):
    with file_lock:
        allowed_groups = load_json_file(ALLOWED_GROUPS_FILE, {})
        return str(chat_id) in allowed_groups

def get_group_usage(chat_id):
    with file_lock:
        usage_data = load_json_file(USAGE_DATA_FILE, {})
        today = datetime.now().strftime("%Y-%m-%d")
        chat_str = str(chat_id)
        if chat_str not in usage_data:
            usage_data[chat_str] = {}
        if today not in usage_data[chat_str]:
            usage_data[chat_str][today] = {"count": 0, "limit": 20}
        return usage_data[chat_str][today]

def update_group_usage(chat_id, increment=1):
    with file_lock:
        usage_data = load_json_file(USAGE_DATA_FILE, {})
        today = datetime.now().strftime("%Y-%m-%d")
        chat_str = str(chat_id)
        if chat_str not in usage_data:
            usage_data[chat_str] = {}
        if today not in usage_data[chat_str]:
            usage_data[chat_str][today] = {"count": 0, "limit": 20}
        usage_data[chat_str][today]["count"] += increment
        save_json_file(USAGE_DATA_FILE, usage_data)

# ================== COURT REPORT ================== #
@bot.my_chat_member_handler(func=lambda event: True)
def track_group_add(event):
    try:
        if event.new_chat_member.status in ["member", "administrator"]:
            chat = event.chat
            added_by = event.from_user

            msg = f"""
⚖️ **NEW GROUP REPORT** ⚖️

👥 **Group:** {chat.title}
🆔 **Group ID:** `{chat.id}`
👤 **Added By:** {added_by.first_name} (ID: `{added_by.id}`)

⏱️ **Time:** {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
"""

            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("✅ Allow", callback_data=f"allow:{chat.id}:{chat.title}"),
                InlineKeyboardButton("❌ Disallow", callback_data=f"disallow:{chat.id}:{chat.title}")
            )

            for admin_id in ADMIN_IDS:
                try:
                    bot.send_message(admin_id, msg, parse_mode="Markdown", reply_markup=markup)
                except:
                    pass
    except Exception as e:
        print(f"Error tracking group add: {e}")

# ================== ADMIN ACTIONS ================== #
@bot.callback_query_handler(func=lambda call: call.data.startswith("allow:") or call.data.startswith("disallow:"))
def handle_group_admin_action(call):
    try:
        action, group_id, group_name = call.data.split(":", 2)
        group_id = str(group_id)

        allowed_groups = load_json_file(ALLOWED_GROUPS_FILE, {})

        if action == "allow":
            allowed_groups[group_id] = {
                "name": group_name,
                "added_by": call.from_user.id,
                "added_at": datetime.now().isoformat()
            }
            save_json_file(ALLOWED_GROUPS_FILE, allowed_groups)

            bot.answer_callback_query(call.id, f"✅ {group_name} allowed!", show_alert=True)
            bot.edit_message_text(f"✅ Group **{group_name}** has been authorized!",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  parse_mode="Markdown")

            try:
                usage = get_group_usage(group_id)
                remaining = max(0, usage['limit'] - usage['count'])
                welcome_msg = f"""
🎉 **Group Authorized!** 🎉

✅ This group is now allowed to use the bot.

📊 **Daily Limit:** {usage['limit']} requests
🔢 **Used Today:** {usage['count']}
⏳ **Remaining:** {remaining}

⚡ **Commands:**
• `/like <uid> <region>` → Send likes
• `/usage` → Check daily usage
• `/regions` → View supported regions
• `/status` → Bot status

💫 Powered by **Likes Bot**
"""
                bot.send_message(int(group_id), welcome_msg, parse_mode="Markdown")
            except Exception as e:
                print(f"Failed to notify group: {e}")

        elif action == "disallow":
            if group_id in allowed_groups:
                del allowed_groups[group_id]
                save_json_file(ALLOWED_GROUPS_FILE, allowed_groups)

            bot.answer_callback_query(call.id, f"❌ {group_name} disallowed!", show_alert=True)
            bot.edit_message_text(f"❌ Group **{group_name}** has been removed/disallowed!",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  parse_mode="Markdown")

            try:
                bot.send_message(int(group_id),
                                 "⚠️ This group has been **disallowed** by admin.\n\n❌ You cannot use the bot here anymore.",
                                 parse_mode="Markdown")
            except:
                pass

    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {e}", show_alert=True)

# ================== EXISTING COMMANDS (start/help/status/like etc.) ================== #
# ⚠️ Yaha pe aapke jo /start, /help, /regions, /usage, /status, /like ka pura code hai
# usko same chhod dena. Sirf upar ka "court system" add kiya gaya hai. ⚠️

# ================== START BOT ================== #
if __name__ == "__main__":
    print("🤖 Likes Bot is starting...")
    load_json_file(ALLOWED_GROUPS_FILE, {})
    load_json_file(USAGE_DATA_FILE, {})
    print("✅ Bot is ready!")
    bot.infinity_polling(none_stop=True)
