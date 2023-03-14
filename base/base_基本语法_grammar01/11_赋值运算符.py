# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:05
# @Author  : pgl
# @File    : 11_赋值运算符.py.py
# @IDE     : PyCharm

# 赋值运算符
# 赋值运算符主要用的是 = 作用是把一个数的值赋给另外一个变量

# age += 1 就是把 age + 1 的结果赋值给age
age = 18
age += 1  # age = age +1
print(age)

# money -= 1 就是把 money - 1 的结果赋值给money
money = 1201
money -= 1  # money = money - 1
print(money)

# time *= 2 就是把 time * 2 的结果赋值给time
time = 3
time *= 2
print(time)

# weight /4 就是把weight /4 的结果赋值给weight(/除法并未有取整, 输出结果是浮点型)
weight = 101
weight /= 4
print(weight)

# height //4 就是把height //4 的结果赋值给height(//的除法是取整除法, 输出结果是整型)
height = 201
height //= 4
print(height)
