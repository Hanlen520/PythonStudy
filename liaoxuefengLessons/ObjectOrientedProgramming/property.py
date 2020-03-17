#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : property.py
@Time    : 2019-07-26  07:48:19
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

# class  Music():
#
#     def __init__(self, name, type):
#         self.name = name
#         self._type = type
#
#     @property
#     def name(self):
#         return self.name
#
#     @property
#     def type(self):
#         return self._type
#
#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise ValueError('name must be a string')
#         else:
#             self.name = name
#
# song = Music("That girl", "romatic")
# print(song.name)
# # song.name = 123
# # song.name = []
# song.name = "ME!"
# print(song.name)


# https://www.programiz.com/python-programming/property
# https://wiki.jikexueyuan.com/project/explore-python/Class/property.html
# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature   # 实例化对象的时候，没有用到限制条件，如果改成 self.temperature = temperature就可以
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value

# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value
#
#     temperature = property(get_temperature,set_temperature)
#
# c = Celsius(-22)
# print(c.__dict__)
# print(c.__doc__)
# print(c.__dir__())
# print(c.temperature)
# c.to_fahrenheit()
# c.temperature = 37
# print(c.temperature)
# print(c._temperature)


"""
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
"""
class Screen(object):

    # def __init__(self, width = 0, height = 0, resolution = 0):
    #     self.width = width
    #     self.height = height
    #     self.resolution = resolution

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be bigger than 0.")
        self._width  = width    # 如果改成self.width，会报错：Python: Maximum recursion depth exceeded

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be bigger than 0.")
        self._height  = height

    @property
    def resolution(self):
        return self._height * self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
# s.resolution = 11111  # 属性只读，报错AttributeError: can't set attribute
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')