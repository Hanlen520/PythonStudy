# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : replace_space.py
@Time    : 2020-04-26  14:47:16
@Author  : arthinking
"""


class ReplaceSpace:
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = list(s)
        array_new = []
        new_index = 0

        for i in array:
            if i == ' ':
                array_new[new_index:new_index+2] = "%20"
                new_index += 3
            else:
                array_new.insert(new_index, i)
                new_index += 1
        return "".join(array_new)


if __name__ == '__main__':
    s = ReplaceSpace()
    print(s.replaceSpace(" aeee e"))

