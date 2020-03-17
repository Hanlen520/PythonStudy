#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : debugging.py
@Time    : 2019-08-12  21:50:14
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

# assert语句
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

# logging
import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
# logging.info('n = %d' % n)
print(10 / n)
