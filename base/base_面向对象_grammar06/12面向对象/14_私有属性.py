# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:36
# @Author  : pgl
# @File    : 14_私有属性.py.py
# @IDE     : PyCharm


# 定义一个对象
# 私有属性，在属性名或方法名前加两个下划线，
# 只能在当前类的内部使用，不能在类外部和子类中直接使用
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __eat(self):
        print(f'{self.__name}在吃饭')


class Dog(Animal):
    pass


pen = Animal('大黄', 22)
# pen._Animal__eat()
# print(pen._Animal__name)
# #当属性变为私有，外部不能进行访问
dog = Dog('二哈', 22)
dog._Animal__eat()
print(dir(Animal))
