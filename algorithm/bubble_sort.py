# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : bubble_sort.py
@Time    : 2020-05-04  17:25:38
@Author  : indeyo_lin
"""


class BubbleSort:
    def bubble_sort(self, arr: list):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j] > arr[j + 1]:
                    self.swap(arr, j, j + 1)

    def swap(self, arr: list, x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp


if __name__ == '__main__':
    s = BubbleSort()
    arr = [2, 8, 49, 4, 21, 0, 45, 22, 91, 5, 10]

    s.bubble_sort(arr)
    print(arr)