#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__auther__  = 'shuanglong'

class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    def run(self):
        print('Dog is running ...')
class Cat(Animal):
    def run(self):
        pass

class Timer(object):
    def run(self):
        print('start ...')

def run_twice(animal):
        animal.run()
        animal.run()

run_twice(Animal()) 
run_twice(Dog())
run_twice(Cat())
run_twice(Timer())