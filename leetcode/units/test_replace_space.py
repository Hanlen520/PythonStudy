# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_replace_space.py
@Time    : 2020-04-26  21:38:59
@Author  : indeyo_lin
"""
import pytest

from leetcode.replace_space import ReplaceSpace, SimpleReplaceSpace


class TestReplaceSpace:
    def setup(self):
        self.s = ReplaceSpace()
        self.s1 = SimpleReplaceSpace()

    @pytest.mark.parametrize("s", [
        "hello world",
        "We are happy.",
        "love&peace",
        " aeee e",
        " lalal gogo ye ",
        "a ye a b"
    ])
    def test_success(self, s):
        print(self.s.replaceSpace(s))
        print(self.s1.replaceSpace(s))

    @pytest.mark.parametrize("s", [
        " ",
        "",
        "   ",
        "1234 222"
    ])
    def test_fail(self, s):
        print(self.s.replaceSpace(s))
        print(self.s1.replaceSpace(s))