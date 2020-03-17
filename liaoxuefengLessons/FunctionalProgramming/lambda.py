# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : lambda.py
@Time    : 2019-07-19  16:03:10
@Author  : indeyo_lin
@Version : 
@Remark  :
"""


"""
请用匿名函数改造下面的代码：
"""
def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda x : x % 2 == 1, range(1, 20)))

print(L1)
print(L2)
