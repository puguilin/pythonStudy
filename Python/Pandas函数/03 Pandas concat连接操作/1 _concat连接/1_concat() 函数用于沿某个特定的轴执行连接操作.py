# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 17:01
# @Author  : pgl
# @File    : 1_concat() 函数用于沿某个特定的轴执行连接操作.py
# @IDE     : PyCharm
import b as b
import pandas as pd

a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                  'B': ['B0', 'B1', 'B2', 'B3'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']},
                 index=[0, 1, 2, 3])
b = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B4', 'B5', 'B6', 'B7'],
                  'C': ['C4', 'C5', 'C6', 'C7'],
                  'D': ['D4', 'D5', 'D6', 'D7']})
# 连接a与b
print("concat() 函数用于沿某个特定的轴执行连接操作 \n", pd.concat([a, b]))

'''
concat() 函数用于沿某个特定的轴执行连接操作 
     A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
0  A4  B4  C4  D4
1  A5  B5  C5  D5
2  A6  B6  C6  D6
3  A7  B7  C7  D7
'''
