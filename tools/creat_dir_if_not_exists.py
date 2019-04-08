#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
创建不存在的目录，如果已经存在提示创建成功
'''

MESSAGE = 'This dir already exists'
TESTDIR = 'testdir'

import os

try:
    home = os.path.expanduser('~')
    print(home)

    if not os.path.exists(os.path.join(home, TESTDIR)):
        os.makedirs(os.path.join(home, TESTDIR))
        print('creat success')
    else:
        print(MESSAGE)
except Exception as e:
    print(e)
