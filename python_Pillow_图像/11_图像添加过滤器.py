# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 16:05
# @Author  : pgl
# @File    : 11_图像添加过滤器.py
# @IDE     : PyCharm

# 导入所需的图像模块
from PIL import Image, ImageFilter

if __name__ == "__main__":
    # 从图像中创建一个图像对象
    im = Image.open("images/dh.jpg")
    from PIL.ImageFilter import (
        BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
        EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
    )

    # Create image object
    img = Image.open('images/cat.jpg')
    # Applying the blur filter
    img1 = img.filter(CONTOUR)
    img1.save('images/ImageFilter_blur.jpg')
    img1.show()
