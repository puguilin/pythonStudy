# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 17:24
# @Author  : pgl
# @File    : 3_如果沿着 axis=1 添加，那么将会追加新的列.py
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
                 index=[4, 5, 6, 7])

# 沿着 axis=1，连接a与b   concat（）  axis=1 添加新的列
print("如果您想要沿着 axis=1 添加两个对象，那么将会追加新的列。\n", pd.concat([a, b], axis=1))


'''
如果您想要沿着 axis=1 （列方向） 添加两个对象，那么将会追加新的列。
      A    B    C    D    A    B    C    D
0   A0   B0   C0   D0  NaN  NaN  NaN  NaN
1   A1   B1   C1   D1  NaN  NaN  NaN  NaN
2   A2   B2   C2   D2  NaN  NaN  NaN  NaN
3   A3   B3   C3   D3  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN   A4   B4   C4   D1
5  NaN  NaN  NaN  NaN   A5   B5   C5   D2
6  NaN  NaN  NaN  NaN   A6   B6   C6   D5
7  NaN  NaN  NaN  NaN   A7   B7   C7   D6



如果您想要沿着 axis=0  （行方向） 那么将会追加新的行。
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