#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD6.py
@Time    : 2019-05-21  22:43:43
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
练习1：实现计算求最大公约数和最小公倍数的函数。
"""
# 最大公约数
# def gcd(x, y):
#     if x > y :
#         x, y = y, x
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
#
# # 最小公倍数
# def lcm(x, y):
#     return int(x * y / gcd(x, y))
#     #return x * y // gcd(x, y)   # //代表整数除法
#
# print(lcm(15, 19))


"""
练习2：实现判断一个数是不是回文数的函数。

设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数。
注意：
1.偶数个的数字也有回文数124421
2.小数没有回文数
"""

def palindromic_num(x):
    num = []
    y = x
    while y > 0:  # 取出每一位
        num.append(y % 10)   # 列表插入元素用append()准没错！别再用i++赋值的方式啦
        y = y // 10
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10  # 把整个数颠倒过来了，注意题干
        temp //= 10
    return total == num  # 判断颠倒过来的数和原来的数对比


"""
练习3：实现判断一个数是不是素数的函数

解决思路：
遍历N能否能被从2到sqrt(N)之间的素数整除。若不能则为素数。
比如判断101是不是素数，只需要判断101是否能被【2，10】之间的素数整除，即101是否能被2、3、5、7整除即可，如果不能，则101就是素数。
"""

from math import sqrt

def is_prime(x):
    end = int(sqrt(x))
    for fator in range(2, end + 1):
        if x % fator == 0:
            return False
    return True if x != 1 else False   #  return True if num != 1 else False，这里需要补充一个判断，这个正整数不是1

"""
练习4：写一个程序判断输入的正整数是不是回文素数
"""

if __name__ == '__main__':
    x = int(input("please input a positive integer:"))
    if is_palindrome(x) and is_prime(x):
        print(True)
    else:
        print(False)

