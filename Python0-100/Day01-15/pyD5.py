# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD5.py
@Time    : 2019-05-20  12:23:28
@Author  : indeyo_lin
@Version : 
@Remark  :
"""


"""
练习题1：寻找水仙花数

概念：
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
（例如：1^3 + 5^3+ 3^3 = 153）。
"""


# for x in range(100, 1000):
#     hundred_num = int(x / 100)
#     decade_num = int(x % 100 / 10)
#     unit_num = int(x % 100 % 10)
#     narcissistic_num = hundred_num ** 3 + decade_num ** 3 + unit_num ** 3
#     if narcissistic_num == x:
#         print(x)

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10   # // 符号是取整运算
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

"""
练习题2：寻找完美数

概念：
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
"""



import time
import math

# start = time.clock()
# for x in range(1, 10000):   # 找出10000以内的完美数
#     divisor_sum = 0
#     for divisor in range(1, x):  # 遍历比这个数小的数，找到真因子
#         if x % divisor == 0 :
#             divisor_sum += divisor
#     if divisor_sum == x:
#         print(x)
# end = time.clock()
# print("执行时间:", (end - start), "秒")
#
# start = time.clock()
# for num in range(1, 10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             sum += factor
#             if factor > 1 and num / factor != factor:  # 每个数的遍历次数减半，查找效率提高
#                 sum += num / factor
#     if sum == num:
#         print(num)
# end = time.clock()
# print("执行时间:", (end - start), "秒")

"""
练习题3：“百钱百鸡”问题

题目：
今有鸡翁一，值钱伍；鸡母一，值钱三；鸡鶵三，值钱一。凡百钱买鸡百只，问鸡翁、母、鶵各几何？
答曰：鸡翁四，值钱二十；鸡母十八，值钱五十四；鸡鶵七十八，值钱二十六。
又答：鸡翁八，值钱四十；鸡母十一，值钱三十三，鸡鶵八十一，值钱二十七。
又答：鸡翁十二，值钱六十；鸡母四、值钱十二；鸡鶵八十 四，值钱二十八。”
"""


# for cock_num in range(20):
#     for hen_num in range(30):
#         for chick_num in range(100):
#             if cock_num + hen_num + chick_num == 100 and 15 * cock_num + 9 * hen_num + chick_num == 300:
#                 print("鸡翁：%d   鸡母：%d    鸡鶵：%d" % (cock_num, hen_num, chick_num))
#
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y    # 这里少了一个循环！棒~
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


"""
练习题4：生成“斐波拉切数列”

概念：
斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........

这个数列从第3项开始，每一项都等于前两项之和。

"""
# one = 1
# two = 1
# three = 0
# print(one, two)
# while three < 10000:   # 算出10000以内的斐波拉切数列
#     three = one + two
#     print(three, end = " ")
#     one, two = two, three
#
# a = 0
# b = 1
# for _ in range(20):
#     (a, b) = (b, a + b)
#     print(a, end=' ')    # 这么简单！！！为啥我没想到呢！


"""
练习题5：Craps赌博游戏

题目：
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

# 囧。。理解错题意了。。每一次下注是一次赌博的过程，只要有一方胜出，就重新下注，从头来过。
# from random import randint
#
# deposit = 1000
# times = 0   # 记录是不是第一次
#
# # 玩家赌注输光，游戏结束
# while deposit > 0:
#     times += 1
#     wager = int(input("请输入您的赌注："))
#
#     # 判断赌注合法性
#     while wager > deposit:
#         wager = int(input("超支啦！您只有%d元赌注，请重新输入您的赌注：" % deposit))
#
#     # 游戏开始
#     if times == 1:
#         first_count = randint(2, 12)
#         if first_count == 7 or first_count == 11:
#             deposit += wager
#             print("恭喜你~ 摇出点数是：%d, 赢了%d元, 当前资产是%d元" % (first_count, wager, deposit))
#         elif first_count == 2 or first_count == 3 or first_count == 12:
#             deposit -= wager
#             print("很遗憾！摇出点数是：%d, 输了%d元, 当前资产是%d元" % (first_count, wager, deposit))
#         else:
#             print("摇出的点数是：%d，游戏继续, 当前资产是%d元" % (first_count, deposit))
#
#     else:
#         count = randint(2, 12)
#         if count == 7:
#             deposit -= wager
#             print("很遗憾！摇出点数是：%d, 输了%d元, 当前资产是%d元" % (count, wager, deposit))
#         elif count == first_count:
#             deposit += wager
#             print("恭喜你~摇出点数是：%d, 赢了%d元, 当前资产是%d元" % (count, wager, deposit))
#         else:
#             print("摇出的点数是：%d，游戏继续, 当前资产是%d元" % (count, deposit))
#
# print("输光噜！游戏结束！")



# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if debt > 0 and debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#
#     while needs_go_on:
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#             needs_go_on = False
#         elif current == first:
#             print('玩家胜')
#             money += debt
#             needs_go_on = False
#
# print('你破产了, 游戏结束!')


