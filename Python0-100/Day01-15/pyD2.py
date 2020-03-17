# -*- coding: utf-8 -*-
'''
@Project : StudyPython0-100
@File    : pyD2.py
@Time    : 2019-05-13  19:56:01
@Author  : indeyo_lin
@Version : 
@Remark  :

'''

'''
练习一：华氏温度转摄氏温度
F = 1.8C + 32
'''

# F = int(input('请输入华氏温度:'))
# print('摄氏温度是: %f' % ((F - 32)/1.8))
#
# #参考答案
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))


"""
练习二：输入半径计算圆的周长和面积
"""
import math

# r = float(input('请输入半径:'))
# c = 2 * math.pi * r
# s = math.pi * r ** 2
# print('半径为%f的圆周长为%.2f' % (r, c))
# print('半径为%f的圆面积为%.2f' %    (r, s))
#
# #参考答案
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

"""
练习三：输入年份判断是不是闰年
"""

year = int(input('请输入年份：'))
if year % 400 == 0 :
    print('%d是闰年' % year)
elif year % 4 == 0 :
    print('%d是闰年' % year)
else :
    print('%d不是闰年' % year)

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

# a = 5
# b = 10
# c = 3
# d = 4
# e = 5
# a += b
# a -= c
# a *= d
# a /= e
# print("a = ", a)
#
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not False)
#
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#
# # a = 3
# # b = 2
# # print(a // b)
# # print(a % b)
# # print(a ** b)
#
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
#
# print('%d + %d = %d' % (a, b, a+b))