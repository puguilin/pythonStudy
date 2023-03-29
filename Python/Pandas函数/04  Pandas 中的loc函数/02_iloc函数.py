# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 9:31
# @Author  : pgl
# @File    : 02_iloc函数.py
# @IDE     : PyCharm


import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
print(df)
# 数据集为以下内容，所有操作均对df进行
'''

       0   1     2       3
0  green   M  10.1  class1
1    red   L  13.5  class2
2   blue  XL  15.3  class1

'''

'''

iloc 主要是通过行号获取行数据，划重点，序号！序号！序号！
iloc[0:1]，由于Python默认是前闭后开，所以，这个选择的只有第一行！
iloc 它只支持int型。
'''

print(" 获取第一行数据 iloc[0:1]  左闭右开 \n" + str(df.iloc[0:1]))
