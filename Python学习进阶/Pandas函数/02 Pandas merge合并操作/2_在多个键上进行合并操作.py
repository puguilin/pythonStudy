# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/15 16:34
# @Author  : pgl
# @File    : 2_在多个键上进行合并操作.py
# @IDE     : PyCharm

# 在多个键上进行合并操作

import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Smith', 'Maiki', 'Hunter', 'Hilen'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6']})
right = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'Name': ['Bill', 'Lucy', 'Jack', 'Mike'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6']})
print("在多个键上进行合并操作 \n", pd.merge(left, right, on=['id', 'subject_id']))


'''
在多个键上进行合并操作 
    id Name_x subject_id Name_y
0   4  Hilen       sub6   Mike

'''
