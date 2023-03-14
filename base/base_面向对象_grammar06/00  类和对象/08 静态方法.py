# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 12:03
# @Author  : pgl
# @File    : 08 静态方法.py
# @IDE     : PyCharm


# 要点：
# 1、Python中允许定义与：类对象，无关的方法，称为“静态方法”。
# 2、”静态方法“和模块中定义普通函数没有区别，著不过"静态方法"放到了“类的名字空间里面”，xuyaotongguo“类调用”。
# 3、静态方法通过装饰器@staticmethod来定义，格式如下：

# @staticmethod
# def 静态方法名([形参列表])：
#       函数体
