#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : Iterator.py
@Time    : 2019-07-11  07:58:27
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from collections import Iterable
from collections import Iterator

#判断是否可迭代
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance((), Iterable))
# print(isinstance('ABC', Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(100, Iterable))

#判断迭代器
# print(isinstance([], Iterator))
# print(isinstance({}, Iterator))
# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance(100, Iterator))

#编程迭代器
print(isinstance(iter([]), Iterator))