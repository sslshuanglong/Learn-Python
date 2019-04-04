#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime,timedelta

dt = datetime(2019,3,26,8,20)
print(dt.timestamp())
t = 1553559600.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2019-3-26 8:10:00','%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now)
print(now + timedelta(hours = 10))
print(now + timedelta(days = 1))
print(now + timedelta(days = 1,hours = 3))