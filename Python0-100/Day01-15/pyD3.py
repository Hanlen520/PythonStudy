#-*- coding: utf-8 -*-
"""
@Project : private-document
@File    : pyD3.py
@Time    : 2019-05-14  21:56:57
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

"""
练习1：
英制单位英寸和公制单位厘米互换
"""
# choice = int(input('英寸转换成厘米请输入1，厘米转换成英寸请输入0，输入其他无效：'))
# if choice == 1:
#     inches_num = float(input('请输入要转换的数：'))
#     trans_num = 2.54 * inches_num
#     print('%f英寸 = %f厘米' % (inches_num, trans_num))
# elif choice == 0:
#     centimeter_num = float(input('请输入要转换的数：'))
#     trans_num = centimeter_num * 2.54
#     print ('%f厘米 = %f英寸' % (centimeter_num, trans_num))
# else:
#     pass

#参考答案
# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')


# from random import randint
#
# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '念绕口令'
# else:
#     result = '讲冷笑话'
# print(result)

# import getpass
# username = input('请输入用户名: ')
# # password = input('请输入口令: ')
# # 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# password = getpass.getpass('请输入口令: ')
# if username == 'admin' and password == '123456':
#     print('身份验证成功!')
# else:
#     print('身份验证失败!')

"""
练习4：输入三条边长如果能构成三角形就计算周长和面积
"""

# a = float(input('请输入第一条边：'))
# b = float(input('请输入第二条边：'))
# c = float(input('请输入第三条边：'))
# if (a + b > c) & (a + c > b) & (b + c > a):
#     p = (a + b + c) / 2
#     print('周长 = %.2f\n面积 = %.2f' % (a + b + c, (p * (p - a) * (p - b) * (p - c)) ** 0.5))


# import math
#
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     print('周长: %f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print('面积: %f' % (area))
# else:
#     print('不能构成三角形')


"""
练习5：输入月收入和五险一金计算个人所得税
"""
#标准答案
salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))