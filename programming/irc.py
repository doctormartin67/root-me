import math
import socket
import time

# server information
server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
nickname = "mybot"
target = "Candy"

# create socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
irc.connect((server, port))

# send nick and user information
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"USER {nickname} {nickname} {nickname} :Python IRC\r\n".encode())

def parse(s):
        a = float(s[1][1:])
        b = float(s[3].strip())
        return round(math.sqrt(a) * b, 2)

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
                print(data[-18:].split(" "))
                c = parse(data[-18:].split(" "))
                irc.send(f"PRIVMSG {target} :!ep1 -rep {c}\r\n".encode())
                print(c)
        if data.find("End of /NAMES list") != -1:
                # do something when the NAMES list is complete
                print("NAMES list complete.")
                irc.send(f"PRIVMSG {target} :!ep1\r\n".encode())
        if not data:
                break
        time.sleep(1)  # sleep for 60 seconds
        irc.send("PING {}\r\n".format(server).encode()) # send PING to the server

# close socket
irc.close()

