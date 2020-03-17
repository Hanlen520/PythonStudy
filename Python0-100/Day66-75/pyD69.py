#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD69.py
@Time    : 2019-07-08  22:21:55
@Author  : indeyo_lin
@Version : 
@Remark  :生成器
"""

# def odd():
#     print("step one")
#     yield 1
#     print("step two")
#     yield(2)
#     print("step three")
#     yield(3)
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# for n in fib(10):
#     print(n)


# 用生成器生成杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# def Triangles(n):
#     last_line = []
#     this_line = []
#     first_line = [1]
#     second_line = [1,1]
#     for line in range(n):
#         if line == 0:
#             print(first_line)
#         if line == 1:
#             print(second_line)
#             last_line = second_line
#         this_line = [1] # 第一个是1
#         for index in range(line - 1):
#             this_line[index + 1] = last_line[index] + last_line[index + 1]
#         this_line.append(1) #最后一个是1
#         yield this_line
#         last_line = this_line
#
# for x in Triangles(5):
#     print(x)


# def triangles():
#     L = [1]
#     yield L
#     while True:
#         L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
#         yield L
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break


# L = [x * x for x in range(10) ]
# print(L)
#
# G = (x * x for x in range(10))
# print(G)
# for n in G:
#     print(n)
#
# def triangles():
#     L = [1]
#     yield L
#     while True:
#         L = [1] + [L[x] + L[x+1] for x in range(len(L) - 1) if len(L) >= 2 ] + [1]  #可以不用if语句，如果range里面为负数，不会报错，也不会有其他
#         yield L
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


for x in range(-2):
    print(x)



