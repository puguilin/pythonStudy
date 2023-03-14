# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 11:50
# @Author  : pgl
# @File    : 05 方法的动态性.py
# @IDE     : PyCharm

# 在Python中比较特殊的是，可以动态地为类和对象增加成员。

class Student:
    def work(self):
        print("工作挣钱")


def play(s):  # 注意与work区别，class里没有这个函数，此时无法用通过s.play()调用
    print("{}爱玩游戏".format(s))


Student.play = play  # 增加了此语句便可以通过s.play()调用了
s = Student()
s.work()
s.play()
