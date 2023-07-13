# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 16:57
# @Author  : pgl
# @File    : 06_序列的计算.py.py
# @IDE     : PyCharm


# 计算序列的长度,最大值和最小值
# Python中提供了计算序列长度的内置函数 len()
# 计算序列的长度就是统计一下
number = [15, 30, 60, 70, 80]
print("列表的长度: ", len(number))
string = "woxue python"
print("字符串的长度: ", len(string))  # 计算的时候空格也算长度

# 计算序列中的最大元素max(), 最小值max() 多用于元素的类型是数值型的时候
number = [15, 30, 60, 70, 80]
print("列表中元素的最大值是: ", max(number))
number = [85, 30, 10, 70, 80]
print("列表中元素的最小值是: ", min(number))

# list(): 把序列转换为列表
# str(): 把序列转换为字符串
# sum(): 计算列表中的元素和
# sorted(): 对元素进行排序
# reversed(): 反转元素
# enumerate(): 把序列转化为索引序列

a = [1, -1, 3]
print("把序列转换为列表: ", list(a))
print("把序列转换为字符串: ", str(a))
print("列表a中的元素和: ", sum(a))
print("对a中元素进行排序: ", sorted(a))
print("对a中元素进行反转: ", reversed(a))

# 反转元素
a1 = reversed(a)
print('列表反转结果转换成列表：', list(a1))
