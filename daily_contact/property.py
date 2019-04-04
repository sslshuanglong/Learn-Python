#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

__auther__ = 'shuanglong'
'''
class students(object):

    @property 
    def score(self):
        return self._score   

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must beteen 0-100')
        self._score = value

    @property
    def birth(self):
        return self._birth
    
    @birth_setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth

s = students()
s.score = 999
print(s.score)
'''

class Screen(object):
    @property
    def width(self):
        return self._width 

    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError('width must greater than 0')
        self._width = value

    @property
    def height(self):
        return self._height 

    @height.setter
    def height(self,value):
        if value < 0:
            raise ValueError('height must greater than 0')
        self._height = value  

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = -10
s.height = 90
print(s.width)
print(s.height)
print('screen size:', s.resolution)