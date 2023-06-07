# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved
#
# @Time    : 2023/6/7 14:28
# @Author  : pgl
# @File    : 02_Pillow Image模块的属性.py
# @IDE     : PyCharm


"""
 格式： Image.open(fp, mode='r')
    fp – 一个文件名(字符串)、pathlib.Path对象或一个文件对象。文件对象必须实现read()、seek()和tell()方法，并且是以二进制模式打开。
    mode – 这是一个可选的参数，如果给出，必须是’r’。
    返回值 – 一个图像对象。
    错误 – 如果找不到文件，或者图像不能被打开和识别。
"""

from PIL import Image
if __name__ == "__main__":


    # 将打开一个任何格式的图像（我们使用的是.jpg），在一个窗口中显示它，然后用另一种文件格式（.bmp）保存它（默认位置）
    # 读取图片
    image = Image.open('./images/1.jpg')
    image.show()
    # 保存图片 你也可以明确地指定文件类型作为第二个参数 –
    image.save('./images/2.bmp', 'bmp')
    image1 = Image.open('./images/2.bmp')
    # 显示保存后的图片
    image1.show()

