#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : map&reduce.py
@Time    : 2019-07-11  08:40:54
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
练习题1
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
"""

# def normalize(name):
#     index = 1
#     new_name = ''
#     for x in name:
#         if index == 1:
#             new_name += x.upper()
#             index += 1
#         else:
#             new_name += x.lower()
#     return new_name

#网友答案
# def normalize(name):
#
#     return name[:][0].upper()+name[:][1:].lower()

#网友答案indeyo改造版
# def normalize(name):
#
#     return name[0].upper()+name[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


"""
练习2：
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：

"""
# from functools import reduce
#
# def prod(L):
#     def fn (x1, x2):
#         return x1 * x2
#     return reduce(fn, L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


"""
练习3：
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""

from functools import reduce


def str2float(s):

    def list2int(a, b):
        return a * 10 + b

    def list2float(a, b):
        return a * 0.1 + b

    def char2int(c):  #这里可以用int()代替
        digits = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[c]

    index = 0
    for x in list(s):  # 拿到小数点的位置
        if x != '.':
            index += 1
        else:
            break
    L1 = list(s)[:index]
    L2 = list(s)[:index:-1]
    return reduce(list2int, map(char2int, L1)) + reduce(list2float,  map(char2int, L2)) * 0.1


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')