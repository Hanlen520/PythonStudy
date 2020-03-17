# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD13.py
@Time    : 2019-06-19  12:09:06
@Author  : indeyo_lin
@Version : 
@Remark  : 进程与线程
"""

# from threading import Thread
# from time import time, sleep
# from random import randint
# 
# class downloadFile(Thread):
# 
#     def __init__(self, filename):
#         super().__init__()
#         self.filename = filename
# 
#     def download(self):
#         print("Begin to download %s ..." % self.filename)
#         download_time = randint(0, 5)
#         sleep(download_time)
#         print("It takes %s seconds to download %s ." % (download_time, self.filename))
# 
# def main():
#     
#     #多线程无法实现并发
#     
#     start = time()
#     t1 = downloadFile("Tatanic.mp4")
#     t1.start()
#     t2 = downloadFile("Begin Again.mp4")
#     t2.start()
#     t1.download()
#     t2.download()
#     t1.join()
#     t2.join()
#     end = time()
#     print("Finally it takes %.2f seconds to download." % (end - start))

from multiprocessing import Process
from random import randint
from time import time,sleep
from os import getpid

def downloadFileInProcess(filename):
    print("The process id is [%d]" % getpid())
    download_time = randint(0,5)
    sleep(download_time)
    print("It takes %ds to download %s" % (download_time, filename))

def main():
    start = time()
    print("The main process id is [%d]" % getpid())
    p1 = Process(target=downloadFileInProcess, args=('Flipped.avi',))
    p1.start()
    p2 = Process(target=downloadFileInProcess, args=('working.jpg',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("It takes %.2f to download these two files" % (end - start))

    
if __name__ == '__main__':
    main()