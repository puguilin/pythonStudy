# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:02
# @Author  : pgl
# @File    : 09_数值类型转换.py.py
# @IDE     : PyCharm


# 数据类型转换
# Python是一种动态类型的语言, 也称为弱类型语言, 在使用变量之前不要先声明这个变量(这个变量的类型)

# 数值类型转换的函数
# int()     ---->  把一个值转换为整型
# float()   ---->  把一个值转换为浮点型
# str()     ---->  把一个值转换为字符串类型
# hex()     ---->  把整数转换为十六进制字符串
# oct()     ---->  整数转换为八进制字符串

money_all = 56.75 + 72.91 + 88.50 + 26.37 + 68.51  # 累计总计金额, 因为带小数,得到的结果是浮点类型的
# 现在想把浮点类型转换为字符串
money_all_str = str(money_all)  # 转化为字符串
print("尚品总金额为: " + money_all_str)
money_real = int(money_all)  # 转化为整型(进行抹零处理)
money_real_str = str(money_real)  # 转化为字符串
print("实收金额为: " + money_real_str)
