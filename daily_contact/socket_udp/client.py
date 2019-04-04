#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8080)


while True:
    msg=input('请输入消息,回车发送,输入q结束和他的聊天: ').strip()
    if msg == 'q':
        break
    sk.sendto(msg.encode('utf-8'),ip_port)
    back_msg,addr=sk.recvfrom(1024)
    print('来自%s的一条消息:\033[1;44m%s\033[0m' %(addr,back_msg.decode('utf-8')))

sk.close()