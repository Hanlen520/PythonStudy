# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/25 10:48 下午 
# @File : find_coder.py 
"""


def find_coder(arr):
    if not arr:
        return -1
    coder = []

    for s in arr:
        if "coder coder" in s:
            coder.append(s)

    return coder if coder else -1


if __name__ == '__main__':
    arr_1 = []
    arr_2 = ["coder"]
    arr_3 = ["coder coder", "aaa coder coder bbb", "adb", " coder coder "]
    print(find_coder(arr_1))
    print(find_coder(arr_2))
    print(find_coder(arr_3))