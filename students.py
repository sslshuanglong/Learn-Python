#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Students(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            print('A')
        elif 60 <= self.__score < 90:
            print('B')
        else:
            print('C')

bart = Students('tom',90)
bart.set_score(80)
print(bart.get_score())