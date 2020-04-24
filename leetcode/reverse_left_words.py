# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : reverse_left_words.py
@Time    : 2020-04-23  14:36:02
@Author  : indeyo_lin
"""


def reverse_left_words(s: str, n):
    """
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
    比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

    示例 1：
    输入: s = "abcdefg", k = 2
    输出: "cdefgab"

    示例 2：
    输入: s = "lrloseumgh", k = 6
    输出: "umghlrlose"
     
    限制：
    1 <= k < s.length <= 10000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    :param s:
    :param n:
    :return:
    """
    # done:入参类型和长度校验
    try:
        if n < 1:
            raise ValueError("%s is less than 1" % n)
        if len(s) > 10000:
            # done：如果长度超了是不是要抛异常？
            # 对，可以自己raise
            raise ValueError("the length of %s is over 10000" % s)
        list_of_str = list(s)
        for i in range(n):
            list_of_str.append(list_of_str.pop(0))
        return ''.join((list_of_str))
    # done:try语句里面python会自己抛异常，那么自己写异常处理的意义在哪里？
    # 自己写异常处理的意义在于，自己可以把异常处理掉，或者属于业务行为的异常。如果这个异常无法处理，则不需要捕获。
    except TypeError as e:
        if not isinstance(s, str):
            print(s, "is not str")
            raise e
        if not isinstance(n, int):
            print(n, "is not int")
            raise e
    except ValueError as e:
        raise e


if __name__ == '__main__':
    print(reverse_left_words('abcdefg', 2))
    print(reverse_left_words('lrloseumgh', 6))

    # L = [1,2,3,4]
    # print(L)
    # L.append(5)
    # print(L)
    # for i in range(3):
    #     L.append(L.pop(0))
    # print(L)
    #
    # s = "1234"
    # print(''.join(list(s)))