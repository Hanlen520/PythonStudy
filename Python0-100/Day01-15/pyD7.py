# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD7.py
@Time    : 2019-05-23  12:35:54
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
import sys

# 列表每次查询节约时间但占空间，生成器节约空间但每次查询消耗时间
# 这个创建列表的方法有意思
# def main():
#     f = [x for x in range(1, 10)]
#     print(f)
#     f = [x + y for x in 'ABCDE' for y in '1234567']
#     print(f)
#     # 用列表的生成表达式语法创建列表容器
#     # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
#     f = [x ** 2 for x in range(1, 1000)]
#     print(sys.getsizeof(f))  # 查看对象占用内存的字节数
#     print(f)
#     # 请注意下面的代码创建的不是一个列表而是一个生成器对象
#     # 通过生成器可以获取到数据但它不占用额外的空间存储数据
#     # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
#     f = (x ** 2 for x in range(1, 1000))
#     print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
#     print(f)
#     for val in f:
#         print(val)

#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a   # 这是一个生成器函数
#
# def main():
#     for val in fib(20):
#         print(val)

# def main():
#     # 定义元组
#     t = ('骆昊', 38, True, '四川成都')
#     print(t)
#     # 获取元组中的元素
#     print(t[0])
#     print(t[3])
#     # 遍历元组中的值
#     for member in t:
#         print(member)
#     # 重新给元组赋值
#     # t[0] = '王大锤'  # TypeError
#     # 变量t重新引用了新的元组原来的元组将被垃圾回收
#     t = ('王大锤', 20, True, '云南昆明')
#     print(t)
#     # 将元组转换成列表
#     person = list(t)
#     print(person)
#     # 列表是可以修改它的元素的
#     person[0] = '李小龙'
#     person[1] = 25
#     print(person)
#     # 将列表转换成元组
#     fruits_list = ['apple', 'banana', 'orange']
#     fruits_tuple = tuple(fruits_list)
#     print(fruits_tuple)


# def main():
#     set1 = {1, 2, 3, 3, 3, 2}
#     print(set1)
#     print('Length =', len(set1))
#     set2 = set(range(1, 10))
#     print(set2)
#     set1.add(4)
#     set1.add(5)
#     set2.update([11, 12])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#     # remove的元素如果不存在会引发KeyError
#     if 4 in set2:
#         set2.remove(4)
#     print(set2)
#     # 遍历集合容器
#     for elem in set2:
#         print(elem ** 2, end=' ')
#     print()
#     # 将元组转换成集合
#     set3 = set((1, 2, 3, 3, 2, 1))
#     print(set3.pop())
#     print(set3)
#     # 集合的交集、并集、差集、对称差运算
#     print(set1 & set2)
#     # print(set1.intersection(set2))
#     print(set1 | set2)
#     # print(set1.union(set2))
#     print(set1 - set2)
#     # print(set1.difference(set2))
#     print(set1 ^ set2)
#     # print(set1.symmetric_difference(set2))
#     # 判断子集和超集
#     print(set2 <= set1)
#     # print(set2.issubset(set1))
#     print(set3 <= set1)
#     # print(set3.issubset(set1))
#     print(set1 >= set2)
#     # print(set1.issuperset(set2))
#     print(set1 >= set3)
#     # print(set1.issuperset(set3))


# def main():
#     scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
#     # 通过键可以获取字典中对应的值
#     print(scores['骆昊'])
#     print(scores['狄仁杰'])
#     # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
#     for elem in scores:
#         print('%s\t--->\t%d' % (elem, scores[elem]))
#     # 更新字典中的元素
#     scores['白元芳'] = 65
#     scores['诸葛王朗'] = 71
#     scores.update(冷面=67, 方启鹤=85)
#     print(scores)
#     if '武则天' in scores:
#         print(scores['武则天'])
#     print(scores.get('武则天'))
#     # get方法也是通过键获取对应的值但是可以设置默认值
#     print(scores.get('武则天', 60))
#     # 删除字典中的元素
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('骆昊', 100))
#     # 清空字典
#     scores.clear()
#     print(scores)


"""
练习1：在屏幕上显示跑马灯文字
"""
# 参考答案
# import os
# import time
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')    这两个字符串好像都没有实现清屏的功能，满屏的输出
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]

"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
# # 猪猪的实现，好开心！！！从代码行数来看，完败参考答案
# from random import choices
#
# def generate_verify_code(len):
#     return "".join(choices(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), k = len))
#
# # 参考答案，此做法是通过下标的随机性来实现随机，也是一种新思路。还设置了默认值，不错
# import random
#
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#
#     :param code_len: 验证码的长度(默认4个字符)
#
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code

"""
练习3：设计一个函数返回给定文件名的后缀名。
"""
# import re
#
# def get_postfix(file_name):
#     """
#     返回后缀名
#     @param file_name: 文件名
#     @return: 后缀名
#     """
#     return re.match(r'[a-zA-Z\d\_\.\s]+\.([a-zA-Z]+)$', file_name).group(1)  # 中文的正则咋写？文件名带.会不会和结尾的.混淆？
#
# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1 # 绝妙啊！直接从.后面的值开始取
#         return filename[index:]  # 这个切片用得妙呀！
#     else:
#         return ''

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""

# def get_top2_largest(list):   # 又一次打败吼吼吼
#     """
#     返回列表最大的两个值
#     @param list: 列表
#     @return: 返回最大的两个值
#     """
#     return sorted(list, reverse = True)[0:2]
#
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2

"""
练习5：计算指定的年月日是这一年的第几天

思路：
1. 判断闰年，闰年2月有29天
2. 每个月的天数
3. 兼容不同入参格式，取出年月日
"""

# def count_days(days_in_a_year, month, day):
#     """
#     计算天数
#     @param days_in_a_year: 一年中每月的天数
#     @param month: 指定月份
#     @param day: 指定某天
#     @return: 某天在这一年的第几天
#     """
#     days = 0
#     for m in range(month - 2):
#         days += days_in_a_year[m]
#     return days + day
#
# def which_day(year, month, day):
#     """
#     计算指定的年月日是这一年的第几天
#     @param year: 年份
#     @param month: 月份
#     @param day: 天数
#     @return: 天数
#     """
#     leap_year = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     common_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0: # 闰年
#         return count_days(leap_year, month, day)
#     else:
#         return count_days(common_year, month, day)

# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年
#
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天
#
#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]   #二维数组的应用方式无敌了！
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date

"""
练习6：打印杨辉三角
　　　　  　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１
"""

# def yanghui_triangle():
#     n = int(input("请输入行数n（n > 0）："))  # 总共n行
#     while n <= 0:
#         n = int(input("请输入行数n（n > 0）："))
#     last_list = []
#     for line in range(n):  # 输出的行数
#         for _ in range(n - line): # 输出空格
#             print("", end = "  ")
#         this_list = []
#         this_num = 0
#         for x in range(line + 1): # 输出行数个数字
#             if x == 0 or x == line:
#                 this_list.append(1)
#                 print(this_list[x], end = "   ")
#             else:
#                 this_num = last_list[x - 1] + last_list[x]
#                 this_list.append(this_num)
#                 print(this_num, end = "   ")
#         print()
#         last_list = this_list
#
# # 杨辉三角参考答案，用了二维数组，强大，唯一不足，打印出来不漂亮
# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()


"""
案例1：双色球选号
"""
#参考答案
# from random import randrange, randint, sample
#
# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()
#
# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
#
# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())

"""
综合案例2：约瑟夫环问题
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

# 参考答案
# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')


"""
综合案例3：井字棋游戏
"""

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()

    # yanghui_triangle()

    #print(which_day(2000, 5, 25))

    # print(which_day(1980, 11, 28))
    # print(which_day(1981, 12, 31))
    # print(which_day(2018, 1, 1))
    # print(which_day(2016, 3, 1))

    # print(get_top2_largest([9,6,0,5,3,4]))
    # print(max2([9, 6, 0, 5, 3, 4]))

    # print(generate_verify_code(8))
    # print(generate_code(8))

    #print(get_postfix("财务报表.exel"))
    #print(get_suffix(" "))
