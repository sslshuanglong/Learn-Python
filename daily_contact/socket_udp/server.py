#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

ip_port = ('127.0.0.1',8080)
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(ip_port)

while True:
    msg,addr = sk.recvfrom(1024)
    print('来自%s的消息：%s' % (addr,msg.decode('utf-8')))
    back_msg = input('回复消息:').strip()
    sk.sendto(back_msg.encode('utf-8'),addr)

sk.close()
