# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 16:13
# @Author  : pgl
# @File    : 12_图像颜色.py
# @IDE     : PyCharm

'''

    格式：
    PIL.ImageColor.getrgb(color)
    参数： color – 一个颜色字符串
    返回值：(红、绿、蓝[, alpha])
'''

# 导入所需的图像模块
from PIL import Image, ImageColor

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    im = Image.open("images/dh.jpg")
    # 创建新图像并获得RGB颜色元组。
    img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))

    # 显示图像
    im.show()
    img.show()
