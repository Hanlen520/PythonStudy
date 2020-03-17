#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD8.py
@Time    : 2019-05-27  22:01:13
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
练习1：定义一个类描述数字时钟
"""
# from time import sleep
#
# class Clock:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def run(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def print_time(self):
#         print("%02d:%02d:%02d" % (self.hour, self.minute, self.second))

"""
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""
from math import sqrt

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, end_a, end_b):
#         """
#         计算点A到点B需要移动的距离
#         @param end_a: 终点横坐标
#         @param end_b: 终点纵坐标
#         @return: 返回移动的距离，正的向上向右，负的向下向左
#         """
#         a = end_a - self.x
#         b = end_b - self.y
#         return (a, b)
#
#     def distance(self, end_a, end_b):
#         """
#         计算点A到点B之间的距离
#         @param end_a: 终点B的横坐标
#         @param end_b: 终点B的纵坐标
#         @return: 两点距离
#         """
#         return sqrt((end_a - self.x) ** 2 + (end_b - self.y) ** 2)

# 参考答案
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):  # 给了默认值
        """初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置

        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):  # 这里的other也是一个Point对象
        """计算与另一个点的距离

        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))  # 为什么强制转化成str，而不是整型？——__str__只能返回字符串

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))  #另一个点用了一个新对象

if __name__ == '__main__':

    main()

    # p1 = Point(4, 3)
    # print(p1.move(8, 2))
    # print(p1.distance(8, 2))

    # clock1 = Clock(23, 59, 58)
    # while True:
    #     clock1.run()
    #     clock1.print_time()
    #     sleep(1)

