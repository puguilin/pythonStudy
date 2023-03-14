# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:20
# @Author  : pgl
# @File    : 02_if_选择语句.py.py
# @IDE     : PyCharm

# 选择语句, 也是条件语句
# 选择语句主要三种形式, 简单的if语句; if...else 语句; if...elif...else语句, 在使用if语句的时候也可以嵌套使用


# 简单的if语句
# if 条件表达式(布尔值):
# 语句块 (别忘了缩进)
print("今有物不知其数, 三三数值剩二, 五五数之剩三, 七七数之剩二, 问几何?\n")  # \n换行
number = int(input("请输入您认为符合条件的数: "))  # 因为要进行数字的运算, 所以要转成int型, 输入一个数
# 下面进行判断
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件 % 是求余符号
    print(number, "符合条件")

a = 10
b = 5
if a > b:
    print(a)

number2 = 5
if number2 == 5:
    print("number2的值为5")

# if条件语句中符合条件的时候执行多个语句
number3 = 15
if number3 < 18.5:
    print("numbers的值为15")  # 如果没有缩进就会被认为不属于这个if语句, 就会无条件的执行, 写代码的时候一定要注意这个异常
    print("number3的值小于18.5")  # 如果没有缩进就会被认为不属于这个if语句, 就会无条件的执行, 写代码的时候一定要注意这个异常

# if 条件表达式 :
#    语句块1
# else:
#    语句块2

print("今有物不知其数, 三三数之剩二, 五五数之剩三, 七七数之剩二, 问几何?\n")
number = int(input("请输入您认为符合条件的数: "))  # 输入一个数
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 余数的是% == 不是一个等号是两个等号
    print("符合条件")
else:  # else语句是不可以单独使用的!
    print("不符合条件")

# if...elif...else语句
# if语句 --> 如果...就...
# if...else语句 --> 如果...就...否则...(非黑即白)
# if...elif...else(多分枝选择语句) --> 如果满足某种条件, 就进行某种处理, 否则, 如果满足另一种条件, 则执行另一种处理...

# if 表达式1:
#     语句块1
# elif 表达式2:
#     语句块2
# ..........
# else:
#     语句块n
# 根据输入的玫瑰花的朵数输出相对应的花语
print("在古希腊神话中, 玫瑰集爱与美于一身. 人们常用玫瑰来表达爱意. \n 送不同朵数的玫瑰花代表的含义也不同.")
number = int(input("输入你想送的玫瑰花的朵数, 嘿嘿会告诉您含义: "))  # 获取输入的朵数, 单位为朵
if number == 1:
    print("1朵: 你是我的唯一")
elif number == 3:
    print("3朵: I Love You! ")
elif number == 10:
    print("10朵: 十全十美")
elif number == 99:
    print("99朵: 天长地久")
elif number == 108:
    print("108朵: 求婚哦 ^_^")
else:
    print("嘿嘿也不知道了, 可以考虑送1朵, 3朵, 10朵, 99朵或者108朵哦 ~@_@~")
# 假设已经定义了一个布尔型变量flag 当我们使用这个变量的时候建议:
# if flag:         不要写成    if flag == True:   (虽然不报错, 但是不规范不优雅)
# if not flag:     不要写成    if flag == False:  (虽然不报错, 但是不规范不优雅)


#  求两个数中较大的一个, 通过if...else语句实现
a = 10
b = 20
if a > b:
    r = a
else:
    r = b
print(r)

# 求两个数中较大的一个
a = 10
b = 20
r = a if a > b else b  # Python中的条件表达式
print(r)

# 条件表达式的基本能语法:
# 结果1 if 表达式 else 结果2
# 在if之前的结果1是条件表达式为真的时候返回的结果; 在else之后的结果2是条件表达式为假的时候返回的结果
# 通常把条件表达式赋给一个变量, 如果条件表达式的值为真, 就把结果1赋给这个变量; 如果条件表达式的值为假, 就把结果2赋给这个变量

# 应用条件表达式求绝对值的功能
a1 = -10
b1 = a if a > 0 else -a
print(b1)
