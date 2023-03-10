# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 14:53
# @Author  : pgl
# @File    : 06_数据类型.py.py
# @IDE     : PyCharm


# 数据类型就是数据的类型. Python中有数字类型. 字符串类型. 布尔类型. 以及各种类型间的转换
# 数据   ------->     数据类型
# 整数   ------->     整型
# 小数   ------->     浮点型
# 字母   ------->     字符串型

# 1.整数有: 十进制(逢十进一, 由0--9组成). 八进制(逢九进一, 由0--7组成). 二进制(逢二进一, 由0--7组成). 十六进制(逢十六进一, 由0--9以及A--F组成)
a = 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
b = 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
print(a + b)

# 2.浮点数: 浮点数由整数部分和小数部分组成

print(180 / 26)
# 2.2 小数点不确定问题
print(0.1 + 0.2)
# 保留指定位数
print(round(0.1 + 0.3, 2))
height = 1.7236401208  # 保存身高的变量, 单位: 米
print("您的身高: ", height)
print("您的身高: " + str(height))  # 建议采用这种方式进行输出

weight = 48.5  # 保存体重的变量, 单位: 千克
print("您的体重: " + str(weight))
bmi = weight / (height * height)  # 计算BMI指数
print("您的BMI指数: ", bmi)
if bmi < 18.5:
    print("您的体重过轻~@_@~")
if 18.5 <= bmi < 24.9:
    print("您的体重正常, 轻基础保持 ^_^")
if bmi >= 24.9:
    print("您的体重过重-_-")
# 使用浮点数进行计算时, 可能会出现小数位数不确定的情况
# Python中四舍五入函数, round函数, 也可以指定保留小数位数的四舍五入
print(height + weight)
print(round(height + weight))
print(round(height + weight, 6))

# 3. 复数: 复数由实部和虚部组成 复数: 实部+虚
print(1.23 + 4.56j)



