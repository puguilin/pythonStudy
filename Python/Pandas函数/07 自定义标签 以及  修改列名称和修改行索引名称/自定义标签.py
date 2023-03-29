# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 11:46
# @Author  : pgl
# @File    : 自定义标签.py
# @IDE     : PyCharm


import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
print(df)
# 自定义标签 添加标签  , index=['名称', '标识', '数值', '班级']
df.columns = ['名称', '标识', '数值', '班级']
df.index = ['rank1', 'rank2', 'rank3']
print("\n 自定义标签 ")
print(df)

df = df.rename(
    columns={'名称': '名称1', '标识': '标识1', '数值': '数值1', '班级': '班级1'},
    index={'rank1': 'rank11', 'rank2': 'rank22', 'rank3': 'rank33'}
    )
print("\n 修改列名称和修改行索引名称 ")
print(df)
