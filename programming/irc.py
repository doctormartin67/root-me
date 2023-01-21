import math
import socket
import time
import base64
import codecs
import zlib

# server information
server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
nickname = "mybot"
target = "Candy"

msg = "!ep4"

# create socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
irc.connect((server, port))

# send nick and user information
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"USER {nickname} {nickname} {nickname} :Python IRC\r\n".encode())

def answer(s):
        s = s.strip()
        s = base64.b64decode(s)
        s = zlib.decompress(s)
        return s.decode()

while True:
        # receive data
        data = irc.recv(4096).decode()
        print(data)
        if data.find("001") != -1:
                # registration was successful, join channel
                irc.send(f"JOIN {channel}\r\n".encode())
        if data.find("PING") != -1:
                irc.send("PONG ".encode() + data.split()[1].encode() + "\r\n".encode())
        if data.find("PRIVMSG") != -1:
                # do something with the message
                print("Received a message!")
                print(data)
                reply = data[data.index("mybot :") + len("mybot :"):]
                print(reply)
                a = answer(reply)
                print(a)
                irc.send(f"PRIVMSG {target} :{msg} -rep {a}\r\n".encode())
        if data.find("End of /NAMES list") != -1:
                # do something when the NAMES list is complete
                print("NAMES list complete.")
                irc.send(f"PRIVMSG {target} {msg}\r\n".encode())
        if not data:
                break
        time.sleep(1)  # sleep for 60 seconds
        irc.send("PING {}\r\n".format(server).encode()) # send PING to the server

# close socket
irc.close()

