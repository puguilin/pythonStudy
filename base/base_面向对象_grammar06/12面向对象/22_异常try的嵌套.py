# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:47
# @Author  : pgl
# @File    : 22_异常try的嵌套.py.py
# @IDE     : PyCharm


try:
    try:
        num = int(input("请输入一个数字"))
        result = 1 / num
        print(result)
    except ValueError:
        print("请输入数字")
except Exception as e:
    print(f"捕获到的错误为{e}")


