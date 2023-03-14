# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:13
# @Author  : pgl
# @File    : 02_类的定义和方法的使用.py.py
# @IDE     : PyCharm


# 类的定义和使用
# 1.如何定义类
# 2.如何创建类的实例(也就是对象)
# 3.创建_init_()方法
# 4.创建类的成员并访问
# 5.访问限制

# 使用class创建类
# class ClassNanme:    # 大写字母开头的"驼峰式命名法"
#    '''类的帮助信息'''
#    statement

# 类的成员函数必须有一个参数self且必须位于参数列表的开头。self就代表类的实例（对象）自身，可以使用self引用类的属性和成员函数。


# 演示:
class Gess:
    '''这是大雁类'''  # 帮助信息的注释
    #  属性
    # 方法
    pass  # 还没想好做什么


# 定义类
class Pesron:
    # 类属性
    province = '北京'

    # 类的成员函数必须有一个参数self且必须位于参数列表的开头。self就代表类的实例（对象）自身，可以使用self引用类的属性和成员函数。
    # 初始化属性
    def __init__(self, name):
        self.name = name

    # 定义类方法
    # 使用装饰器@classmethod
    @classmethod
    def chang_province(cls, province):
        # cls是class的缩写
        cls.province = province


# 通过类名调用
Pesron.chang_province('湖北')
print(Pesron.province)

# 通过实例对象调用
student = Pesron('张三')
student.chang_province('四川')
print(student.province)

# 实例对象可以调用类方法
