# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:12
# @Author  : pgl
# @File    : 16_基本输入和输出.py.py
# @IDE     : PyCharm

# 使用input()函数输入
# 基本输入和输出
# 在Python中可以使用内置函数input()来接收用户在键盘上输入的内容
# 基本语法: variable = input("提示文字") # 提示文字就是一个字符串, 用来指定显示给用户接下来将要输入什么, 然后把这个结果保存到一个变量中
# 对于input()函数它的返回值是一个字符串类型的(str), 如果想要通过input()函数得到整型或者浮点型数据需要进行强制类型转换,
tip = input("请输入文字: ")  # 获取键盘上的输入
print(tip)  # 输出键盘输入结果
print(type(tip))  # 看一下输入的字符类型 str是字符串类型, 如果想获取到整型的数值还要进行强制类型转换
print(type(int(tip)))

# 根据身高, 体重计算BMI指数(改进版)
height = float(input("请输入您的身高(单位为米): "))
weight = float(input("请输入您的体重(单位千克): "))
print("您的身高: ", height, "米", "您的体重: ", weight, "千克")
bmi = weight / (height * height)
print("您的BMI指数: ", bmi)
if bmi < 18.5:
    print("您的体重过轻~@_@~")
if bmi >= 18.5 and bmi < 24.9:
    print("您的体重正常, 请继续保持^_^")
if bmi >= 24.9:
    print("您的体重过重^@_@^")

# 使用print()函数输出
# print(输出内容) 输出内容可以是数字,也可以是字符串,如果是字符串要使用字符串定界符括起来,
# 只要是字符串定界符括起来的内容就认为是字符串会直接输出, 输出内容可以是包含运算符的表达式,并且这样的内容会先计算表达式中的结果,然后再把这个结果输出
a = 10
b = 6
print("数字: ", 6)  # 输出的是数字
print("表达式: ", a * b)  # 输出的是表达式
# 指定盘符以及指定文件输出
fp = open(r'F:\11_26.txt', 'a+')  # 输出到F盘的11_26.txt文档中, 且11_26.txt不需要自己新建
print("字符串: ", "成功的唯一秘诀--坚持最后一分钟", file=fp)  # 输出的字符串, 写入到F盘的11_26.txt文档中,11_26.txt不需要自己新建
fp.close()  # 关闭文件
