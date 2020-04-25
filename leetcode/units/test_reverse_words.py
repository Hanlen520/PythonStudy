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

    @pytest.mark.parametrize("str1", [
        "the sky is blue",
        "  hello world!  ",
        "a good   example"
    ])
    def test_success(self, str1):
        print(self.reverse.reverse_words(str1))

    @pytest.mark.parametrize("str1", [
        " ",
        "1234 55555"
    ])
    def test_fail(self, str1):
        print(self.reverse.reverse_words(str1))
