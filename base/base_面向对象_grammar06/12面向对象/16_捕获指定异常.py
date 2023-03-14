# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:42
# @Author  : pgl
# @File    : 16_捕获指定异常.py.py
# @IDE     : PyCharm


""""
语法
try:
   运行代码
except 错误类型
"""
try:
    1/0
except ZeroDivisionError:
    print("除数不能为零")


try:
    print(name)
except NameError:

    print("没有声明变量的错误")

