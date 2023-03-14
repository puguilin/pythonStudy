# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:43
# @Author  : pgl
# @File    : 17_捕获多个异常.py.py
# @IDE     : PyCharm


# try:
#     num = int(input("请输入一个数字"))
#     reslut = 1 / num
#     print(reslut)
# except (ZeroDivisionError,ValueError):
#     print("输入的数字不合法")
try:
    num = int(input("请输入一个数字"))
    result = 1 /num
    print(result)
except ZeroDivisionError:
    print("输入的数字不能为零")
except ValueError:
    print("输入的不是数字")
