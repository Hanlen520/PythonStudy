# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : str_str.py
@Time    : 2020-04-30  21:11:19
@Author  : indeyo_lin
"""


class StrStr:
    """
    实现 strStr() 函数。
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
    如果不存在，则返回  -1。

    示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2
    示例 2:
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    说明:

    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/implement-strstr
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def strStr(self, haystack: str, needle: str) -> int:
        # 移动窗口法
        # 平均执行时间：40+ms
        # 这个办法最佳！时间最短且代码最短
        for start in range(len(haystack) - len(needle) + 1):
            if haystack[start:start + len(needle)] == needle:
                return start
        return -1

        # 思路二，OUT!
        # if len(haystack) < len(needle):
        #     return -1
        # h_index, n_index = 0, 0
        # flag_found = False
        #
        # # 不能用for，因为haystack的指针也要跟着移动
        # while h_index < len(haystack):
        #     for n_index in range(len(needle)):
        #         if haystack[h_index] == needle[n_index]:
        #             flag_found = True
        #             h_index += 1
        #             continue
        #         elif flag_found and haystack[h_index] != needle[n_index]:
        #             flag_found = False
        #         break
        #     if flag_found:
        #         break
        #     h_index += 1
        # return (h_index - len(needle)) if flag_found else -1

        # 思路一  OUT!!
        # for ch in needle:
        #     # 找到相同字符之前，如果字符不相同则继续内循环，如果相同则退出内循环
        #     while ch != haystack[index] and not flag_found:
        #         index += 1
        #         if index == len(haystack):
        #             return -1
        #     flag_found = True
        #     # 找到相同字符后，如果字符不同，清空重新来
        #     if ch != haystack[index] and flag_found:
        #         flag_found = False
        #     index += 1
        # return index - len(needle)

    def strStr_2(self, haystack: str, needle: str) -> int:
        # 双指针法（回溯法）
        # 平均执行时间：50+ms
        # 多了回溯的思想，解决我之前方案的难题，但效率没有滑动窗口的高。
        # 就当做打开一种新思路吧
        p_hay, p_nee = 0, 0
        len_hay = len(haystack)
        len_nee = len(needle)
        # 是否出现相同字符
        flag = False

        while p_hay < len_hay:
            # 如果needle已经遍历完，直接返回，防止溢出
            if p_nee == len_nee:
                return p_hay-len_nee
            if not flag and haystack[p_hay] != needle[p_nee]:
                p_hay += 1
                continue
            if haystack[p_hay] == needle[p_nee]:
                p_hay += 1
                p_nee += 1
                flag = True
            else:
                # 回溯
                p_hay = p_hay - p_nee + 1
                # 遇到不相同字符，重置 p_nee 和 flag
                p_nee = 0
                flag = False
        return (p_hay-len_nee) if p_nee == len_nee else -1


if __name__ == '__main__':
    a = 0
    b = 0
