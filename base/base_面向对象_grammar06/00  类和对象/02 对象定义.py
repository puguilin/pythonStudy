# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:39
# @Author  : pgl
# @File    : 02 对象定义.py
# @IDE     : PyCharm

#  对象是类的实例，只有定义了具体的对象，并通过“对象名.成员”的方式才能访问其中的数据成员或成员方法。语法如下：
# 对象名=类名（）

class Person:
    num = 1

    def SayHello(self):
        print("Good!")


a = Person()
a.SayHello()
