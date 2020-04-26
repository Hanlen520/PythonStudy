# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_reverse_left_words.py
@Time    : 2020-04-23  16:33:07
@Author  : indeyo_lin
"""
import pytest

from leetcode.reverse_left_words import reverse_left_words, Solution


class TestReverseLeftWords:
    def setup(self):
        self.s = Solution()

    @pytest.mark.parametrize("s, n", {
        ("abcdefg", 2),
        ("rloseumghl", 6)
    })
    def test_success(self, s, n):
        print(reverse_left_words(s, n))

    @pytest.mark.parametrize("s, n", [
        (1234, 2),
        ("12sdfsf", "123"),
        ("JJDJFJ", 0)
    ])
    def test_type(self, s, n):
        print(reverse_left_words(s, n))

    @pytest.mark.parametrize("s, n", {
        ("abcdefg", 2),
        ("rloseumghl", 6)
    })
    def test_success(self, s, n):
        print(self.s.reverseLeftWords(s, n))

    @pytest.mark.parametrize("s, n", [
        (1234, 2),
        ("12sdfsf", "123"),
        ("JJDJFJ", 0)
    ])
    def test_type(self, s, n):
        print(self.s.reverseLeftWords(s, n))
