# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/30 9:11 下午 
# @File : triangles.py
# @text : 杨辉三角
"""


def triangles(n):
    yield [1]
    yield [1, 1]
    arr = [1, 1]
    while n > 2:
        next_arr = [1, 1]
        for i in range(len(arr) - 1):
            next_arr.insert(i + 1, arr[i] + arr[i + 1])
        arr = next_arr
        n -= 1
        yield next_arr


def triangles_1():
    yield [1]
    yield [1, 1]
    arr = [1, 1]
    while True:
        next_arr = [1, 1]
        for i in range(len(arr) - 1):
            next_arr.insert(i + 1, arr[i] + arr[i + 1])
        arr = next_arr
        yield next_arr


def triangles_2():
    arr = [1]
    while True:
        yield arr
        arr = [arr[i] + arr[i + 1] for i in range(len(arr) - 1)]
        arr.insert(0, 1)
        arr.append(1)


if __name__ == '__main__':
    print(triangles(6))
    for i in triangles(6):
        print(i)
