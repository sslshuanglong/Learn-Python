#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
from urllib import request

with request.urlopen('http://news-at.zhihu.com/api/4/news/latest') as f:
    data = f.read()
    print('status:',f.status,f.reason)
    
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    #print('Data:', data.decode('utf-8'))
'''

import requests
r = requests.get('https://www.sina.com.cn')
print(r.status_code)
#print(r.text)

f = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(f.url)
print(r.encoding)
print(r.content)