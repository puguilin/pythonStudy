# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 14:20
# @Author  : pgl
# @File    : 01_使用Image模块.py
# @IDE     : PyCharm


from PIL import Image

# 使用Image模块打开图像
im = Image.open("images/1.jpg")
# 显示实际的图像
im.show()
# 显示旋转的图像
im = im.rotate(45)
im.show()
