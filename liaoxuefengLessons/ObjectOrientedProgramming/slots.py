# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : slots.py
@Time    : 2019-07-24  12:38:24
@Author  : indeyo_lin
@Version : 
@Remark  :slots约束不能再新增属性
"""


class Animal():

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
class Dog(Animal):

    __slots__ = ('fur_color')  #子类不定义slots变量，则不能继承父类的约束，定义则可以


dog = Dog('Mexico', 'Female')
dog.fur_color = 'black&white'
print(dog.name)
print(dog.gender)
print(dog.fur_color)

animal = Animal('Xian','Male')
animal.age = 3
print(animal.name)
print(animal.gender)
print(animal.age)  # AttributeError: 'Animal' object has no attribute 'age'
