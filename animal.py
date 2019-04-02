#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
class Animal(object):
    def run(self):
        print('animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running...')

    def eat(self):
        print('dog eating...')

class Cat(object):
    def run(self):
        print('cat is running...')

def run_twice(Animal):
    Animal.run()
    Animal.run()

a = Dog()
b = Cat()
c = Animal()

run_twice(a)
run_twice(b)
'''

class Animal(object):
    pass

# 技能
class Runnable(object):
    def run(self):
        print('running...')

class Flyable(object):
    def fly(self):
        print('flying...')

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 动物
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
    