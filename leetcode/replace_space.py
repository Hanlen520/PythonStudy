# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : replace_space.py
@Time    : 2020-04-26  14:47:16
@Author  : indeyo_lin
"""


class ReplaceSpace:
    """
        面试题05. 替换空格
        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

        示例 1：
        输入：s = "We are happy."
        输出："We%20are%20happy."

        限制：0 <= s 的长度 <= 10000
    """

    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 转换成列表，方便对每个字符进行操作
        array = list(s)
        # python里面数组的赋值操作，实际上相当于引用，而没有开辟一个新的存储空间
        # 如果不copy，直接赋值，那么对array_new进行修改会影响到array
        array_new = array.copy()
        # 代表当前空格后面的字符串收尾指针
        p_head, p_tail = 0, len(array) - 1
        # 原字符串扫描指针
        p_search = 0

        for i in array:
            if i == ' ':
                # 这种切片赋值法有一种情况不能实现，不能默认输入空字符，赋值后list后面都是有值的
                # 当结尾是一个空格加一个字符的时候，最后一个字符会丢失
                last = array[p_search + 1:len(array)]
                if len(last) < 2:
                    array_new.append("")
                    array_new[p_head + 3:p_tail + 3] = last
                else:
                    array_new[p_head + 3:p_tail + 3] = array[p_search + 1:len(array)]
                array_new[p_head:p_head + 3] = "%20"
                p_head += 3
                p_tail += 3
                p_search += 1
                continue
            p_head += 1
            p_search += 1
        return "".join(array_new)


class SimpleReplaceSpace:
    def replaceSpace(self, s):
        origin = list(s)
        new = []
        for i in origin:
            if i == " ":
                new.append("%20")
            else:
                new.append(i)
        return "".join(new)


class LessSpaceReplaceSpace:
    def replaceSpace(self, s):
        array = list(s)
        length = len(array)
        p, blank_num = 0, 0

        while p < length:
            if array[p] == " ":
                blank_num += 1
                array.append('x')
                array.append('x')
            p += 1

        p_orgin_tail = length - 1
        p_new_tail = length - 1 + 2 * blank_num

        while p_orgin_tail >= 0:
            if array[p_orgin_tail] == " ":
                # python不支持给空的list用切片赋值
                array[p_new_tail-2:p_new_tail+1] = ["%", "2", "0"]
                # array.insert(p_new_tail-2, "%20")
                p_new_tail -= 3
            else:
                array[p_new_tail] = array[p_orgin_tail]
                p_new_tail -= 1
            p_orgin_tail -= 1
        return "".join(array)

if __name__ == '__main__':
    # a = [1, 2, 3, 4, 5, 6, 7, 8]
    # b = ['l', 'o', 'v', 'e']
    # 实际上赋值给a[8]
    # a[10:11] = b[1:2]
    # print(a)
    # print(a[:-5:2])
    # a[1:3] = [9, 9]
    # print(a)
    # b[2:4] = "abc"
    # print(b)
    #
    # for i in range(5):
    #     print(i)
    # print(a.index(3))

    s = ReplaceSpace()
    print(s.replaceSpace(" aeee e"))
    s1 = SimpleReplaceSpace()
    print(s1.replaceSpace(" aeee e"))
    s2 = LessSpaceReplaceSpace()
    print(s2.replaceSpace(" aeee e"))

    # a = []
    # q = queue.Queue()
    # q.put(a)
    # q.put(0)
    # # print(q.get())
    # print(q.get())
