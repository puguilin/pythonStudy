# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:27
# @Author  : pgl
# @File    : 01__new__方法.py.py
# @IDE     : PyCharm

class Person:
    def __new__(cls, *args, **kwargs):
        # __new__两个方法：1.为对象分配空间，2.返回对象引用
        # 1.创建实例化对象前，最先调用
        # 2.初始化内存空间
        print("最先调用")
        # 3.继承父类object，调用__new__方法，创建内存空间，返回对象的引用
        print(super().__new__(cls))
        return super().__new__(cls)

    # （1）__ init__()方法的要点：
    # 1）名称必须固定，即要以两个下划线“_”开头和结束。
    #
    # 2）第一个参数固定，必须为：self。self指的就是刚刚创建好的实例对象。
    #
    # 3）一个类定义了__init__()方法以后，类实例化时就会自动为新生的类实例调用__init__()方法。
    #
    # 4）构造函数一般用于完成对象数据成员设置初值或进行其他必要的初始化工作，如果用户未涉及构造函数，Python将提供一个默认的构造函数。
    #
    def __init__(self):
        print("对象初始化")


person = Person()
print(person)


# 很多人误以为__init__是python对象的构造函数，其实它是初始化函数，
# 真正的构造函数是__new__，构造函数创建对象以后才会调用__init__为实例的属性赋值。
# 下面的代码展示了如何是用__init__函数
# __init__不是构造函数的最直接证据便是self，self是实例，这说明实例已经被创建。
class Stu:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def test(self):
        print("{name}")
        print("{name}".format(name=self.name))
        print("{age}".format(age=self.age))
        print("{score}".format(score=self.score))


s = Stu('小明', 18, 600)
Stu.test(s)
