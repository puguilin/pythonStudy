# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:31
# @Author  : pgl
# @File    : 13_列表推导式.py.py
# @IDE     : PyCharm

# 列表推导式
# 列表推导式可以快速生成一个列表, 或者根据某个列表生成满足指定需求的列表
# 我们要生成由10个元素组成的列表, 且每个元素的值在10--100之间的随机整数,包括100
# 方法1
import random  # 导入生成随机数的模块

list = []  # 定义一个空列表
for i in range(10):  # 循环10次
    list.append(random.randint(10, 100))  # append()向列表中添加元素, random.randint(10,100)是生成随机数, 起始值是10,结束值是100
print("输出列表: ", list)
# 方法2    列表推导式
list1 = [random.randint(10, 100) for i in range(10)]  # 定义了一个列表, 随机数产生的列表, 列表中10个数是通过for循环产生的
print("方法2产生的列表: ", list1)

# 列表推导式的语法格式:
# list = [Expression for var in range]
# 列表的名称 = [表达式,这个表达式就是描述新列表的元素的, for 关键字 in range(迭代对象)]
# 应用列表推导式生成1--10之间所有偶数生成数的平方
list2 = [i * i for i in range(2, 11, 2)]  # 列表list2的元素是i*i ,i是1到10之间的偶数集合
print("1到10之间所有偶数平方产生的列表: ", list2)

# 根据列表生成指定需求的列表
# newlist = [expression for var in list]
# 列表的名称 = [表达式,这个表达式就是描述新列表的元素的, for 关键字 in 一个列表]
# 生成一个把所有商品价格打5折的列表
price = [1000, 500, 888, 666]
sale = [int(x * 0.5) for x in price]  # int(x*0.5), 转化为整型
print("原价格:", price)
print("打折后的价格:", sale)

# 从列表中选择符合条件的元素组成新的列表
# newlist = [Expression for var in list if condition]
# 列表名称 = [生成列表元素的表达式, for循环语句, 添加了if条件语句, 这样就能选择符合条件的元素添加到新的元素当中]
price1 = [1002, 502, 882, 662]
sale1 = [y for y in price1 if y >= 800]
print("输出大于等于800的组成的列表: ", sale1)
