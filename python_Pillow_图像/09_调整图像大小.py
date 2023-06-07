# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:47
# @Author  : pgl
# @File    : 09_调整图像大小.py
# @IDE     : PyCharm


# 导入所需的图像模块
from PIL import Image

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    im = Image.open("images/boy.jpg")

    # 显示实际图像
    im.show()
    # 使新图像的宽度和高度分别为原图像的一半
    resized_im = im.resize((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # 显示调整后的图像
    resized_im.show()
    # 保存裁剪后的图片
    resized_im.save('images/resizedBeach1.jpg')
