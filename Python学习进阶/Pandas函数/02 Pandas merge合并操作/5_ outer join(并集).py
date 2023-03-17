# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 16:48
# @Author  : pgl
# @File    : 5_ outer join(并集).py
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
# 求出两个subject_id的并集，并作为键
print("outer join(并集) \n", pd.merge(left, right, on='subject_id', how="outer"))


'''
outer join(并集) 
    id_x  Name_x subject_id  id_y Name_y
0   1.0   Smith       sub1   NaN    NaN
1   2.0   Maiki       sub2   1.0   Bill
2   3.0  Hunter       sub4   2.0   Lucy
3   4.0   Hilen       sub6   4.0   Mike
4   NaN     NaN       sub3   3.0   Jack
'''