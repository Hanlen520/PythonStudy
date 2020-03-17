# -*- coding: utf-8 -*-
'''
@Project : private-document
@File    : pyD4.py
@Time    : 2019-05-16  12:12:30
@Author  : indeyo_lin
@Version : 
@Remark  :

'''

"""
练习1：输入一个数判断是不是素数。

解决思路：
遍历N能否能被从2到sqrt(N)之间的素数整除。若不能则为素数。
比如判断101是不是素数，只需要判断101是否能被【2，10】之间的素数整除，即101是否能被2、3、5、7整除即可，如果不能，则101就是素数。
"""

import math

# random_num = int(input('请输入一个整数：'))

# 参考答案
# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


"""
练习2：输入两个正整数，计算最大公约数和最小公倍数。
"""

# a = int(input('请输入正整数a：'))
# b = int(input('请输入正整数b：'))
# greatest_common_divisor = 1
# lowest_common_multiple = 1
# for x in range(1, min(a, b)):
#     if a % x == 0 and b % x == 0:
#         greatest_common_divisor = x
# lowest_common_multiple = a * b / greatest_common_divisor
# print("最大公约数: %d\n最小公倍数: %d" %(greatest_common_divisor, lowest_common_multiple))


#这个解法牛逼轰轰啊！遍历的数组从大到小来，这样就可以更快找到最大公约数了！
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

"""
练习3：打印三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""
#第三种

row = int(input('行数是：'))
for i in range(row):   # 要打印的行数
    for j in range(row):   # 打印空格
        if j < row - i - 1:
            print(' ', end = '')
    for _ in range(2 * (i + 1) - 1):  # 打印*号
            print('*', end = '')
    print()



#
# for x in range(1, 6):
#     while x:
#         print('*')
#         x -= 1
#
# for x in range(4, 0, -1):
#     y = 5 - x
#     while x:
#         print('\t')
#         x -= 1
#     while y:
#         print('*\n')


# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

# """
# 输出乘法口诀表(九九表)
#
# Version: 0.1
# Author: 骆昊
# """
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()