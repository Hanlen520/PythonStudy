# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : longest_common_prefix.py
@Time    : 2020-04-30  10:37:34
@Author  : indeyo_lin
"""
from typing import List


class LongestCommonPrefix:
    """
    14. 最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

    说明:
    所有输入只包含小写字母 a-z 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-common-prefix
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 获取最短字符串的长度，防止越界问题
        min_str_len = min([len(x) for x in strs])

        for ch_index in range(min_str_len):
            char = strs[0][ch_index]
            for string in strs:
                if char != string[ch_index]:
                    return strs[0][:ch_index]
        return strs[0][:min_str_len]


if __name__ == '__main__':
    # l = [x*x for x in range(5)]
    # print(l)
    # print(max(l))

    prefix = LongestCommonPrefix()
    print(prefix.longestCommonPrefix(["aa", "aa"]))
    print(prefix.longestCommonPrefix(["flower", "flow", "flowing"]))