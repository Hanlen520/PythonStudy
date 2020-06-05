# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Author : indeyo_lin 
# @Time : 2020/6/5 5:00 下午 
# @File : LRUCache.py 
"""


class LRUCache:
    def __init__(self, size):
        # 字典列表，每次insert(0, 新元素)，头部是最新的元素，尾部是最老的元素，pop出去
        self.list: [dict] = []
        self.size = size

    def put(self, key, value):
        self.list.insert(0, {key: value})
        if len(self.list) > self.size:
            self.list.pop()
        print(self.list)

    def get(self, key):
        target, p = None, 0
        # 获取目标对象的下标和元素值
        for index, item in enumerate(self.list):
            if key in item.keys():
                target, p = item, index
                break

        print(target, p)
        # 找不到返回-1
        if not target:
            return -1

        # 如果被查看的元素在第一位，则不需要挪动
        if p != 0:
            # 元素全体往后挪一位
            self.list[1:p+1] = self.list[:p]
            # 最新访问元素放在第一位
            self.list[0] = target
        print(self.list)
        return target[key]


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, "1")
    lru.put(2, "2")
    lru.put(3, "3")
    lru.put(4, "4")
    lru.get(3)
    lru.get(2)
