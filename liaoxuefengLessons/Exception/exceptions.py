# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : exceptions.py
@Time    : 2019-08-07  12:40:15
@Author  : indeyo_lin
@Version : 
@Remark  :
做异常捕获的意义：
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

"""
#
# try:
#     print('try...')
#     r = 10 / 5
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# err.py:
import logging

# class FooError(ValueError):  # 一般不自己定义异常类
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value is : %s' % s)
#     return 10 / int(s)
#
# # def bar(s):
# #     return foo(s) * 2

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         # raise   # 向上抛异常
#
# bar()

#
# def main():
#     # try:
#     #     bar('0')
#     # except Exception as e:
#     #     logging.exception(e)
#     foo('0')
#
# main()
# print("END")


"""
练习：
运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
"""

from functools import reduce

def str2num(s):
    # return float(s)

    # 网友回复
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()