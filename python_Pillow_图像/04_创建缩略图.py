# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/6/7 14:58
# @Author  : pgl
# @File    : 04_创建缩略图.py
# @IDE     : PyCharm


from PIL import Image


'''
创建缩略图 语法：
Image.thumbnail(size, resample=3)
'''

if __name__ == "__main__":

    def tnails():
        try:
            image = Image.open('images/3.jpg')
            image.thumbnail((90, 90))
            image.save('images/3thumbnail.jpg')
            image1 = Image.open('images/3thumbnail.jpg')
            image1.show()
        except IOError:
            pass


    tnails()
