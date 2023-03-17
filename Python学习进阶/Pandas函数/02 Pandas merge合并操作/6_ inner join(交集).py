# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 16:55
# @Author  : pgl
# @File    : 6_ inner join(交集).py
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
# 求出两个subject_id的交集，并将结果作为键
print("inner join(交集) \n", pd.merge(left, right, on='subject_id', how="inner"))


