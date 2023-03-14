#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved
#
# @Time    : 2023/02/12 0:41
# @Author  : pgl
# @File    : 02_代码缩进.py
# @IDE     : PyCharm
# 代码缩进

""""
代码缩进: 是指在每一行代码左端空出一定长度的空白, 从而可以更加清晰地从外观上看出程序的逻辑结构
1.一个Tab或者4个空格, 推荐使用空格
2.同一个级别的代码块的缩进量必须相同. 如果不采用合理的代码缩进, 将抛出SyntaxError异常.
    if bim<18.5:
        print("您的体重过轻 ~@_@~")
          print("同学您的BIM指数为:" + str(bim)) #上面缩进4个空格, 下面缩进6个空格就会报错, 同一个级别的代码块的缩进量必须相同
"""

print("正常语句")
num = 2
if num < 0:
    # 注意前面有四个空格， 后面的就是代码块，可以有多条
    print("num < 0")
    print(num < 0)
if num > 0:
    print("num > 0")
    print(num > 0)
