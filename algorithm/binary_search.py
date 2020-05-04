# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : binary_search.py
@Time    : 2020-05-04  16:12:24
@Author  : indeyo_lin
"""


class BinarySearch:
    def binary_search(self, arr: list, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    s = BinarySearch()
    arr = [2, 3, 5, 6, 7, 9, 10]
    print(s.binary_search(arr, 5))
    print(s.binary_search(arr, 6))
