# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 11:30
# @Author  : pgl
# @File    : Pandas去重复数据drop_duplicates详解.py
# @IDE     : PyCharm


import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1'],
    ['black', 'S', 12.3, 'class3'],
    ['black', 'S', 12, 'class3']
])
print(df)
# 自定义标签  , index=['名称', '标识', '数值', '班级']
df.columns = ['名称', '标识', '数值', '班级']
df.index = ['rank1', 'rank2', 'rank3', 'rank4', 'rank5']
print("\n 自定义标签 ")
print(df)

'''
    去重： df.drop_duplicates(subset=None, keep='first', inplace=False)
subset： 列标签，可选  None  
    subset=None 表示 两条记录完全一样时才会删除  
    subset='名称'  选择标签时  只要当前列的标签下的值相同就会删除重复的记录
keep： {‘first’, ‘last’, False}, 默认值 ‘first’
first： 保留第一次出现的重复项。
last： 删除重复项，仅保留最后一次出现的重复项。
False： 删除所有重复项。
inplace：布尔值，默认为False，是否删除重复项或返回副本

'''
df.drop_duplicates(subset='名称', keep='first', inplace=True)
print("\n 删除重复的数据  保留第一次出现的记录 ")
print(df)

