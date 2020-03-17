#-*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD11.py
@Time    : 2019-06-05  21:42:19
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

def ReadFile(file_route):
    try:
        with open(file_route, "r", encoding = "utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Could't open the file")
    except UnicodeError:
        print("Something is wrong in decoding")

def WriteFile(file_route, str):
    try:
        with open(file_route, "a+", encoding = "utf-8") as f: # 奇怪，a+ 和 r+ 都不支持同时读写，a+只支持写不支持读，r+只支持读不支持写
            f.write(str)
            print(f.read())
    except FileNotFoundError:
        print("FileNotFound")
    except IOError as e:
        print(e)
        print("Writing Failed!")

# ReadFile("D:\interview\private-document\StudyPython0-100\StarryStarryNight.txt")
# ReadFile("../StarryStarryNight.txt")
# ReadFile("")

WriteFile("../StarryStarryNight.txt", " " + '\n')
# ReadFile("../StarryStarryNight.txt")