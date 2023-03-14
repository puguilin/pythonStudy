# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:35
# @Author  : pgl
# @File    : 01 类定义.py
# @IDE     : PyCharm

# class 类名：
#       属性（成员变量）
#       属性
#       成员函数（成员方法）

class Person:
    num = 1

    def SayHello(self):
        print("Good!")

# 注意：类的成员函数必须有一个参数self且必须位于参数列表的开头。self就代表类的实例（对象）自身，可以使用self引用类的属性和成员函数。
