# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:03
# @Author  : pgl
# @File    : 10_运算符.py.py
# @IDE     : PyCharm


# 算数运算符
# Python中 运算符主要包括: 算数运算符. 赋值运算符. 比较运算符. 逻辑运算符. 位运算符
# 算数运算符就是用来进行四则运算的以及求余
# 36 ÷ 5 = 7......1  使用 Python 语言就是 36 % 5 = 1
# 求余符号与第一个操作数无关, 求余符号与第二个操作数一致  36 % -5 = -4
print(-36 % 5)
print(36 % -5)
print(-36 % -5)

# 在Python中进行除法运算的时候有两个运算符, 一个是/另一个是//
# / 在进行除法运算的时候得到的是浮点数
# //在进行除法运算的时候得到的是整数, 也就是取整符号
print(36 / 5)
print(36 // 5)

# 计算学生成绩的分差以及平均分
python = 95  # python分数
english = 92  # 英语分数
c = 89  # C语言分数
sub = python - english  # python和英语的分数差
avg = (python + english + c) / 3  # 计算平均分
print("Python课程和English课程的分数之差为: ", sub, "分")
print("三门课程的平均成绩为: ", avg, "分")

# python中的算数运算主要有: +.-.*././/.% 其中/.//.% 除数不能为0, 如果为0就会出现除数为0的异常
# /表示正常的除法, 结果是浮点型
# //表示取整除法, 结果是整型
