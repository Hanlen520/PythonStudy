# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD16-sort.py
@Time    : 2019-06-28  12:37:55
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

# from time import time
#
# def select_sort(origin_items, comp=lambda x, y: x < y):
#     """简单选择排序"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items
#
#
# def bubble_sort(origin_items, comp=lambda x, y: x > y):
#     """高质量冒泡排序(搅拌排序)"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items
#
#
# start = time()
# print(select_sort([55,1,23,12,9,2,4,99,44,45,62,5,7,2,0,100]))
# end = time()
# print("Select_sort takes %.5fs." % (end - start))
#
# start = time()
# print(bubble_sort([55,1,23,12,9,2,4,99,44,45,62,5,7,2,0,100]))
# end = time()
# print("Bubble_sort takes %.5fs." % (end - start))

#
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)


"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

# collections模块下的工具类

"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))