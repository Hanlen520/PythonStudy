# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_str_str.py
@Time    : 2020-04-30  21:11:47
@Author  : indeyo_lin
"""
import pytest

from leetcode.str_str import StrStr


class TestStrStr:
    def setup(self):
        self.s = StrStr()

    @pytest.mark.parametrize("haystack, needle, index", [
        ("hello", "ll", 2),
        ("hello", "he", 0),
        ("hello", "o", 4),
        ("hello", "hello", 0),
        ("hello", "", 0),
        ("", "", 0),
        ("mississippi", "issip", 4)
    ])
    def test_success(self, haystack, needle, index):
        assert self.s.strStr(haystack, needle) == index

    @pytest.mark.parametrize("haystack, needle", [
        ("aaaaa", "bba"),
        ("aaaaa", "aab"),
        ("aaaaa", "aaaaaa"),
        ("aaaaa", "bb"),
        ("", "a")
    ])
    def test_fail(self, haystack, needle):
        assert self.s.strStr(haystack, needle) == -1