# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : roman_to_int.py
@Time    : 2020-04-28  16:22:06
@Author  : indeyo_lin
"""


class RomanToInt:
    """
    13. 罗马数字转整数
        罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

        示例 1:
        输入: "III"
        输出: 3
        示例 2:
        输入: "IV"
        输出: 4
        示例 3:
        输入: "IX"
        输出: 9
        示例 4:
        输入: "LVIII"
        输出: 58
        解释: L = 50, V= 5, III = 3.
        示例 5:
        输入: "MCMXCIV"
        输出: 1994
        解释: M = 1000, CM = 900, XC = 90, IV = 4.
    """

    def romanToInt(self, s: str) -> int:
        """
        解法一：
            罗马数字所有组合用字典保存，从字符串第一位扫描
            如果是组合，就取组合值并减去前一位的值，
            如果不是组合，加上当前值
            平均实行时间：70+ms
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        l_str = list(s)
        p, roman_int = 0, 0

        while p < len(l_str):
            if p == 0:
                roman_int = roman[l_str[p]]
            elif "".join(l_str[p - 1:p + 1]) in roman:
                # 如果可以和前一位组成一对，则减去前一位的值
                roman_int += roman["".join(l_str[p - 1:p + 1])] - roman[l_str[p - 1]]
            else:
                roman_int += roman[l_str[p]]
            p += 1
        return roman_int

    def roman_to_int2(self, s):
        """
        解法二：
            和解法一不同的是，字典不一样，不包含双字符罗马数字。
            和前一位比较大小，判断当前位用加法还是减法
            这个算法稍微比解法一快一点，平均执行时间：60+ms
            缺点是代码可读性不强
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        l_str = list(s)
        p, roman_int = 0, 0

        while p < len(s):
            if p == 0 or roman[l_str[p]] <= roman[l_str[p - 1]]:
                roman_int += roman[l_str[p]]
            else:
                roman_int = roman_int + roman[l_str[p]] - roman[l_str[p - 1]] * 2
            p += 1
        return roman_int

    def roman_to_int3(self, s:str):
        """
        解法三：
            字典存储的是单字符，从字符串第二位开始扫描，只对前一个字符进行加减法。
            如果前一位小于当前值，则对前一位做减法
            如果前一位大于等于当前值，则对前一位做加法
            该算法比前面两种都快一点，平均执行时间50+ms
        :param s:
        :return:
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        l_str = list(s)
        # 从第二位开始遍历
        p, roman_int = 1, 0
        # 对pre_val做处理，可以节省掉很多raman[]的写法，代码更优雅
        pre_val = roman[l_str[0]]

        while p < len(s):
            # 当前值小于等于前一位，加法
            if roman[l_str[p]] <= pre_val:
                roman_int += pre_val
            else:
                # 当前值大于前一位，减法
                roman_int -= pre_val
            pre_val = roman[l_str[p]]
            p += 1
        # 注意最后一位要加上，别忘了
        roman_int += pre_val
        return roman_int


if __name__ == '__main__':
    s = "12345"
    print(s.find('2'))
    print(s.index('3'))

    s = RomanToInt()
    print(s.roman_to_int3("CXLII"))
