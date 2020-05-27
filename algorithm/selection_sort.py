# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/26 4:43 下午 
# @File : selection_sort.py 
"""


def selection_sort(arr):
    if not arr:
        return -1

    # 遍历n-1趟
    for i in range(len(arr) - 1):
        # 找到无序区中最小值
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # 无序区第一个元素和无序区最小值交换
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    arr = [4, 45, 6, 7, 8, 1, 0, 3]
    print(selection_sort(arr))
