# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 17:40
# @Author  : pgl
# @File    : 2_append() 函数也可接收多个对象.py
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
c = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B8', 'B9', 'B10', 'B7'],
                  'C': ['C9', 'C8', 'C7', 'C6'],
                  'D': ['D8', 'D5', 'D7', 'D6']},
                 index=[8, 9, 10, 11])
print("append() 函数也可接收多个对象 \n", a.append(b, c, a))
