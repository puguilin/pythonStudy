# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 16:32
# @Author  : pgl
# @File    : 1_在单个键上进行合并操作.py
# @IDE     : PyCharm


# 通过 on 参数指定一个连接键，然后对上述 DataFrame 进行合并操作：
import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Smith', 'Maiki', 'Hunter', 'Hilen'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6']})
right = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['William', 'Albert', 'Tony', 'Allen'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6']})
# 通过on参数指定合并的键
print("在单个建上进行合并 \n", pd.merge(left, right, on='id'))


'''
    id  Name_x subject_id_x   Name_y subject_id_y
0   1   Smith         sub1  William         sub2
1   2   Maiki         sub2   Albert         sub4
2   3  Hunter         sub4     Tony         sub3
3   4   Hilen         sub6    Allen         sub6

'''