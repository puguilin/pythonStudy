# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 16:28
# @Author  : pgl
# @File    : 14_在图像上写文字.py
# @IDE     : PyCharm

# 导入所需的图像模块
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    img = Image.open("images/boy.jpg")
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('arial.ttf', 40)
    d1.text((0, 0), "Sample PGL", font=myFont, fill=(255, 0, 0))
    img.show()
    img.save("images/image_text.jpg")
