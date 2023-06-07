# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 14:28
# @Author  : pgl
# @File    : 02_Pillow Image模块的属性.py
# @IDE     : PyCharm

from PIL import Image

if __name__ == "__main__":
    image = Image.open('images/1.jpg')
    # image.filename 获取图像名或路径
    print("获取图像名或路径：" + image.filename)
    # Image.format 返回图像文件的文件格式，如’JPEG’、’BMP’、’PNG’等
    print("返回图像的格式：" + image.format)
    # Image.mode 用于获取图像所使用的像素格式。典型的值是 "1"、"L"、"RGB "或 "CMYK"
    print("获取图像所使用的像素格式：" + image.mode)
    # Image.size 返回由图像的高度和重量组成的元组。
    print("返回由图像的高度和重量组成的元组：" + str(image.size))
    # Image.width 返回图像的宽度
    print("返回图像的宽度：" + str(image.width))
    # Image.height 返回图像的高度
    print("返回图像的高度：" + str(image.height))
    # Image.info 返回一个持有与图像相关的数据的字典
    print("返回一个持有与图像相关的数据的字典：" + str(image.info))
    # Image.palette 返回调色板表，如果有的话
    print("返回调色板表，如果有的话：" + str(image.palette))

