#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sk = socket.socket()    # 创建一个 socket 对象
sk.bind(('127.0.0.1',8888))   # server 绑定一个 ip 和端口
sk.listen(5)

while True:
    conn,addr = sk.accept() # 获取一个客户端的连接，已经完成了三次握手，建立了连接，阻塞
    msg = conn.recv(1024)            # 阻塞，直到收到一个客户端发来的消息
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(b'Hello')     # 发送消息

    conn.close()            # 关闭 tcp 链接
sk.close()              # 关闭 scort 对象，如果不关闭还可以接受消息