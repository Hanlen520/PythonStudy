# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/5/29 4:50 下午 
# @File : merge_sort.py 
"""


def merge(arr, left, mid, right):
    temp = []
    # i表示左数组的索引，j表示右数组的索引，k表示temp的索引
    i, j, k = left, mid + 1, 0

    # 对比两个数组的大小，小的进入temp
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.insert(k, arr[i])
            i += 1
        else:
            temp.insert(k, arr[j])
            j += 1
        k += 1

    # 剩下还没比较完的数组直接挪到temp后面
    if i <= mid:
        temp.extend(arr[i:mid+1])
    if j <= right:
        temp.extend(arr[j:right+1])

    # temp作为已排好序的部分，替换掉arr
    for p in range(len(temp)):
        arr[left + p] = temp[p]

    return arr


def merge_sort(arr, left, right):
    if right <= left:
        return None
    mid = (left + right) // 2

    # 递归调用
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    # 将两个排好序的数组合并到一起
    merge(arr, left, mid, right)

    return arr


if __name__ == '__main__':
    arr = [4, 45, 6, 7, 8, 1, 0, 3]
    print(merge_sort(arr, 0, len(arr) - 1))
