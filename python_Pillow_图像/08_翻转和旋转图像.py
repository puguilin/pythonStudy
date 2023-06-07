# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:36
# @Author  : pgl
# @File    : 08_翻转和旋转图像.py
# @IDE     : PyCharm


'''
 Image.FLIP_LEFT_RIGHT – 用于水平翻转图像
Image.FLIP_TOP_BOTTOM – 用于垂直翻转图像。
Image.ROTATE_90 – 通过指定的度数旋转图像。
'''

# 导入所需的图像模块
from PIL import Image

if __name__ == "__main__":

    # 打开一个已经存在的图像
    imageObject = Image.open("images/boy.jpg")
    # ============ 水平翻转=================
    # 做一个左右翻转的动作 (水平翻转)
    hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
    # 显示原始图像
    imageObject.show()
    # 显示水平翻转后的图像
    hori_flippedImage.show()

    # ================垂直翻转===============
    Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
    # 显示垂直翻转的图像
    Vert_flippedImage.show()

    # ===========将图像旋转到一个特定的程度===========
    degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
    # 显示90度翻转的图像
    degree_flippedImage.show()
