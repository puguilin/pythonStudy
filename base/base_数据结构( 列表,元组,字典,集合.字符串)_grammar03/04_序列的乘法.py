# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 16:52
# @Author  : pgl
# @File    : 04_序列的乘法.py.py
# @IDE     : PyCharm


# 序列的乘法
# 在进行数学计算的时候把一个数乘以另一个数就能得到两个数相乘的积
# 在Python中, 序列*乘数=重复n次的序列, 这个新的序列就是原来序列重复n次的结果
phone = ["HuaWeri Mate 10", "Vivo X21"]
print("序列*乘数=重复n次的序列", phone * 3)
# 序列中的乘法就是把序列中的内容重复几次, 重复几次, 重复几次,重复几次,重复几次
number = [1, 2, 3]
print("序列*乘数=重复n次的序列  ", number * 3)  # 不是把元素内容*3, 而是把内容重复3次

# 序列的乘法运算还可以实现初始化指定长度列表的功能
# 如果想创建长度5的列表,并且列表中的每个元素都是none值, 就可以这样定义
emptylist = [None] * 5
print("创建长度5的列表,并且列表中的每个元素都是none值",emptylist)

# 如果想输出10个*号的字符串
print("想输出10个*号的字符串", "*" * 10)

# 如果我们想输出重复的字符串, 可以使用序列的乘法
