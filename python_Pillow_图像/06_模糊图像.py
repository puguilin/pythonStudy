# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:14
# @Author  : pgl
# @File    : 06_模糊图像.py
# @IDE     : PyCharm

"""
模糊图像语法格式：
filter(ImageFilter.BLUR)
"""
# 导入所需的图像库
from PIL import Image, ImageFilter

if __name__ == "__main__":
    # =============== 简单模糊 =============

    # 打开现有图像
    OriImage = Image.open('images/boy.jpg')
    OriImage.show()

    blurImage = OriImage.filter(ImageFilter.BLUR)
    blurImage.show()
    blurImage.save('images/simBlurImage.jpg')
    print("简单模糊 simBlurImage.jpg")

    # =========== Python Pillow 盒式模糊 ==============
    '''
      Python Pillow 盒式模糊语法格式：
      
        ImageFilter.BoxBlur(radius)
        在这个过滤器中，我们使用 "半径 "作为参数。半径与模糊值成正比。
        Radius – 一个方向上的盒子的大小。
        Radius 0 – 表示没有模糊，并返回相同的图像。
        RRadius 1 &minnus; 在每个方向取1个像素，即总共9个像素。
    '''
    # 打开现有的图像
    OriImage = Image.open('images/boy.jpg')
    OriImage.show()

    # 应用盒式模糊过滤器
    boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
    boxImage.show()

    # 保存盒式模糊的图像
    boxImage.save('images/boxblur.jpg')
    print("盒式模糊 boxblur.jpg")

    # =============  高斯模糊 ===================
    '''
    高斯模糊 语法格式：
        ImageFilter.GaussianBlur(radius=2)
        这个滤镜也使用参数半径，与盒式模糊做同样的工作，只是在算法上有一些变化。简而言之，改变半径值，将产生不同强度的 "高斯模糊 "图像。
    '''

    # 打开现有图像
    OriImage = Image.open('images/boy.jpg')
    OriImage.show()

    # 应用高斯模糊滤波器
    gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
    gaussImage.show()

    # 保存高斯模糊的图像
    gaussImage.save('images/gaussian_blur.jpg')
    print("高斯模糊 gaussian_blur.jpg")
