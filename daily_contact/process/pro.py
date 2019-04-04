#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os,time
'''
def test(name):
    print('hello,%s' % name)
    time.sleep(2)
    print('子进程')

if __name__ == '__main__':
    p = Process(target=test,args=('bob',))
    p.start()
    p.join()
    print('执行主进程')
'''   
#开启多个子进程

def func(i):
    time.sleep(1)
    print('%d 子进程%d，父进程：%d' % (i,os.getpid(),os.getppid()))

if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=func,args=(i,))
        p.start()
        p_list.append(p)
    
    for p in p_list:
        p.join()

    print('-------主进程--------')