# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : decorator.py
@Time    : 2019-07-19  16:21:26
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

# import functools

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# now()
# print(now.__name__)


"""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""
# import time
# import functools
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         fn(*args, **kwargs)
#         end = time.time()
#         print('%s executed in %s ms' % (fn.__name__, end - start))
#         return fn(*args, **kwargs)  #如果没有这一行，则“测试失败”，因为没有将结果返回出去
#     return wrapper
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

"""
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""
import functools

def log(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print("begin call %s" % f.__name__)
            print(text)
            f(*args, **kwargs)
            print("end call %s" % f.__name__)
            # return f
        return wrapper
    return decorator

@log("execute")
def getSum(L):
    print(sum(L))

getSum([250,106,108,135])
# print(getSum([130,109,108,135]))