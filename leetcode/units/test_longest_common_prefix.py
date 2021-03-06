# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_longest_common_prefix.py
@Time    : 2020-04-30  11:15:40
@Author  : indeyo_lin
"""
import pytest

from leetcode.longest_common_prefix import LongestCommonPrefix, Solution, LongestCommonPrefix1


class TestLongestCommonPrefix:
    def setup(self):
        self.pre = LongestCommonPrefix()
        self.pre1 = Solution()
        self.pre2 = LongestCommonPrefix1()

    @pytest.mark.parametrize("strs, prefix", [
        (["flower", "flow", "flight"], "fl"),
        (["flower", "flow", "flowing"], "flow"),
        (["apple", "aunt", "aproach", "app"], "a"),
        (["zoo", "zookeeper"], "zoo"),
        # 题目中没有说明1个字符串的情况
        (["gogogo"], "gogogo"),
        (["aa", "aa"], "aa"),
        (['ca', 'a'], '')
    ])
    def test_success(self, strs, prefix):
        # assert self.pre.longestCommonPrefix(strs) == prefix
        assert self.pre1.longestCommonPrefix(strs) == prefix
        assert self.pre2.longestCommonPrefix(strs) == prefix

    @pytest.mark.parametrize("strs", [
        ["dog", "racecar", "car"],
        ["yes", "yellow", "white"]
    ])
    def test_fail(self, strs):
        assert self.pre.longestCommonPrefix(strs) == ""
