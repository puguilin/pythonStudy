
# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:11
# @Author  : pgl
# @File    : 15_位运算符的优先级.py.py
# @IDE     : PyCharm

# 位运算符的优先级
# 所谓运算符的优先级就是在使用的哪个运算符先计算, 哪一个运算符后计算, 这和在数学的四则运算先乘除后加减是一个道理
# python运算规则: 优先级高的运算先执行, 优先级低得运算后执行, 同一优先级的操作按照先从左到右的顺序执行, 数学中可以使用括号改变运算次序, Python中也可以通过括号改变运算次序

# 运算符从高到低
# 类型             运算符           说明
# 单目运算符        ~ + -           取反. 正号和负号
# 算数运算符        * / % //        乘 除 求余
# 算数运算符        + -             加 减
# 位运算符          <<  >>          左移 右移
# 位运算符          &   ^           位与  位异或
# 位运算符          |               位或
# 比较运算符        < <= > >=        小于 小于等于 大于 大于等于
# 比较运算符        !=   ==          不等于   等于

