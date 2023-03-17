# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 14:20
# @Author  : pgl
# @File    : 1_ 创建空的DataFrame对象.py
# @IDE     : PyCharm


import pandas as pd

# ======================1) 创建空的DataFrame对象 pd.DataFrame()===========================
df = pd.DataFrame()
print("创建空的DataFrame对象 \n", df)

# ======================2) 列表创建DataFame对象 ===========================
# 示例 1，单一列表创建 DataFrame：
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print("列表创建DataFame对象 \n", df)

# 示例 2，使用嵌套列表创建 DataFrame 对象
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print("使用嵌套列表创建 DataFrame 对象 \n", df)

# 示例 3，指定数值元素的数据类型为 float：
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print("指定数值元素的数据类型为 float \n", df)

# ======================3) 字典嵌套列表创建==========================

# 示例1  使用默认标签
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data)
# 这里使用了默认行标签，也就是 range(n)。它生成了 0,1,2,3，并分别对应了列表中的每个元素值。
print("字典嵌套列表创建，使用默认标签 \n", df)

# 示例 2，现在结合上述示例1 添加自定义的行标签：
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print("字典嵌套列表创建 添加自定义的行标签 \n", df)

# ========================4) 列表嵌套字典创建DataFrame对象==========================

# 示例 1 如果其中某个元素值缺失，也就是字典的 key 无法找到对应的 value，将使用 NaN 代替。
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print("列表嵌套字典创建DataFrame对象 \n", df)

# 示例 2，结合上述示例 1 添加行标签索引：
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print("列表嵌套字典创建DataFrame对象 添加行标签索引\n", df)

# 使用列表嵌套字典以及行、列索引表创建一个 DataFrame 对象
# 注意：因为 b1 在字典键中不存在，所以对应值为 NaN。
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print("使用列表嵌套字典以及行、列索引表创建一个 DataFrame 对象 df1 \n", df1)
print("使用列表嵌套字典以及行、列索引表创建一个 DataFrame 对象 df2 \n", df2)
