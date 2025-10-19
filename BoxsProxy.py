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
                if b"/box" in dataS:
                    box_idss = ['81fd8751', '82fd8751', '83fd8751', '84fd8751', '85fd8751', '86fd8751', '87fd8751', '88fd8751', '89fd8751', '8afd8751', '8bfd8751', '8cfd8751', '8dfd8751', '8efd8751', '8ffd8751', '90fd8751', '91fd8751', '92fd8751', '93fd8751', '94fd8751', '95fd8751', '96fd8751', '97fd8751', '98fd8751', '99fd8751', '9afd8751', '9bfd8751', '9cfd8751', '9dfd8751', '9efd8751', '9ffd8751', 'a0fd8751', 'a1fd8751', 'a2fd8751', 'a3fd8751', 'a4fd8751', 'a5fd8751', 'a6fd8751', 'a7fd8751', 'a8fd8751', 'a9fd8751', 'aafd8751', 'abfd8751', 'acfd8751', 'adfd8751', 'aefd8751', 'affd8751', 'b0fd8751', 'b1fd8751', 'b2fd8751', 'b3fd8751', 'b4fd8751', 'b5fd8751', 'b6fd8751', 'b7fd8751', 'b8fd8751', 'b9fd8751', 'bafd8751', 'bbfd8751', 'bcfd8751', 'bdfd8751', 'befd8751', 'bffd8751', 'c0fd8751', 'c1fd8751', 'c2fd8751', 'c3fd8751', 'c4fd8751', 'c5fd8751', 'c6fd8751', 'c7fd8751', 'c8fd8751', 'c9fd8751', 'cafd8751', 'cbfd8751', 'ccfd8751', 'cdfd8751', 'cefd8751', 'cffd8751', 'd0fd8751', 'd1fd8751', 'd2fd8751', 'd3fd8751', 'd4fd8751', 'd5fd8751', 'd6fd8751', 'd7fd8751', 'd8fd8751', 'd9fd8751']
                    try:
                            for box_ids in box_idss:
                                self.client0500.send(bytes.fromhex(f"080000003a0888d49a9a28100820062a2e0a180896cbd130100120ffffffffffffffffff012801380140010a1208{box_ids}20ffffffffffffffffff01380108000000150888d49a9a28100820032a090a070896cbd13010010d0000000f0888d49a9a28100d20022a0308ce1a"))
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