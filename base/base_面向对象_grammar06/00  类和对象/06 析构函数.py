# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:43
# @Author  : pgl
# @File    : 06 析构函数.py
# @IDE     : PyCharm

# Python中类的析构函数是__del__,用来释放对象占用的资源。
# 注意：在删除x对象变量之前，x是存在的，在内存中的标识为0x03348C10，执行del x语句后，x对象变量不存在了，系统自动调用析构函数，所以出现“不存在了”。

class Student:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def __del__(self):
        print("不存在了")


x = Student("小明", 20)
print(x.n)
print(x.a)
print(x)
del x
