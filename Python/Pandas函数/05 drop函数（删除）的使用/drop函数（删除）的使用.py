# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 10:15
# @Author  : pgl
# @File    : drop函数（删除）的使用.py
# @IDE     : PyCharm


import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
print(df)
# 自定义标签  , index=['名称', '标识', '数值', '班级']
df.columns = ['名称', '标识', '数值', '班级']
df.index = ['rank1', 'rank2', 'rank3']
print("\n 自定义标签 ")
print(df)
'''
 drop函数默认删除行，列需要加axis = 1
（1）drop函数的使用：删除行、删除列
（2）drop函数的使用：inplace参数

采用drop方法，有下面三种等价的表达式：

凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。如果手动设定为True（默认为False），那么原数组直接就被替换。
也就是说，采用inplace=True之后，原数组名 对应的内存值直接改变；
而采用inplace=False之后，原数组名对应的内存值并不改变，需要将新的结果赋给一个新的数组或者覆盖原数组的内存位置。

'''

#  删除列      drop函数默认删除行，列需要加axis = 1  或者不加 axis = 1 使用  columns='班级'

df1 = df.drop('班级', axis=1)
# df1 = df.drop(columns='班级')
print(" \n 删除 班级 列之后的数据 df1 删除列需要加axis = 1 ")
print(df1)
print("  \n 删除 班级 列之后的数据（原数据不改变）df  删除列需要加axis = 1")
print(df)

# inplace=True 原始数据也会改变
df2 = df.drop('数值', axis=1, inplace=True)
print("\n 删除 数值 列 原数组值改变 df   (inplace=True) ")
print(df)
print("\n 删除 数值 列 新数组值 df2   (inplace=True) ")
print(df2)  # None


# 删除行  drop 默认删除行 或者使用  index='rank2'
dfh = df.drop('rank1')
print(" \n 删除行 rank1  原数组值不改变 df")
print(df)
print("\n 删除行 rank1  得到的新数据 dfh")
print(dfh)

# inplace=True 原始数据也会改变
# 或者 dfh2 = df.drop(index='rank2', inplace=True)
dfh2 = df.drop('rank2', inplace=True)    # 或者 index='rank2', inplace=True
print("\n 删除行 rank2  原数组值df ")
print(df)
print("\n删除行 rank2  新数组值dfh2 ")
print(dfh2)  # None


