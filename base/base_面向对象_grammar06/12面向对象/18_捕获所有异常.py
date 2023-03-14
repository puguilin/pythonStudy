# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:43
# @Author  : pgl
# @File    : 18_捕获所有异常.py.py
# @IDE     : PyCharm

# try:
#     num = int(input("请输入一个数字"))
#     result = 1 / num
#     print(result)
# except Exception as e:
#     print(e)
try:
    num = int(input("请输入一个数字"))
    result = 1 / num
    print(result)
except:
    print("错误")

