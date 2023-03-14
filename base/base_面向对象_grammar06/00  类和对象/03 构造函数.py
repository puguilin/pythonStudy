# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:41
# @Author  : pgl
# @File    : 03 构造函数.py
# @IDE     : PyCharm

# 1）__ init__()方法的要点：
# 1）名称必须固定，即要以两个下划线“_”开头和结束。
#
# 2）第一个参数固定，必须为：self。self指的就是刚刚创建好的实例对象。
#
# 3）一个类定义了__init__()方法以后，类实例化时就会自动为新生的类实例调用__init__()方法。
#
# 4）构造函数一般用于完成对象数据成员设置初值或进行其他必要的初始化工作，如果用户未涉及构造函数，Python将提供一个默认的构造函数。

class Student:
    def __init__(self, name, age):
        self.n = name
        self.a = age


x = Student("小明", 20)
print(x.n)
print(x.a)
