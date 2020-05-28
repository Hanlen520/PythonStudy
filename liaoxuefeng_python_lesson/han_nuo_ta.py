# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/28 10:02 下午 
# @File : han_nuo_ta.py 
"""


def move(n, a, b, c):
    """
    汉诺塔问题：
        请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
        然后打印出把所有盘子从A借助B移动到C的方法，例如：
        期待输出:
        A --> C
        A --> B
        C --> B
        A --> C
        B --> A
        B --> C
        A --> C
        move(3, 'A', 'B', 'C')
    """
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


if __name__ == '__main__':
    print(move(3, 'A', 'B', 'C'))
