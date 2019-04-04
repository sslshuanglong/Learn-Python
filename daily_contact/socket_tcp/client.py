#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8888))
sk.send(b'hi')
ret = sk.recv(1024)
print(ret)
sk.close()