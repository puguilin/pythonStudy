# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 16:19
# @Author  : pgl
# @File    : 13_ImageDraw模块.py
# @IDE     : PyCharm

'''
       一个图像可以被很好地理解为一个二维的像素（图片元素）阵列。一个像素是被支持的最小的颜色点。
    ImageDraw使用的二维坐标系的原点在图像的左上角。
   我们使用的枕头颜色方案是RGB。RGB颜色的表示和支持是由模块ImageColor提供的。
   bitmap、OpenType或TrueType是可接受的用于文本注释的字体。
   大多数绘图命令可能需要一个边界框参数，以指定该命令要应用的图像上的区域。
  一个坐标序列可以表示为[ (x0, y0), (x1, y1), … (xn, yn)]。
  对于某些绘图命令，我们需要角度值。
'''

# 导入所需的图像模块
from PIL import Image, ImageDraw,ImageFont

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    im = Image.open("images/cat.jpg")

    # 画线
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # 显示图像
    im.show()

    # ====================在给定的图像上绘制文本 =======================

    # 获得一个图像
    base = Image.open('images/boy.jpg').convert('RGBA')

    # 为文本制作一个空白图像，初始化为透明的文本颜色
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    # 获得一种字体
    fnt = ImageFont.truetype('arial.ttf', 40)
    # 获得一个绘图环境
    d = ImageDraw.Draw(txt)
    # 绘制文本，一半不透明
    d.text((14, 14), "PGLPGL", font=fnt, fill=(255, 255, 255, 128))

    # 绘制文本，完全不透明
    d.text((14, 60), "Point", font=fnt, fill=(255, 255, 255))
    out = Image.alpha_composite(base, txt)

    # 显示图像
    out.show()





