# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:44
# @Author  : pgl
# @File    : 19_打印错误信息.py.py
# @IDE     : PyCharm


# try:
#     num = int(input("请输入一个数字"))
#     reslut = 1 / num
#     print(reslut)
# except (ZeroDivisionError,ValueError) as e:
#     print(e)

try:
    num = int(input("请输入一个数字"))
    result = 1 / num
    print(result)
except Exception as e:
    print(e.__getattribute__())


