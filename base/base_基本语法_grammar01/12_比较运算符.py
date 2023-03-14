# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:06
# @Author  : pgl
# @File    : 12_比较运算符.py.py
# @IDE     : PyCharm

# 比较运算符
# 比较运算符用来比较用的, 比较的结果有两个: 真True  假Flae
# Python中提供了6种运算符

python = 95
english = 92
c = 89
print("python分数:", python, "english分数:", english, "c分数:", c)
print("python < english: ", python < english)  # 判断python是否小于english
print("python > endlish: ", python > english)  # 判断python是否大于english
print("python == english: ", python == english)  # 判断python是否与english相等
print("pthon != english: ", python != english)  # 判断python是否与english不等
print("python <= english: ", python <= english)  # 判断python是否小于等于english
print("english >= c: ", english >= c)  # 判断english是否大于等于c

# 当需要判断一个变量是否结余两个值之间时, 可以采用"值1 < 变量 < 值2"的形式.
math = 150
print("math是否大于149, 小于151, 其结果是: ", 149 < math < 151)
