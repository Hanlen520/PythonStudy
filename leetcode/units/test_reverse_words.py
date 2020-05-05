# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_reverse_words.py
@Time    : 2020-04-25  11:07:39
@Author  : indeyo_lin
"""
import pytest

from leetcode.reverse_words import ReverseWords


class TestReverseWords:
    def setup(self):
        self.reverse = ReverseWords()

    @pytest.mark.parametrize("str1,str2", [
        ("the sky is blue", "blue is sky the"),
        ("  hello world!  ", "world! hello"),
        ("a good   example", "example good a")
    ])
    def test_success(self, str1, str2):
        assert self.reverse.reverse_words(str1) == str2
        assert self.reverse.reverse_words2(str1) == str2

    @pytest.mark.parametrize("str1", [
        " ",
        "1234 55555"
    ])
    def test_fail(self, str1):
        print(self.reverse.reverse_words(str1))
        print(self.reverse.reverse_words2(str1))
