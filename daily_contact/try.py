#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
__auther__ = 'shuanglong'

import logging

def foo(s):
    return 10 / int('s')

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
'''
from functools import reduce
import logging

def str2num(s):
    try:
        return int(s)
    except Exception as e:
        logging.exception(e)
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()