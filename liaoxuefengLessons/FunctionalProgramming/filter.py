#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : filter.py
@Time    : 2019-07-16  20:49:07
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
生成素数数列
"""
# #先生成一个奇数数列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# #筛选函数
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# #选出素数
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


"""
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
"""

#整数转换列表
def int2list(n):
    L = []
    while n != 0:
        L.append(n % 10)
        n = n // 10
    return L

def is_palindrome(n):
    L = int2list(n)
    for index in range(len(L) // 2): # 比较1/2列表长度次数
        if L[index] != L[-1 - index]:
            return False
        else:
            pass
    return True

#网友答案
#读入第n个数，str(n)将数字转成字符串，str(n)[::-1]将数字转成字符串并逆序，然后两者对比，如果相同则判断是回文，返回true，filter采纳，否则filter抛弃
def is_palindrome(n):
    return str(n)==str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')