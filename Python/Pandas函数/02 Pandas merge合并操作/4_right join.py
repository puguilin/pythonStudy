# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 16:44
# @Author  : pgl
# @File    : 4_right join.py
# @IDE     : PyCharm

import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Smith', 'Maiki', 'Hunter', 'Hilen'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6']})
right = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Bill', 'Lucy', 'Jack', 'Mike'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6']})
# 以right侧的subject_id为键
print("right join合并 \n", pd.merge(left, right, on='subject_id', how="right"))

'''
right join合并 
    id_x  Name_x subject_id  id_y Name_y
0   2.0   Maiki       sub2     1   Bill
1   3.0  Hunter       sub4     2   Lucy
2   NaN     NaN       sub3     3   Jack
3   4.0   Hilen       sub6     4   Mike
'''