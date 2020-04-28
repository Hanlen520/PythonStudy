# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_is_valid.py
@Time    : 2020-04-28  09:43:06
@Author  : indeyo_lin
"""
import pytest

from leetcode.is_valid import IsValid


class TestIsValid:
    def setup(self):
        self.s = IsValid()

    @pytest.mark.parametrize("s", [
        "()",
        "([])",
        "{}()[]",
        "{[()]}",
        "{}([{}])()[](()){{{((()))}}}",
        ""
    ])
    def test_success(self, s):
        assert self.s.isValid(s) is True
        assert self.s.easy_is_valid(s) is True

    @pytest.mark.parametrize("s", [
        "(}",
        "[(])",
        "{{))}}(",
        "}{}{",
        "(){([]})",
        "{",
        "]",
        "   ",
        "(("
    ])
    def test_fail(self, s):
        # assert self.s.isValid(s) is False
        assert self.s.easy_is_valid(s) is False
