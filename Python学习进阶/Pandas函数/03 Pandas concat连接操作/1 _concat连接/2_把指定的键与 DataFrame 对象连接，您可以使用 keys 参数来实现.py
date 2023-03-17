# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 17:13
# @Author  : pgl
# @File    : 2_把指定的键与 DataFrame 对象连接，您可以使用 keys 参数来实现.py
# @IDE     : PyCharm


import pandas as pd

a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                  'B': ['B0', 'B1', 'B2', 'B3'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']},
                 index=[0, 1, 2, 3])
b = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B4', 'B5', 'B6', 'B7'],
                  'C': ['C4', 'C5', 'C6', 'C7'],
                  'D': ['D1', 'D2', 'D5', 'D6']},
                 index=[2, 3, 4, 5])
# 连接a与b,并给a，b连接一个指定的键
print("把指定的键与 DataFrame 对象连接，您可以使用 keys 参数来实现 \n", pd.concat([a, b], keys=['x', 'y']))

'''
  注意： 可以看出行索引 index 存在重复使用的现象，如果想让输出的行索引遵循依次递增的规则，那么需要将 ignore_index 设置为 True。
把指定的键与 DataFrame 对象连接，您可以使用 keys 参数来实现 
       A   B   C   D
x 0  A0  B0  C0  D0
  1  A1  B1  C1  D1
  2  A2  B2  C2  D2
  3  A3  B3  C3  D3
y 2  A4  B4  C4  D1
  3  A5  B5  C5  D2
  4  A6  B6  C6  D5
  5  A7  B7  C7  D6
'''

a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                  'B': ['B0', 'B1', 'B2', 'B3'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']},
                 index=[0, 1, 2, 3])
b = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B4', 'B5', 'B6', 'B7'],
                  'C': ['C4', 'C5', 'C6', 'C7'],
                  'D': ['D1', 'D2', 'D5', 'D6']},
                 index=[2, 3, 4, 5])
# 连接a与b,设置 ignore_index 等于 True
print("把指定的键与 DataFrame 对象连接，您可以使用 keys 参数来实现  \n "
      " 索引去重了  并且keys 指定的键(x 和 y )也被覆盖\n", pd.concat([a, b], keys=['x', 'y'], ignore_index=True))
'''
把指定的键与 DataFrame 对象连接，您可以使用 keys 参数来实现  
  索引去重了  并且keys 指定的键(x 和 y )也被覆盖
     A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D1
5  A5  B5  C5  D2
6  A6  B6  C6  D5
7  A7  B7  C7  D6
'''