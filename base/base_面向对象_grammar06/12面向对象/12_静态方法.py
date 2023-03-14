# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:32
# @Author  : pgl
# @File    : 12_静态方法.py.py
# @IDE     : PyCharm


# 静态方法

class Person:
    sex = None

    def __init__(self):
        pass

    # 静态方法通过@staticmethod
    # 与类无关的方法，但需要通过类调用
    @staticmethod
    def rule():
        print("人们都要遵守规则")


# 静态方法和模块中定义普通函数没有什么区别，只不过静态方法放到类的名字里面，需要通过类调用
# 通过类名.方法调用
Person.rule()
print('----' * 20)
# 通过对象调用
# 实例化
person = Person()
person.rule()
