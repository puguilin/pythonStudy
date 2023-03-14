# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:33
# @Author  : pgl
# @File    : 13_单列.py.py
# @IDE     : PyCharm


class Singleton:
    __obj = None
    __is_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = super().__new__(cls)
            return cls.__obj
        return cls.__obj

    def __init__(self, name):
        if Singleton.__is_init == False:
            print("第一初始化")
            self.name = name
            Singleton.__is_init = True


s1 = Singleton('张三')

print(s1)
print(s1.name)
s2 = Singleton('李四')
print(s2)
print(s2.name)
