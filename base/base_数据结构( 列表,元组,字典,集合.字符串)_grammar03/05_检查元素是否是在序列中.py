# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 16:54
# @Author  : pgl
# @File    : 05_检查元素是否是在序列中.py.py
# @IDE     : PyCharm

# 检查某个元素是否是序列的成员(看某个元素是够在序列当中) in 关键字来实现
# valye(要检查的元素) in sequence(指定的序列, 要判断的这个元素是否在这个序列中)
nba = ["乔丹", "拉塞尔", "周一", "周二", "周三", "周四", "周五", "周六", "周日", "许巍"]  # 定义了一个字符串类型的列表
print("乔丹" in nba)  # 判断"科比"是否在nba这个列表中, 结果True
print("李荣浩" in nba)  # 判断"李荣浩"是否在nba这个列表中, 结果False

# 如果判断一个元素是否不在这个列表当中, 使用not in关键字来实现
print("李荣浩" not in nba)  # 判断"李荣浩"是否不在nba这个列表中, 结果True
