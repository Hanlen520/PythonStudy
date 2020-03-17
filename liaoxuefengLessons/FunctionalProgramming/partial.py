#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : partial.py
@Time    : 2019-07-21  10:15:30
@Author  : indeyo_lin
@Version : 
@Remark  : 偏函数
"""

from functools import partial

int2 = partial(int, base = 2)

print(int2("10000110"))