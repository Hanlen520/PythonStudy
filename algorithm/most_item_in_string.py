# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/6/5 10:31 下午 
# @File : most_item_in_string.py 
"""


def get_most(s: str):
    """
    头条面试题
    统计一个字符串中出现次数最多字母和次数
    """
    if not s:
        return -1

    # 字典保存字母和出现的次数
    count = {}
    result = []   # 保存字母和次数数对

    # 计算每个字母出现的次数
    for ch in s:
        count[ch] = s.count(ch)

    # 获取出现最多的次数
    max_count = max(count.values())

    # 字典.items()可以同时取到key，value值
    for key, value in count.items():
        if value == max_count:
            result.append((key, value))
    return result


if __name__ == '__main__':
    s = "aaaaabbccc"
    s1 = "aaabbbc"
    s2 = ""
    print(get_most(s))
    print(get_most(s1))
    print(get_most(s2))