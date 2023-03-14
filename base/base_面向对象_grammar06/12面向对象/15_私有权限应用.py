# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:40
# @Author  : pgl
# @File    : 15_私有权限应用.py.py
# @IDE     : PyCharm


# 定义类
class Person:
    # 初始化属性
    def __init__(self, name):
        self.name = name
        self.__age = 0

    # 定义设置age方法
    def set_age(self, age):
        if age > 150 or age < 18:
            print("当前年龄不合法")
        else:
            self.__age = age

    # 定义获取age方法
    def get_age(self):
        return self.__age


# 对象实例化
person = Person('小三')
person.set_age(22)
print(person.get_age())
# 通过对象._类名__属性
print(person._Person__age)
