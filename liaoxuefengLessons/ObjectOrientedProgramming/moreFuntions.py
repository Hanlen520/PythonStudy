#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : moreFuntions.py
@Time    : 2019-07-30  22:54:40
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

import logging

class Student():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self._name

    __repr__ = __str__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name  # RecursionError: maximum recursion depth exceeded while calling a Python object
        else:
            print("%s must be a string" % name)

    def __call__(self):
        return self._name + "!!!"

stu = Student("Shelly")
print(stu)
# logging.info(stu)
# stu1 = Student("Shelly")
# print(stu1)
# print(stu == stu)
# stu.having_class(stu)
# print(isinstance(stu ,Student))

print(stu())