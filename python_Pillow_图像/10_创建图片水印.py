# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:50
# @Author  : pgl
# @File    : 10_创建图片水印.py
# @IDE     : PyCharm

'''

    为了给我们的图片添加水印，我们需要Pillow包中的"Image "、"ImageDraw "和"ImageFont "模块。
'''

# 导入所需的图像模块
from PIL import Image, ImageDraw, ImageFont

import warnings
# 去除 DeprecationWarning等类似警告：
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    im = Image.open("images/boy.jpg")
    width, height = im.size
    draw = ImageDraw.Draw(im)
    # 水印信息
    text = "pgl_pgl"

    # 所需字体 和 字体大小
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # 水印显示的地方
    draw.text((x, y), text, font=font)
    im.show()
    im.save('images/pgl_pgl.jpg')
