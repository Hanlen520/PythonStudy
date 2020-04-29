# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_roman_to_int.py
@Time    : 2020-04-28  21:05:37
@Author  : indeyo_lin
"""
import pytest

from leetcode.roman_to_int import RomanToInt


class TestRomanToInt:
    def setup(self):
        self.s = RomanToInt()

    # 注意要是合法的罗马数字才行，要不然算出来一定会报错！
    @pytest.mark.parametrize("s, int_num", [
        ("I", 1),
        ("V", 5),
        ("VI", 6),
        ("IV", 4),
        ("III", 3),
        ("CXLII", 142),
        ("MCMXCIV", 1994),
        ("LVIII", 58)
    ])
    def test_success(self, s, int_num):
        assert self.s.romanToInt(s) == int_num
        assert self.s.roman_to_int2(s) == int_num
        assert self.s.roman_to_int3(s) == int_num
        assert self.s.roman_to_int4(s) == int_num