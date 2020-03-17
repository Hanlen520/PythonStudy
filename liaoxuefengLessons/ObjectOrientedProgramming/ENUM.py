#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : ENUM.py
@Time    : 2019-08-05  22:57:52
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
练习：
把Student的gender属性改造为枚举类型，可以避免使用字符串：
"""
# from enum import Enum, unique
#
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student():
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# # 测试:
# # 这道题完全不需要改嘛！！！直接通过
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6