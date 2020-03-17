#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : class&instance.py
@Time    : 2019-07-21  12:20:43
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

# class Student():
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def get_name(self):
#         print("name is : %s" % self.__name)
#
#     def get_score(self):
#         print("score is %d" % self.__score)

# stu = Student("Shelly", 99)
# stu.get_name()
# stu.get_score()
# stu.__name = "Lily"  # 在Student类中，__name是私有属性，不可直接被外部调用或赋值，这里相当于新增了一个属性__name
# stu.get_name()
# print(stu.__name)

# bart = Student()
# bart.name = "Lucy"
#
# print(bart.name)
# print(bart)
# print(Student)


"""
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
"""

# class Student():
#
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         if gender == 'male' or gender == 'female':
#             self.__gender = gender
#         else:
#             print("输入有误！")
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Timer(object):
#     def run(self):
#         print('Start...')
#
#
# time = Timer()
# time.run
# # print(dir(Animal))
# print(type(time))
# print(isinstance(time, Animal))
# print(isinstance(time, Timer))
# print(isinstance(time, object))

"""
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
"""

class Student():

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# stu1 = Student('Shelly')
# stu2 = Student('Josh')
# print(Student.count)

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')