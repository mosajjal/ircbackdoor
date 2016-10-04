#!/usr/bin/env python3

import sys
import socket
import string

HOST = "chat.freenode.net" # You can change this to whatever you want
PORT = 6667

NICK = "Your Nick Name"
IDENT = "Your Identity"
REALNAME = "Your REAL Name"
MASTER = "The Master of this particular Slave"

CHANNEL = "The Channel To join"

readbuffer = ""

s = socket.socket()
s.connect((HOST, PORT))
# sets the nickname inside IRC channel
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
# Connects to the server using the provided inforamtion above. The 'bla' is irrelevent
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
# Joins the Channel
s.send(bytes("JOIN #%s \r\n" % (CHANNEL), "UTF-8"))
# starts a conversation with the 'master' when joining
s.send(bytes("PRIVMSG %s :Hello Master\r\n" % MASTER, "UTF-8"))

while True:
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)

        if(line[0] == "PING"):
            s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
        if(line[1] == "PRIVMSG"):
            sender = ""
            for char in line[0]:
                if(char == "!"):
                    break
                if(char != ":"):
                    sender += char
            size = len(line)
            i = 3
            message = ""
            while(i < size):
                message += line[i] + " "
                i = i + 1
            message.lstrip(":")
            s.send(bytes("PRIVMSG %s %s \r\n" % (sender, message), "UTF-8"))
        for index, i in enumerate(line):
            print(line[index])
