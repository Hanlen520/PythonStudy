# -*- coding: utf-8 -*-
"""
@Project : StudyPython0-100
@File    : pyD15.py
@Time    : 2019-06-21  18:56:43
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from PIL import Image,ImageFilter

image = Image.open('./tlp.jpg')
print(image.format, image.size, image.mode)

# 裁剪图片
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# 上下旋转
# image.rotate(180).show()
# 左右翻转
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
# for x in range(200, 330):
#     for y in range(30, 200):
#         image.putpixel((x, y), (222,222,222))

# 滤镜效果
# 浮雕
# image.filter(ImageFilter.CONTOUR).show()
# 模糊
image.filter(ImageFilter.MaxFilter).show()


# image.show()
