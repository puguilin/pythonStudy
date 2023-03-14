#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved
#
# @Time    : 2023/02/12 23:21
# @Author  : pgl
# @File    : 04_保留字.py
# @IDE     : PyCharm
# Python 保留字与标识符
# 怎么在Python中使用变量?
python = "学会Python还可以飞"  # 定义了一个字符型的变量
print(python)
age = 18  # 定义了一个整型的变量
print(age)

# 通过内置的type函数查询变量的类型
print(type(python))
print(type(age))

# 变量的类型是可以改变的
nickname = "碧海苍梧"  # 定义了一个字符串类型的变量
print(type(nickname))
nickname = 1024
print(type(nickname))

# 使用变量, 在Python中允许多个变量指向同一个值, 这就像一个盒子上面贴了很多标签,通过哪个标签都能得到这个盒子
no = number = 2048
print(no)
print(number)
# 通过内置的id函数可以获取变量的内存地址
print(id(no))
print(id(number))

# 变量的命名不是任意的,需要遵循几个规则:
# 1.必须是一个有效的标识符
# 2.选择有意义的单词
# 3.不能使用Python中的保留字
# 4.谨慎用小写字母l和大写字母O

# 常量: 在程序运行过程中, 值不能改变的量, 通常不使用
