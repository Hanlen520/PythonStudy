# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/28 4:20 下午 
# @File : insertion_sort.py 
"""


def insertion_sort(arr):
    if not arr:
        return -1

    for i in range(1, len(arr)):
        current = arr[i]
        # 有序区的索引
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 遇到比当前元素大的就往后挪
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


if __name__ == '__main__':
    # for i in range(0, -1, -1):
    #     print(i)

    arr = [2, 8, 49, 4, 21, 0, 45, 22, 91, 5, 10]
    print(insertion_sort(arr))
