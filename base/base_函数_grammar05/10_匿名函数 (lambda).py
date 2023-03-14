# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:09
# @Author  : pgl
# @File    : 10_匿名函数 (lambda).py.py
# @IDE     : PyCharm


# 匿名函数 (lambda)    # 相当于电影中的群演, 通常情况下这样的函数值使用一次, 不会给它们起名字
# 计算圆的面积的函数(需要使用数学模块math模块)
# 方法1:
import math


def circlearer(r):  # 计算圆的面积的函数
    return math.pi * r * r  # 计算圆的面积


r = 10  # 半径
print("半径为", r, "的圆面积为: ", circlearer(r))

# 方法2:
r1 = 11  # 重新定义的变量
result = lambda r1: math.pi * r1 * r1
print("方法2输出结果: ", result(r1))

# lambda基本语法
# result = lambda [arg1 [,arg2,......,argn]]:expression
# 赋一个值, 然后是关键字lambda, 后面跟上一些参数, 对于这个参数是要传递的参数可以有多个, 多个参数之间使用','分隔, 然后使用':', 之后接着表达式, 表达式是实现具体功能的表达式, 主要用于计算返回结果,
# 如果我们不省略参数, 那个在表达式中会应用这些参数, 不过在表达式中不能出现for或者while等非表达式语句

# 模拟, lambda表达式的具体应用
bookinfo = [('不一样的卡梅拉', 22.50, 120), ('零基础学Android', 65.10, 89.80), ('摆渡人', 23.40, 36.00),
            ('福尔摩斯探案集', 22.50, 128)]  # 商品列表
print('爬取到的商品信息: \n', bookinfo, "\n")
bookinfo.sort(key=lambda x: (x[1], x[1] / x[2]))  # 指定排序规则,x[1]是索引值为1的元素, 也就是折扣之后的价格; x[2]是原价, x[1])/x[2]是折扣比
print('排序后的商品信息: \n', bookinfo, "\n")
