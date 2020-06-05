# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/6/5 11:01 下午 
# @File : most_item_in_list.py 
"""


def get_most_in_list(arr: list):
    """
    富途笔试题
    找出列表中出现次数最多的元素
    """
    if not arr:
        return -1
    count = {}
    result = []

    for i in arr:
        count[i] = arr.count(i)
    max_count = max(count.values())
    for key, value in count.items():
        if value == max_count:
            result.append(key)
    return result


if __name__ == '__main__':
    a1 = [1, 1, 1, 2, 3, 4]
    a2 = [33, 33, 33, 56, 56, 56, 77, 77]
    a3 = []
    print(get_most_in_list(a1))
    print(get_most_in_list(a2))
    print(get_most_in_list(a3))
