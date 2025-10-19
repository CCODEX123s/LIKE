import socket
import select
import requests
import threading
import re
import time
import struct
import random
import urllib3
from datetime import datetime
#━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#CLASS SOCKES5!
SOCKS_VERSION = 5
class Proxy:
    def __init__(self):
        self.username = "bot"
        self.password = "bot"
    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS_VERSION, 2]))
        if not self.verify_credentials(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
            else:
                connection.close()
            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
            port = bind_address[1]
            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            reply = self.generate_failed_reply(address_type, 5)
        connection.sendall(reply)
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)
        connection.close()
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def get_bot(self):
        try:
            get_bot1 = f""
            self.client0500.send(bytes.fromhex(get_bot1))    
        except:
            pass
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def handle_id(self, iddd):
        if '***' in iddd:
            iddd = iddd.replace('***', '106')
        iddd = str(iddd).split('(\\x')[0]
        add_id_packet = self.Encrypt_ID(iddd)
        finale_packet = Danse_Players(add_id_packet)
        self.client0500.send(bytes.fromhex(finale_packet))
#━━━━━━━━━━━━━━━━━━━
    def exchange_loop(self, client, remote):
        global fake_friend, spam_room, spam_inv, get_room_code, packet_start, recode_packet, bot_true, bot_codes
        while True:
            r, w, e = select.select([client, remote], [], [])
            #CLIENT
            if client in r:
                try:
                    dataC = client.recv(9999)
                except:
                    break
                #ports
                if "39699" in str(client):
                    self.client0500 = client
                if "39699" in str(remote):
                    self.remote0500 = remote
                try:
                    if remote.send(dataC) <= 0:
                        break 
                except:
                    break 
            #SERVER
            if remote in r:
                try:
                    dataS = remote.recv(9999)
                except:
                    break
                self.EncryptedPlayerid = dataS.hex()[12:22]
                self.client1200 = client
                if "0500" in dataS.hex()[0:4]:
                    self.client0500 = client
                if b"/evo" in dataS:
                    wep_idss = ['9181bfb003', '9281bfb003', '9381bfb003', '9481bfb003', '9581bfb003', '9681bfb003', '9781bfb003', '9881bfb003', '9981bfb003', '9a81bfb003', '9b81bfb003', '9c81bfb003', '9d81bfb003', '9e81bfb003', '9f81bfb003', 'a081bfb003', 'a181bfb003', 'a281bfb003', 'a381bfb003', 'a481bfb003', 'a581bfb003', 'a681bfb003', 'a781bfb003', 'a881bfb003', 'c1f1beb003', 'c2f1beb003', 'c3f1beb003', 'c4f1beb003', 'c5f1beb003', 'c6f1beb003', 'c7f1beb003', 'c8f1beb003', 'c9f1beb003', 'caf1beb003', 'cbf1beb003', 'ccf1beb003', 'cdf1beb003', 'cef1beb003', 'cff1beb003', 'd0f1beb003', 'd1f1beb003', 'd2f1beb003', 'd3f1beb003', 'd4f1beb003', 'd5f1beb003', 'd6f1beb003', 'd7f1beb003', 'd8f1beb003', 'd9f1beb003', 'daf1beb003', 'dbf1beb003', 'dcf1beb003', 'ddf1beb003', 'def1beb003', 'dff1beb003', 'e0f1beb003', 'e1f1beb003', 'e2f1beb003', 'e3f1beb003', 'e4f1beb003', 'e5f1beb003', 'e6f1beb003', 'e7f1beb003', 'e8f1beb003', 'e9f1beb003', 'eaf1beb003', 'ebf1beb003', 'ecf1beb003', 'edf1beb003', 'eef1beb003', 'eff1beb003', 'f0f1beb003', 'f1f1beb003', 'f2f1beb003', 'f3f1beb003', 'f4f1beb003', 'f5f1beb003', 'f6f1beb003', 'f7f1beb003', 'f8f1beb003', 'f9f1beb003', 'faf1beb003', 'fbf1beb003', 'fcf1beb003', 'fdf1beb003', 'fef1beb003', 'fff1beb003', '80f2beb003', '81f2beb003', '82f2beb003', '83f2beb003', '84f2beb003', '85f2beb003', '86f2beb003', '87f2beb003', '88f2beb003', '89f2beb003', '8af2beb003', '8bf2beb003', '8cf2beb003', '8df2beb003', '8ef2beb003', '8ff2beb003', '90f2beb003', '91f2beb003', '92f2beb003', '93f2beb003', '94f2beb003', '95f2beb003', '96f2beb003', '97f2beb003', '98f2beb003', '99f2beb003', '9af2beb003', '9bf2beb003', '9cf2beb003', '9dfdbeb003', '9efdbeb003', '9ffdbeb003', 'a0fdbeb003', 'a1fdbeb003', 'a2fdbeb003', 'a3fdbeb003', 'a4fdbeb003', 'a5fdbeb003', 'a6fdbeb003', 'a7fdbeb003', 'a8fdbeb003', 'a9fdbeb003', 'aafdbeb003', 'abfdbeb003', 'acfdbeb003', 'adfdbeb003', 'aefdbeb003', 'affdbeb003', 'b0fdbeb003', 'b1fdbeb003', 'b2fdbeb003', 'b3fdbeb003', 'b4fdbeb003', 'b9fcbeb003', 'bafcbeb003', 'bbfcbeb003', 'bcfcbeb003', 'bdfcbeb003', 'befcbeb003', 'bffcbeb003', 'c0fcbeb003', 'c1fcbeb003', 'c2fcbeb003', 'c3fcbeb003', 'c4fcbeb003', 'c5fcbeb003', 'c6fcbeb003', 'c7fcbeb003', 'c8fcbeb003', 'c9fcbeb003', 'cafcbeb003', 'cbfcbeb003', 'ccfcbeb003', 'cdfcbeb003', 'cefcbeb003', 'cffcbeb003', 'd0fcbeb003', 'd1fcbeb003', 'd2fcbeb003', 'd3fcbeb003', 'd4fcbeb003', 'd5fcbeb003', 'd6fcbeb003', 'd7fcbeb003', 'd8fcbeb003', 'd9fcbeb003', 'dafcbeb003', 'dbfcbeb003', 'dcfcbeb003', 'ddfcbeb003', 'defcbeb003', 'dffcbeb003', 'e0fcbeb003', 'e1fcbeb003', 'e2fcbeb003', 'e3fcbeb003', 'd5fbbeb003', 'd6fbbeb003', 'd7fbbeb003', 'd8fbbeb003', 'd9fbbeb003', 'dafbbeb003', 'dbfbbeb003', 'dcfbbeb003', 'ddfbbeb003', 'defbbeb003', 'dffbbeb003', 'e0fbbeb003', 'e1fbbeb003', 'e2fbbeb003', 'e3fbbeb003', 'e4fbbeb003', 'e5fbbeb003', 'e6fbbeb003', 'e7fbbeb003', '81febeb003', '82febeb003', '83febeb003', '84febeb003', '85febeb003', '86febeb003', '87febeb003', '88febeb003', '89febeb003', '8afebeb003', '8bfebeb003', '8cfebeb003', '8dfebeb003', '8efebeb003', '8ffebeb003', '90febeb003', '91febeb003', '92febeb003', '93febeb003', '94febeb003', '95febeb003', '96febeb003', '97febeb003', '98febeb003', '99febeb003', '9afebeb003', '9bfebeb003', '9cfebeb003', '9dfebeb003', 'e5febeb003', 'e6febeb003', 'e7febeb003', 'e8febeb003', 'e9febeb003', 'eafebeb003', 'ebfebeb003', 'ecfebeb003', 'edfebeb003', 'eefebeb003', 'effebeb003', 'f0febeb003', 'f1febeb003', 'f2febeb003', 'f3febeb003', 'f4febeb003', 'f5febeb003', 'f6febeb003', 'f7febeb003', 'f8febeb003', 'f9febeb003', 'fafebeb003', 'fbfebeb003', 'fcfebeb003', 'c9ffbeb003', 'caffbeb003', 'cbffbeb003', 'ccffbeb003', 'cdffbeb003', 'ceffbeb003', 'cfffbeb003', 'd0ffbeb003', 'd1ffbeb003', 'd2ffbeb003', 'd3ffbeb003', 'd4ffbeb003', 'd5ffbeb003', 'd6ffbeb003', 'd7ffbeb003', 'd8ffbeb003', 'd9ffbeb003', 'daffbeb003', 'dbffbeb003', 'dcffbeb003', 'ddffbeb003', 'deffbeb003', 'dfffbeb003', 'e0ffbeb003', 'ad80bfb003', 'ae80bfb003', 'af80bfb003', 'b080bfb003', 'b180bfb003', 'b280bfb003', 'b380bfb003', 'b480bfb003', 'b580bfb003', 'b680bfb003', 'b780bfb003', 'b880bfb003', 'b980bfb003', 'ba80bfb003', 'bb80bfb003', 'bc80bfb003', 'bd80bfb003', 'be80bfb003', 'bf80bfb003', 'c080bfb003', 'c180bfb003', 'c280bfb003', 'c380bfb003', 'c480bfb003','cbd4cab003', 'd3d0cab003', 'd4d0cab003', 'd5d0cab003', 'd6d0cab003', 'e985bfb003', 'ea85bfb003', 'eb85bfb003', 'ec85bfb003', 'ed85bfb003', 'ee85bfb003', 'ef85bfb003', 'f085bfb003', 'f185bfb003', 'f285bfb003', 'f385bfb003', 'f485bfb003', 'f585bfb003', 'f685bfb003', 'f785bfb003', 'f885bfb003', 'f985bfb003', 'fa85bfb003', 'fb85bfb003', 'fc85bfb003', 'fd85bfb003', 'fe85bfb003', 'ff85bfb003', '8086bfb003', '8186bfb003', '8286bfb003', '8386bfb003', '8486bfb003', '8586bfb003', '8686bfb003', '8786bfb003', '8886bfb003', '8986bfb003', '8a86bfb003', '8585bfb003', '8685bfb003', '8785bfb003', '8885bfb003', '8985bfb003', '8a85bfb003', '8b85bfb003', '8c85bfb003', '8d85bfb003', '8e85bfb003', '8f85bfb003', '9085bfb003', '9185bfb003', '9285bfb003', '9385bfb003', '9485bfb003', '9585bfb003', '9685bfb003', '9785bfb003', '9885bfb003', '9985bfb003', '9a85bfb003', '9b85bfb003', '9c85bfb003', '9d85bfb003', '9e85bfb003', '9f85bfb003', 'a085bfb003', 'a185bfb003', 'a285bfb003', 'a385bfb003', 'a485bfb003', 'a585bfb003', 'a685bfb003', 'a184bfb003', 'a284bfb003', 'a384bfb003', 'a484bfb003', 'a584bfb003', 'a684bfb003', 'a784bfb003', 'a884bfb003', 'a984bfb003', 'aa84bfb003', 'ab84bfb003', 'ac84bfb003', 'ad84bfb003', 'ae84bfb003', 'af84bfb003', 'b084bfb003', 'b184bfb003', 'b284bfb003', 'b384bfb003', 'b484bfb003', 'b584bfb003', 'b684bfb003', 'b784bfb003', 'b884bfb003', 'b984bfb003', 'ba84bfb003', 'bb84bfb003', 'bc84bfb003', 'bd84bfb003', 'be84bfb003', 'bf84bfb003', 'c084bfb003', 'c184bfb003', 'c284bfb003', 'c384bfb003', 'c484bfb003', 'bd83bfb003', 'be83bfb003', 'bf83bfb003', 'c083bfb003', 'c183bfb003', 'c283bfb003', 'c383bfb003', 'c483bfb003', 'c583bfb003', 'c683bfb003', 'c783bfb003', 'c883bfb003', 'c983bfb003', 'ca83bfb003', 'cb83bfb003', 'cc83bfb003', 'cd83bfb003', 'ce83bfb003', 'cf83bfb003', 'd083bfb003', 'd183bfb003', 'd283bfb003', 'd383bfb003', 'd982bfb003', 'da82bfb003', 'db82bfb003', 'dc82bfb003', 'dd82bfb003', 'de82bfb003', 'df82bfb003', 'e082bfb003', 'e182bfb003', 'e282bfb003', 'e382bfb003', 'e482bfb003', 'e582bfb003', 'e682bfb003', 'e782bfb003', 'e882bfb003', 'e982bfb003', 'ea82bfb003', 'eb82bfb003', 'ec82bfb003', 'ed82bfb003', 'ee82bfb003', 'ef82bfb003', 'f082bfb003', 'f182bfb003', 'f282bfb003', 'f382bfb003', 'f482bfb003', 'f582bfb003', 'f682bfb003', 'f782bfb003', 'f581bfb003', 'f681bfb003', 'f781bfb003', 'f881bfb003', 'f981bfb003', 'fa81bfb003', 'fb81bfb003', 'fc81bfb003', 'fd81bfb003', 'fe81bfb003', 'ff81bfb003', '8082bfb003', '8182bfb003', '8282bfb003', '8382bfb003', '8482bfb003', '8582bfb003', '8682bfb003', '8782bfb003', '8882bfb003', '8982bfb003', '8a82bfb003', 'bbd1cab003', '9fd2cab003', '83d3cab003', 'e7d3cab003','e9decab003', '85decab003', '95e1cab003', 'dfdecab003', 'fbddcab003', '97ddcab003', 'afd5cab003']
                    try:
                            for wep_ids in wep_idss:
                                self.client0500.send(bytes.fromhex(f"080000003308e7e8e8ba30100820062a270a2508{wep_ids}100118a5f1bec50620ffffffffffffffffff0128013080e90f380240097003"))
                                time.sleep(0.05)
                    except:
                        pass
                if client.send(dataS) <= 0:
                    pass
#━━━━━━━━━━━━━━━━━━━
    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ]) 
    def verify_credentials(self, connection):
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password = connection.recv(password_len).decode('utf-8')
        if username == self.username and password == self.password:
            response = bytes([version, 0])
            connection.sendall(response)
            return True
        else:
            response = bytes([version, 0])
            connection.sendall(response)
            return True  
    def get_available_methods(self, nmethods, connection):
        methods = []
        for _ in range(nmethods):
            methods.append(connection.recv(1)[0])
        return methods
    def run(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # تكفي مرة واحدة
        try:
            s.bind((ip, port))
            s.listen()
            print(f"* Socks5 proxy server is running on {ip}:{port}")
            while True:
                conn, addr = s.accept()
                t = threading.Thread(target=self.handle_client, args=(conn,))
                t.daemon = True  # ⬅️ تجعل الثريد ينتهي عند إغلاق البرنامج
                t.start()
        except OSError as e:
            print(f"Error: {e} (Port may be in use)")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            s.close()

def start_bot():
    threads = []
    try:
        proxy = Proxy()
        t = threading.Thread(target=proxy.run, args=("127.0.0.1", 1080))
        t.daemon = True  # ⬅️ تجعل الثريد الرئيسي ينتهي عند إغلاق البرنامج
        t.start()
        threads.append(t)
        
        # الانتظار إلى الأبد (بدون join الذي يسبب التوقف)
        while True:
            pass
    except Exception as e:
        print(f"Error in start_bot: {e}")

if __name__ == "__main__":
    start_bot()