# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 15:04
# @Author  : pgl
# @File    : 05_粘贴合并图像.py
# @IDE     : PyCharm

"""
粘贴图像格式：
Image.merge(mode, bands)

    mode – 输出图像要使用的模式。
    bands – 一个序列，包含输出图像中每个波段的一个单波段图像。所有波段必须有相同的大小。
    返回值 – 一个图像对象。
    使用merge()函数，你可以将一个图像的RGB波段合并为——。



Python Pillow合并两个图像
    使用open()函数为所需图像创建图像对象。
    在合并两张图片时，你需要确保两张图片的尺寸是相同的。因此，获取两张图片的每个尺寸，如果需要，相应地调整它们的尺寸。
    使用Image.new()函数创建一个空图像。
    使用paste()函数粘贴图像。
    使用save()和show()函数来保存和显示结果的图像。

"""

from PIL import Image

if __name__ == "__main__":
    # 粘贴图像
    image = Image.open("images/1.jpg")
    r, g, b = image.split()
    image.show()
    # 在执行上述代码时，你可以看到原始图像和合并了RGB带的图像，如下图所示
    image = Image.merge("RGB", (b, g, r))
    image.show()

    # 合并图像
    from PIL import Image

    # 读取两张图片
    image1 = Image.open('images/1.jpg')
    # image1.show()
    image2 = Image.open('images/3.jpg')
    # image2.show()
    # 调整大小，第一个图像
    image1 = image1.resize((426, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (2 * image1_size[0], image1_size[1]), (250, 250, 250))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1_size[0], 0))
    # 合并之后的图像
    new_image.save("images/merged_image.jpg", "JPEG")
    new_image.show()
