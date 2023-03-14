# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:45
# @Author  : pgl
# @File    : 04 实例属性和类属性.py
# @IDE     : PyCharm


# (1)实例属性
# 1、实例属性一般在__init__()方法中通过如下代码定义：
# self.实例属性名=初始值
# 2、在本类的其他实例方法中，也是通过self进行访问：
# self.实例属性名。
#
# (2)类属性
# 1、类属性是从属于“类对象”的属性，也成为“类变量”，由于，类属性从属于类对象，可以被所有实例对象共享。
# 2、类属性的定义方式：
#  clas 类名：
#       类变量名=初始值

class Student:
    num = 1  # 类属性

    def __init__(self, name, age):  # 构造函数
        self.n = name  # 实例属性
        self.a = age

    def print(self):  # 成员函数
        print("姓名：{}\n年龄：{}".format(self.n, self.a))

    def printnum(self):  # 成员函数
        print(Student.num)  # 由于是类属性，所以不写self.num


x = Student("小明", 20)
x.print()
Student.num = 2  # 修改类属性
x.printnum()
