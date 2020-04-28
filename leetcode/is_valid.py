# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : is_valid.py
@Time    : 2020-04-28  09:35:17
@Author  : indeyo_lin
"""


class IsValid:
    """
    20. 有效的括号
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

        有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

        示例 1:
        输入: "()"
        输出: true
        示例 2:
        输入: "()[]{}"
        输出: true
        示例 3:
        输入: "(]"
        输出: false
        示例 4:
        输入: "([)]"
        输出: false
        示例 5:
        输入: "{[]}"
        输出: true
"""

    def isValid(self, s: str) -> bool:
        # list_str = list(s)
        # 用堆栈数据结构
        stack = []

        # 如果是奇数个字符,一定是无效的
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            # 右括号先出现的话，此时堆栈为空
            elif not stack:
                return False
            # 通过ASCII码的数值关系判断是不是一对
            elif i == ')' and ord(stack.pop()) + 1 != ord(i):
                return False
            elif i in ['}', ']'] and ord(stack.pop()) + 2 != ord(i):
                return False
        # 如果遍历完了，堆栈内还有数据，则无效
        if stack:
            return False
        return True

    def easy_is_valid(self, s):
        # 用字典保存对应关系，减少if-else判断
        dic = {'(': ')', '{': '}', '[': ']', '?': '?'}
        # 哨兵的作用是，防止右括号先出现的时候无法对栈进行pop操作，真是妙啊！
        stack = ['?']

        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    print(ord('('))
    print(ord(')'))

    print(ord('{'))
    print(ord('}'))

    print(ord('['))
    print(ord(']'))

    print(list("   "))
