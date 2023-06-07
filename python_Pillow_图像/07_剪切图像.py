# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:32
# @Author  : pgl
# @File    : 07_剪切图像.py
# @IDE     : PyCharm


# 导入所需的图像库
from PIL import Image, ImageFilter

if __name__ == "__main__":
    # 从一个图像中创建一个图像对象
    im = Image.open('images/boy.jpg')

    # 显示实际图像
    im.show()

    # left, upper, right, lowe
    # 裁剪
    cropped = im.crop((1, 2, 300, 300))

    # 显示裁剪后的部分
    cropped.show()

    # 保存裁剪后的图片
    cropped.save('images/croppedBeach1.jpg')
