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
                if b"/bot" in dataS:
                    others_idss = ['81fbc6d202', '82fbc6d202', '83fbc6d202', '84fbc6d202', '85fbc6d202', '86fbc6d202', '87fbc6d202', '88fbc6d202', '89fbc6d202', '8afbc6d202', '8bfbc6d202', '8cfbc6d202', '8dfbc6d202', '8efbc6d202', '8ffbc6d202', '90fbc6d202', '91fbc6d202', '92fbc6d202', '93fbc6d202', '94fbc6d202', '95fbc6d202', '96fbc6d202', '97fbc6d202', '98fbc6d202', '99fbc6d202', '9afbc6d202', '9bfbc6d202', '9cfbc6d202', '9dfbc6d202', '9efbc6d202', '9ffbc6d202', 'a0fbc6d202', 'a1fbc6d202', 'a2fbc6d202', 'a3fbc6d202', 'a4fbc6d202', 'a5fbc6d202', 'a6fbc6d202', 'a7fbc6d202', 'a8fbc6d202', 'a9fbc6d202', 'aafbc6d202', 'abfbc6d202', 'acfbc6d202', 'adfbc6d202', 'aefbc6d202', 'affbc6d202', 'b0fbc6d202', 'b1fbc6d202', 'b2fbc6d202', 'b3fbc6d202', 'b4fbc6d202', 'b5fbc6d202', 'b6fbc6d202', 'b7fbc6d202', 'b8fbc6d202', 'b9fbc6d202', 'bafbc6d202', 'bbfbc6d202', 'bcfbc6d202', 'bdfbc6d202', 'befbc6d202', 'bffbc6d202', 'c0fbc6d202', 'c1fbc6d202', 'c2fbc6d202', 'c3fbc6d202', 'c4fbc6d202', 'c5fbc6d202', 'c6fbc6d202', 'c7fbc6d202', 'c8fbc6d202', 'c9fbc6d202', 'cafbc6d202', 'cbfbc6d202', 'ccfbc6d202', 'cdfbc6d202', 'cefbc6d202', 'cffbc6d202', 'd0fbc6d202', 'd1fbc6d202', 'd2fbc6d202', 'd3fbc6d202', 'd4fbc6d202', 'd5fbc6d202', 'd6fbc6d202', 'd7fbc6d202', 'd8fbc6d202', 'd9fbc6d202', 'dafbc6d202', 'dbfbc6d202', 'dcfbc6d202', 'ddfbc6d202', 'defbc6d202', 'dffbc6d202', 'e0fbc6d202', 'e1fbc6d202', 'e2fbc6d202', 'e3fbc6d202', 'e4fbc6d202', 'e5fbc6d202', 'e6fbc6d202', 'e7fbc6d202', 'e8fbc6d202', 'e9fbc6d202', 'eafbc6d202', 'ebfbc6d202', 'ecfbc6d202', 'edfbc6d202', 'eefbc6d202', 'effbc6d202', 'f0fbc6d202', 'f1fbc6d202', 'f2fbc6d202', 'f3fbc6d202', 'f4fbc6d202', 'f5fbc6d202', 'f6fbc6d202', 'f7fbc6d202', 'f8fbc6d202', 'f9fbc6d202', 'fafbc6d202', 'fbfbc6d202', 'fcfbc6d202', 'fdfbc6d202', 'fefbc6d202', 'fffbc6d202', '80fcc6d202', '81fcc6d202', '82fcc6d202', '83fcc6d202', '84fcc6d202', '85fcc6d202', '86fcc6d202', '87fcc6d202', '88fcc6d202', '89fcc6d202', '8afcc6d202', '8bfcc6d202', '8cfcc6d202', '8dfcc6d202', '8efcc6d202', '8ffcc6d202', '90fcc6d202', '91fcc6d202', '92fcc6d202','99edc8d202', '9aedc8d202', '9bedc8d202', '9cedc8d202', '9dedc8d202', '9eedc8d202', '9fedc8d202', 'a0edc8d202', 'a1edc8d202', 'a2edc8d202', 'a3edc8d202', 'a4edc8d202', 'a5edc8d202', 'a6edc8d202', 'a7edc8d202', 'a8edc8d202', 'a9edc8d202', 'aaedc8d202', 'abedc8d202', 'acedc8d202', 'adedc8d202', 'aeedc8d202', 'afedc8d202', 'b0edc8d202', 'b1edc8d202', 'b2edc8d202', 'b3edc8d202', 'b4edc8d202', 'b5edc8d202', 'b6edc8d202', 'b7edc8d202', 'b8edc8d202', 'b9edc8d202', 'baedc8d202', 'bbedc8d202', 'bcedc8d202', 'bdedc8d202', 'beedc8d202', 'bfedc8d202', 'c0edc8d202', 'c1edc8d202', 'c2edc8d202', 'c3edc8d202', 'c4edc8d202', 'c5edc8d202', 'c6edc8d202', 'c7edc8d202', 'c8edc8d202', 'c9edc8d202', 'caedc8d202', 'cbedc8d202', 'ccedc8d202', 'cdedc8d202', 'ceedc8d202', 'cfedc8d202', 'd0edc8d202', 'd1edc8d202', 'd2edc8d202', 'd3edc8d202', 'd4edc8d202', 'd5edc8d202', 'd6edc8d202', 'd7edc8d202', 'd8edc8d202', 'd9edc8d202', 'daedc8d202', 'dbedc8d202', 'dcedc8d202', 'ddedc8d202', 'd184c9d202', 'd284c9d202', 'd384c9d202', 'd484c9d202', 'd584c9d202', 'd684c9d202', 'd784c9d202', 'd884c9d202', 'd984c9d202', 'da84c9d202', 'db84c9d202', 'dc84c9d202', 'dd84c9d202', 'de84c9d202', 'df84c9d202', 'e084c9d202', 'e184c9d202', 'e284c9d202', 'e384c9d202', 'e484c9d202', 'e584c9d202', 'e684c9d202', 'e784c9d202', 'e884c9d202', 'e984c9d202', 'ea84c9d202', 'eb84c9d202', 'ec84c9d202', 'ed84c9d202', 'ee84c9d202', 'ef84c9d202', 'f084c9d202', 'f184c9d202', 'f284c9d202', 'f384c9d202', 'f484c9d202', 'f584c9d202', 'f684c9d202', 'f784c9d202', 'f884c9d202', 'f984c9d202', 'fa84c9d202', 'fb84c9d202', 'fc84c9d202', 'fd84c9d202', 'fe84c9d202', 'ff84c9d202', '8085c9d202', '8185c9d202', '8285c9d202', '8385c9d202', '8485c9d202', '8585c9d202', '8685c9d202', '8785c9d202', '8885c9d202', '8985c9d202', '8a85c9d202', '8b85c9d202', '8c85c9d202', '8d85c9d202', '8e85c9d202', '8f85c9d202', '9085c9d202', '9185c9d202', '9285c9d202', '9385c9d202', '9485c9d202', '9585c9d202', 'b98cc9d202', 'ba8cc9d202', 'bb8cc9d202', 'bc8cc9d202', 'bd8cc9d202', 'be8cc9d202', 'bf8cc9d202', 'c08cc9d202', 'c18cc9d202', 'c28cc9d202', 'c38cc9d202', 'c48cc9d202', 'c58cc9d202', 'c68cc9d202', 'c78cc9d202', 'c88cc9d202', 'c98cc9d202', 'ca8cc9d202', 'cb8cc9d202', 'cc8cc9d202', 'cd8cc9d202', 'ce8cc9d202', 'cf8cc9d202', 'd08cc9d202', 'd18cc9d202', 'd28cc9d202', 'd38cc9d202', 'd48cc9d202', 'd58cc9d202', 'd68cc9d202', 'd78cc9d202', 'd88cc9d202', 'd98cc9d202', 'da8cc9d202', 'db8cc9d202', 'dc8cc9d202', 'dd8cc9d202', 'de8cc9d202', 'df8cc9d202', 'e08cc9d202', 'e18cc9d202', 'e28cc9d202', 'e38cc9d202', 'e48cc9d202', 'e58cc9d202', 'e68cc9d202', 'e78cc9d202', 'e88cc9d202', 'e98cc9d202', 'ea8cc9d202', 'eb8cc9d202', 'ec8cc9d202', 'ed8cc9d202', 'ee8cc9d202', 'ef8cc9d202', 'f08cc9d202', 'f18cc9d202', 'f28cc9d202', 'f38cc9d202', 'f48cc9d202', 'f58cc9d202', 'f68cc9d202', 'f78cc9d202', 'f88cc9d202', 'f98cc9d202', 'fa8cc9d202', 'fb8cc9d202', 'fc8cc9d202', 'fd8cc9d202', 'a194c9d202', 'a294c9d202', 'a394c9d202', 'a494c9d202', 'a594c9d202', 'a694c9d202', 'a794c9d202', 'a894c9d202', 'a994c9d202', 'aa94c9d202', 'ab94c9d202', 'ac94c9d202', 'ad94c9d202', 'ae94c9d202', 'af94c9d202', 'b094c9d202', 'b194c9d202', 'b294c9d202', 'b394c9d202', 'b494c9d202', 'b594c9d202', 'b694c9d202', 'b794c9d202', 'b894c9d202', 'b994c9d202', 'ba94c9d202', 'bb94c9d202', 'bc94c9d202', 'bd94c9d202', 'be94c9d202', 'bf94c9d202', 'c094c9d202', 'c194c9d202', 'c294c9d202', 'c394c9d202', 'c494c9d202', 'c594c9d202', 'c694c9d202', 'c794c9d202', 'c894c9d202', 'c994c9d202', 'ca94c9d202', 'cb94c9d202', 'cc94c9d202', 'cd94c9d202', 'ce94c9d202', 'cf94c9d202', 'd094c9d202', 'd194c9d202', 'd294c9d202', 'd394c9d202', 'd494c9d202', 'd594c9d202', 'd694c9d202', 'd794c9d202', 'd894c9d202', 'd994c9d202', 'da94c9d202', 'db94c9d202', 'dc94c9d202', 'dd94c9d202', 'de94c9d202', 'df94c9d202', 'e094c9d202', 'e194c9d202', 'e294c9d202', 'e394c9d202', 'e494c9d202', 'e594c9d202', '899cc9d202', '8a9cc9d202', '8b9cc9d202', '8c9cc9d202', '8d9cc9d202', '8e9cc9d202', '8f9cc9d202', '909cc9d202', '919cc9d202', '929cc9d202', '939cc9d202', '949cc9d202', '959cc9d202', '969cc9d202', '979cc9d202', '989cc9d202', '999cc9d202', '9a9cc9d202', '9b9cc9d202', '9c9cc9d202', '9d9cc9d202', '9e9cc9d202', '9f9cc9d202', 'a09cc9d202', 'a19cc9d202', 'a29cc9d202', 'a39cc9d202', 'a49cc9d202', 'a59cc9d202', 'a69cc9d202', 'a79cc9d202', 'a89cc9d202', 'a99cc9d202', 'aa9cc9d202', 'ab9cc9d202', 'ac9cc9d202', 'ad9cc9d202', 'ae9cc9d202', 'af9cc9d202', 'b09cc9d202', 'b19cc9d202', 'b29cc9d202', 'b39cc9d202', 'b49cc9d202', 'b59cc9d202', 'b69cc9d202', 'b79cc9d202', 'b89cc9d202', 'b99cc9d202', 'ba9cc9d202', 'bb9cc9d202', 'bc9cc9d202', 'bd9cc9d202', 'be9cc9d202', 'bf9cc9d202', 'c09cc9d202', 'c19cc9d202', 'c29cc9d202', 'c39cc9d202', 'c49cc9d202', 'c59cc9d202', 'c69cc9d202', 'c79cc9d202', 'c89cc9d202', 'c99cc9d202', 'ca9cc9d202', 'cb9cc9d202', 'cc9cc9d202', 'cd9cc9d202', 'f1a3c9d202', 'f2a3c9d202', 'f3a3c9d202', 'f4a3c9d202', 'f5a3c9d202', 'f6a3c9d202', 'f7a3c9d202', 'f8a3c9d202', 'f9a3c9d202', 'faa3c9d202', 'fba3c9d202', 'fca3c9d202', 'fda3c9d202', 'fea3c9d202', 'ffa3c9d202', '80a4c9d202', '81a4c9d202', '82a4c9d202', '83a4c9d202', '84a4c9d202', '85a4c9d202', '86a4c9d202', '87a4c9d202', '88a4c9d202', '89a4c9d202', '8aa4c9d202', '8ba4c9d202', '8ca4c9d202', '8da4c9d202', '8ea4c9d202', '8fa4c9d202', '90a4c9d202', '91a4c9d202', '92a4c9d202', '93a4c9d202', '94a4c9d202', '95a4c9d202', '96a4c9d202', '97a4c9d202', '98a4c9d202', '99a4c9d202', '9aa4c9d202', '9ba4c9d202', '9ca4c9d202', '9da4c9d202', '9ea4c9d202', '9fa4c9d202', 'a0a4c9d202', 'a1a4c9d202', 'a2a4c9d202', 'a3a4c9d202', 'a4a4c9d202', 'a5a4c9d202', 'a6a4c9d202', 'a7a4c9d202', 'a8a4c9d202', 'a9a4c9d202', 'aaa4c9d202', 'aba4c9d202', 'aca4c9d202', 'ada4c9d202', 'aea4c9d202', 'afa4c9d202', 'b0a4c9d202', 'b1a4c9d202', 'b2a4c9d202', 'b3a4c9d202', 'b4a4c9d202', 'b5a4c9d202', 'd9abc9d202', 'daabc9d202', 'dbabc9d202', 'dcabc9d202', 'ddabc9d202', 'deabc9d202', 'dfabc9d202', 'e0abc9d202', 'e1abc9d202', 'e2abc9d202', 'e3abc9d202', 'e4abc9d202', 'e5abc9d202', 'e6abc9d202', 'e7abc9d202', 'e8abc9d202', 'e9abc9d202', 'eaabc9d202', 'ebabc9d202', 'ecabc9d202', 'edabc9d202', 'eeabc9d202', 'efabc9d202', 'f0abc9d202', 'f1abc9d202', 'f2abc9d202', 'f3abc9d202', 'f4abc9d202', 'f5abc9d202', 'f6abc9d202', 'f7abc9d202', 'f8abc9d202', 'f9abc9d202', 'faabc9d202', 'fbabc9d202', 'fcabc9d202', 'fdabc9d202', 'feabc9d202', 'ffabc9d202', '80acc9d202', '81acc9d202', '82acc9d202', '83acc9d202', '84acc9d202', '85acc9d202', '86acc9d202', '87acc9d202', '88acc9d202', '89acc9d202', '8aacc9d202', '8bacc9d202', '8cacc9d202', '8dacc9d202', '8eacc9d202', '8facc9d202', '90acc9d202', '91acc9d202', '92acc9d202', '93acc9d202', '94acc9d202', '95acc9d202', '96acc9d202', '97acc9d202', '98acc9d202', '99acc9d202', '9aacc9d202', '9bacc9d202', '9cacc9d202', '9dacc9d202', '91c3c9d202', '92c3c9d202', '93c3c9d202', '94c3c9d202', '95c3c9d202', '96c3c9d202', '97c3c9d202', '98c3c9d202', '99c3c9d202', '9ac3c9d202', '9bc3c9d202', '9cc3c9d202', '9dc3c9d202', '9ec3c9d202', '9fc3c9d202', 'a0c3c9d202', 'a1c3c9d202', 'a2c3c9d202', 'a3c3c9d202', 'a4c3c9d202', 'a5c3c9d202', 'a6c3c9d202', 'a7c3c9d202', 'a8c3c9d202', 'a9c3c9d202', 'aac3c9d202', 'abc3c9d202', 'acc3c9d202', 'adc3c9d202', 'aec3c9d202', 'afc3c9d202', 'b0c3c9d202', 'b1c3c9d202', 'b2c3c9d202', 'b3c3c9d202', 'b4c3c9d202', 'b5c3c9d202', 'b6c3c9d202', 'b7c3c9d202', 'b8c3c9d202', 'b9c3c9d202', 'bac3c9d202', 'bbc3c9d202', 'bcc3c9d202', 'bdc3c9d202', 'bec3c9d202', 'bfc3c9d202', 'c0c3c9d202', 'c1c3c9d202', 'c2c3c9d202', 'c3c3c9d202', 'c4c3c9d202', 'c5c3c9d202', 'c6c3c9d202', 'c7c3c9d202', 'c8c3c9d202', 'c9c3c9d202', 'cac3c9d202', 'cbc3c9d202', 'ccc3c9d202', 'cdc3c9d202', 'cec3c9d202', 'cfc3c9d202', 'd0c3c9d202', 'd1c3c9d202', 'd2c3c9d202', 'd3c3c9d202', 'd4c3c9d202', 'd5c3c9d202', 'f9cac9d202', 'facac9d202', 'fbcac9d202', 'fccac9d202', 'fdcac9d202', 'fecac9d202', 'ffcac9d202', '80cbc9d202', '81cbc9d202', '82cbc9d202', '83cbc9d202', '84cbc9d202', '85cbc9d202', '86cbc9d202', '87cbc9d202', '88cbc9d202', '89cbc9d202', '8acbc9d202', '8bcbc9d202', '8ccbc9d202', '8dcbc9d202', '8ecbc9d202', '8fcbc9d202', '90cbc9d202', '91cbc9d202', '92cbc9d202', '93cbc9d202', '94cbc9d202', '95cbc9d202', '96cbc9d202', '97cbc9d202', '98cbc9d202', '99cbc9d202', '9acbc9d202', '9bcbc9d202', '9ccbc9d202', '9dcbc9d202', '9ecbc9d202', '9fcbc9d202', 'a0cbc9d202', 'a1cbc9d202', 'a2cbc9d202', 'a3cbc9d202', 'a4cbc9d202', 'a5cbc9d202', 'a6cbc9d202', 'a7cbc9d202', 'a8cbc9d202', 'a9cbc9d202', 'aacbc9d202', 'abcbc9d202', 'accbc9d202', 'adcbc9d202', 'aecbc9d202', 'afcbc9d202', 'b0cbc9d202', 'b1cbc9d202', 'b2cbc9d202', 'b3cbc9d202', 'b4cbc9d202', 'b5cbc9d202', 'b6cbc9d202', 'b7cbc9d202', 'b8cbc9d202', 'b9cbc9d202', 'bacbc9d202', 'bbcbc9d202', 'bccbc9d202', 'bdcbc9d202', 'e1d2c9d202', 'e2d2c9d202', 'e3d2c9d202', 'e4d2c9d202', 'e5d2c9d202', 'e6d2c9d202', 'e7d2c9d202', 'e8d2c9d202', 'e9d2c9d202', 'ead2c9d202', 'ebd2c9d202', 'ecd2c9d202', 'edd2c9d202', 'eed2c9d202', 'efd2c9d202', 'f0d2c9d202', 'f1d2c9d202', 'f2d2c9d202', 'f3d2c9d202', 'f4d2c9d202', 'f5d2c9d202', 'f6d2c9d202', 'f7d2c9d202', 'f8d2c9d202', 'f9d2c9d202', 'fad2c9d202', 'fbd2c9d202', 'fcd2c9d202', 'fdd2c9d202', 'fed2c9d202', 'ffd2c9d202', '80d3c9d202', '81d3c9d202', '82d3c9d202', '83d3c9d202', '84d3c9d202', '85d3c9d202', '86d3c9d202', '87d3c9d202', '88d3c9d202', '89d3c9d202', '8ad3c9d202', '8bd3c9d202', '8cd3c9d202', '8dd3c9d202', '8ed3c9d202', '8fd3c9d202', '90d3c9d202', '91d3c9d202', '92d3c9d202', '93d3c9d202', '94d3c9d202', '95d3c9d202', '96d3c9d202', '97d3c9d202', '98d3c9d202', '99d3c9d202', '9ad3c9d202', '9bd3c9d202', '9cd3c9d202', '9dd3c9d202', '9ed3c9d202', '9fd3c9d202', 'a0d3c9d202', 'a1d3c9d202', 'a2d3c9d202', 'a3d3c9d202', 'a4d3c9d202', 'a5d3c9d202', 'c9dac9d202', 'cadac9d202', 'cbdac9d202', 'ccdac9d202', 'cddac9d202', 'cedac9d202', 'cfdac9d202', 'd0dac9d202', 'd1dac9d202', 'd2dac9d202', 'd3dac9d202', 'd4dac9d202', 'd5dac9d202', 'd6dac9d202', 'd7dac9d202', 'd8dac9d202', 'd9dac9d202', 'dadac9d202', 'dbdac9d202', 'dcdac9d202', 'dddac9d202', 'dedac9d202', 'dfdac9d202', 'e0dac9d202', 'e1dac9d202', 'e2dac9d202', 'e3dac9d202', 'e4dac9d202', 'e5dac9d202', 'e6dac9d202', 'e7dac9d202', 'e8dac9d202', 'e9dac9d202', 'eadac9d202', 'ebdac9d202', 'ecdac9d202', 'eddac9d202', 'eedac9d202', 'efdac9d202', 'f0dac9d202', 'f1dac9d202', 'f2dac9d202', 'f3dac9d202', 'f4dac9d202', 'f5dac9d202', 'f6dac9d202', 'f7dac9d202', 'f8dac9d202', 'f9dac9d202', 'fadac9d202', 'fbdac9d202', 'fcdac9d202', 'fddac9d202', 'fedac9d202', 'ffdac9d202', '80dbc9d202', '81dbc9d202', '82dbc9d202', '83dbc9d202', '84dbc9d202', '85dbc9d202', '86dbc9d202', '87dbc9d202', '88dbc9d202', '89dbc9d202', '8adbc9d202', '8bdbc9d202', '8cdbc9d202', '8ddbc9d202', 'b1e2c9d202', 'b2e2c9d202', 'b3e2c9d202', 'b4e2c9d202', 'b5e2c9d202', 'b6e2c9d202', 'b7e2c9d202', 'b8e2c9d202', 'b9e2c9d202', 'bae2c9d202', 'bbe2c9d202', 'bce2c9d202', 'bde2c9d202', 'bee2c9d202', 'bfe2c9d202', 'c0e2c9d202', 'c1e2c9d202', 'c2e2c9d202', 'c3e2c9d202', 'c4e2c9d202', 'c5e2c9d202', 'c6e2c9d202', 'c7e2c9d202', 'c8e2c9d202', 'c9e2c9d202', 'cae2c9d202', 'cbe2c9d202', 'cce2c9d202', 'cde2c9d202', 'cee2c9d202', 'cfe2c9d202', 'd0e2c9d202', 'd1e2c9d202', 'd2e2c9d202', 'd3e2c9d202', 'd4e2c9d202', 'd5e2c9d202', 'd6e2c9d202', 'd7e2c9d202', 'd8e2c9d202', 'd9e2c9d202', 'dae2c9d202', 'dbe2c9d202', 'dce2c9d202', 'dde2c9d202', 'dee2c9d202', 'dfe2c9d202', 'e0e2c9d202', 'e1e2c9d202', 'e2e2c9d202', 'e3e2c9d202', 'e4e2c9d202', 'e5e2c9d202', 'e6e2c9d202', 'e7e2c9d202', 'e8e2c9d202', 'e9e2c9d202', 'eae2c9d202', 'ebe2c9d202', 'ece2c9d202', 'ede2c9d202', 'eee2c9d202', 'efe2c9d202', 'f0e2c9d202', 'f1e2c9d202', 'f2e2c9d202', 'f3e2c9d202', 'f4e2c9d202', 'f5e2c9d202', '99eac9d202', '9aeac9d202', '9beac9d202', '9ceac9d202', '9deac9d202', '9eeac9d202', '9feac9d202', 'a0eac9d202', 'a1eac9d202', 'a2eac9d202', 'a3eac9d202', 'a4eac9d202', 'a5eac9d202', 'a6eac9d202', 'a7eac9d202', 'a8eac9d202', 'a9eac9d202', 'aaeac9d202', 'abeac9d202', 'aceac9d202', 'adeac9d202', 'aeeac9d202', 'afeac9d202', 'b0eac9d202', 'b1eac9d202', 'b2eac9d202', 'b3eac9d202', 'b4eac9d202', 'b5eac9d202', 'b6eac9d202', 'b7eac9d202', 'b8eac9d202', 'b9eac9d202', 'baeac9d202', 'bbeac9d202', 'bceac9d202', 'bdeac9d202', 'beeac9d202', 'bfeac9d202', 'c0eac9d202', 'c1eac9d202', 'c2eac9d202', 'c3eac9d202', 'c4eac9d202', 'c5eac9d202', 'c6eac9d202', 'c7eac9d202', 'c8eac9d202', 'c9eac9d202', 'caeac9d202', 'cbeac9d202', 'cceac9d202', 'cdeac9d202', 'ceeac9d202', 'cfeac9d202', 'd0eac9d202', 'd1eac9d202', 'd2eac9d202', 'd3eac9d202', 'd4eac9d202', 'd5eac9d202', 'd6eac9d202', 'd7eac9d202', 'd8eac9d202', 'd9eac9d202', 'daeac9d202', 'dbeac9d202', 'dceac9d202', 'ddeac9d202', '81f2c9d202', '82f2c9d202', '83f2c9d202', '84f2c9d202', '85f2c9d202', '86f2c9d202', '87f2c9d202', '88f2c9d202', '89f2c9d202', '8af2c9d202', '8bf2c9d202', '8cf2c9d202', '8df2c9d202', '8ef2c9d202', '8ff2c9d202', '90f2c9d202', '91f2c9d202', '92f2c9d202', '93f2c9d202', '94f2c9d202', '95f2c9d202', '96f2c9d202', '97f2c9d202', '98f2c9d202', '99f2c9d202', '9af2c9d202', '9bf2c9d202', '9cf2c9d202', '9df2c9d202', '9ef2c9d202', '9ff2c9d202', 'a0f2c9d202', 'a1f2c9d202', 'a2f2c9d202', 'a3f2c9d202', 'a4f2c9d202', 'a5f2c9d202', 'a6f2c9d202', 'a7f2c9d202', 'a8f2c9d202', 'a9f2c9d202', 'aaf2c9d202', 'abf2c9d202', 'acf2c9d202', 'adf2c9d202', 'aef2c9d202', 'aff2c9d202', 'b0f2c9d202', 'b1f2c9d202', 'b2f2c9d202', 'b3f2c9d202', 'b4f2c9d202', 'b5f2c9d202', 'b6f2c9d202', 'b7f2c9d202', 'b8f2c9d202', 'b9f2c9d202', 'baf2c9d202', 'bbf2c9d202', 'bcf2c9d202', 'bdf2c9d202', 'bef2c9d202', 'bff2c9d202', 'c0f2c9d202', 'c1f2c9d202', 'c2f2c9d202', 'c3f2c9d202', 'c4f2c9d202', 'c5f2c9d202', 'e9f9c9d202', 'eaf9c9d202', 'ebf9c9d202', 'ecf9c9d202', 'edf9c9d202', 'eef9c9d202', 'eff9c9d202', 'f0f9c9d202', 'f1f9c9d202', 'f2f9c9d202', 'f3f9c9d202', 'f4f9c9d202', 'f5f9c9d202', 'f6f9c9d202', 'f7f9c9d202', 'f8f9c9d202', 'f9f9c9d202', 'faf9c9d202', 'fbf9c9d202', 'fcf9c9d202', 'fdf9c9d202', 'fef9c9d202', 'fff9c9d202', '80fac9d202', '81fac9d202', '82fac9d202', '83fac9d202', '84fac9d202', '85fac9d202', '86fac9d202', '87fac9d202', '88fac9d202', '89fac9d202', '8afac9d202', '8bfac9d202', '8cfac9d202', '8dfac9d202', '8efac9d202', '8ffac9d202', '90fac9d202', '91fac9d202', '92fac9d202', '93fac9d202', '94fac9d202', '95fac9d202', '96fac9d202', '97fac9d202', '98fac9d202', '99fac9d202', '9afac9d202', '9bfac9d202', '9cfac9d202', '9dfac9d202', '9efac9d202', '9ffac9d202', 'a0fac9d202', 'a1fac9d202', 'a2fac9d202', 'a3fac9d202', 'a4fac9d202', 'a5fac9d202', 'a6fac9d202', 'a7fac9d202', 'a8fac9d202', 'a9fac9d202', 'aafac9d202', 'abfac9d202', 'acfac9d202', 'adfac9d202']
                    for others_ids in others_idss:
                        self.client0500.send(bytes.fromhex(f"08000000be08c0c5cefb18100820062ab1010a1808d885d164100120ffffffffffffffffff012801380140020a1808d985d164100120ffffffffffffffffff012801380140020a1808fe928866100120ffffffffffffffffff012801380140020a1808cfe1e860100120ffffffffffffffffff012801380140020a18088fe6a561100120ffffffffffffffffff012801380140020a1808cfeae261100120ffffffffffffffffff012801380140020a1308{others_ids}20ffffffffffffffffff013801"))
                        time.sleep(0.2)
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
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        try:
            s.bind((ip, port))
            s.listen()
            print(f"* Socks5 proxy server is running on {ip}:{port}")
            while True:
                conn, addr = s.accept()
                t = threading.Thread(target=self.handle_client, args=(conn,))
                t.daemon = True
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
        t.daemon = True
        t.start()
        threads.append(t)
        while True:
            pass
    except Exception as e:
        print(f"Error in start_bot: {e}")
if __name__ == "__main__":
    start_bot()