# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : quick_sort.py
@Time    : 2020-05-04  10:22:40
@Author  : indeyo_lin
"""


class QuickSort:
    def quick_sort(self, arr: list, start, end):
        if start >= end:
            return arr
        pivot = self.partition(arr, start, end)

        self.quick_sort(arr, start, pivot - 1)
        self.quick_sort(arr, pivot + 1, end)

    def partition(self, arr, start, end):
        pivot, counter = end, start

        for i in range(start, end):
            if arr[i] < arr[pivot]:
                self.swap(arr, i, counter)
                counter += 1
        self.swap(arr, counter, pivot)
        return counter

    def swap(self, arr: list, index1, index2):
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp


if __name__ == '__main__':
    # for i in range(1, 5):
    #     print(i)
    arr = [5, 4, 9, 4, 7, 2, 8, 4]
    print(arr)
    s = QuickSort()
    s.quick_sort(arr, 0, 7)
    print(arr)