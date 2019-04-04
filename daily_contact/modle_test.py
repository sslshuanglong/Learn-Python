#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

'''
生成随机验证码
'''

import random
import sys
from json

# random
def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65,90))
        add = random.choice([num,alf])
        code = ''.join([code,str(add)])

    return code

print(v_code())

# sys
try:
    sys.exit(1)
except SystemExit as e:
    print(e)

# json
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = json.dumps(dic)

print(type(str_dic))