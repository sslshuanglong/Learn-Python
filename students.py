#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__auther__ = 'shuanglong'

class Students(object):
    #__slots__ = ('name','score','gender')

    def __init__(self,name,score,gender):
        self._name = name
        self._score = score
        self._gender = gender

    def print_score(self):
        print('%s,%s,%s' %(self._name,self._score,self._gender))

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self,score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')

    def get_gender(self):
        return self._gender
    
    def set_gender(self,gender):
        if (gender == 'male' or gender == 'famale'):
            self._gender = gender
        else:
            raise ValueError('bad gender')

s = Students('Tom',80,'male')
s.set_score(60)
print(s.get_score())
