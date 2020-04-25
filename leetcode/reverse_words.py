# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : reverse_words.py
@Time    : 2020-04-24  15:46:24
@Author  : indeyo_lin
"""


class ReverseWords(object):
    """
    面试题58 - I. 翻转单词顺序
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

    示例 1：
    输入: "the sky is blue"
    输出: "blue is sky the"
    示例 2：
    输入: "  hello world!  "
    输出: "world! hello"
    解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    示例 3：
    输入: "a good   example"
    输出: "example good a"
    解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

    说明：
    无空格字符构成一个单词。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
    """

    # 注意：LeetCode上面的python版本比较老，不支持类型提示，记得去掉：str
    def reverse(self, s: str):
        """字符串内容全部翻转"""
        # 空字符串不处理
        if s == "":
            return ""

        array = list(s)
        begin = 0
        end = len(s) - 1
        temp = ""

        while begin <= end:
            temp = array[begin]
            array[begin] = array[end]
            array[end] = temp
            begin += 1
            end -= 1
        return "".join(array)

    # 提交的时候记得把函数名改成默认的那个，要不然LeetCode找不到函数会报错
    def reverse_words(self, s: str):
        """
        只翻转单词顺序，不翻转单词
        :type s: str
        :rtype: str
        """
        # 整个字符串翻转
        array = self.reverse(s).split(" ")
        # 把多余的空格去掉
        while "" in array:
            array.remove("")
        # print(array)
        point = 0

        # 每个单词翻转
        for item in array:
            array[point] = self.reverse(item)
            point += 1
        # print(array)
        return " ".join(array)


if __name__ == '__main__':
    # s = ReverseWords()
    # print(s.reverse("hello world."))
    # print(s.reverse_words("Today is a nice day."))

    array = ["1", "2", "3"]
    array.extend(["9","7"])
    # array.append([9,9,9])
    print(array)
    array.append("")
    print(array)
    # array.pop(7)
    array.sort(reverse=True)
    print(array)
