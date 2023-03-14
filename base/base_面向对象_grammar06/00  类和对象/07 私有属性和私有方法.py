# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:56
# @Author  : pgl
# @File    : 07 私有属性和私有方法.py
# @IDE     : PyCharm


# 注意要点：
# （1）通常我们约定，两个下划线开头的属性是私有的。
# （2）类内部可以访问私有属性（方法），类外部不能直接访问私有属性（方法）
# （3）类外部可以通过“_类名__私有属性（方法）”访问私有属性（方法）
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Employee("小明", "20")
print(a.name)
print(a.age)


# 1. 如果对年龄进行私有的话会报错：

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


a = Employee("小明", "20")
print(a.name)


# print(a.age)  # 如果对年龄进行私有的话会报错


# 2. 如果想访问私有的话可以：
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __count(self):
        print("中国速度")


a = Employee("小明", "20")
print(a.name)
print(a._Employee__age)
a._Employee__count()  # 访问私有属性方法
