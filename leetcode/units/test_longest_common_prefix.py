# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_longest_common_prefix.py
@Time    : 2020-04-30  11:15:40
@Author  : indeyo_lin
"""
import pytest

from leetcode.longest_common_prefix import LongestCommonPrefix


class TestLongestCommonPrefix:
    def setup(self):
        self.pre = LongestCommonPrefix()

    @pytest.mark.parametrize("strs, prefix", [
        (["flower", "flow", "flight"], "fl"),
        (["flower", "flow", "flowing"], "flow"),
        (["apple", "aunt", "aproach", "app"], "a"),
        (["zoo", "zookeeper"], "zoo")
    ])
    def test_success(self, strs, prefix):
        assert self.pre.longestCommonPrefix(strs) == prefix

    @pytest.mark.parametrize("strs", [
        # 题目中没有说明1个字符串的情况
        ["gogogo"],
        ["dog", "racecar", "car"],
        []
    ])
    def test_fail(self, strs):
        assert self.pre.longestCommonPrefix(strs) == ""
