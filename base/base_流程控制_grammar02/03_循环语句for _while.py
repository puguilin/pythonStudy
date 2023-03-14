# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:23
# @Author  : pgl
# @File    : 03_循环语句for _while.py.py
# @IDE     : PyCharm


# 循环语句--for循环
# for 循环条件表达式:
# for 迭代变量 in 对象:
#     循环体(循环中要执行的语句, 和for循环一样, 每个循环体中都要有4个空格或者1个tab的缩进量)
# for 循环在执行的时候先是要判断要循环的对象中是否有要取的项, 如果有就取下一项, 并且执行循环体中的项, 再继续进行判断, 如果有要取的项就继续取下一项, 继续执行难循环体
# 直到所有的循环都去完就结束循环
# 对于for 循环最基本的应用就是数值循环

# 计算 1+2+3+4+...+100
print("计算1+2+3+...+100的结果为: ")
result = 0  # 保存累加结果的变量
for i in range(101):  # rang是Python中的一个内置函数是用来进行循环计算的
    result += i  # (循环题的内容让结果进行累加) 实现累加
print(result)  # 输出累加结果
# 在Python中进行数值循环要使用range()函数, 它主要生成一系列的连续整数,1.2.3.4.5.6....
# 在Python2中, range()函数表达式是range()函数
# range()函数的基本语法
# range(start, end, step)

for x in range(1, 10, 2):
    print(x, end=' ')  # end=' '为了让输出结果在一行显示, 不然每一个输出结果都占一行
for y in range(1, 10):  # 输出结果包括1, 但是不包括10
    print(y, end=' ')
for y in range(10):  # 输出结果从0开始, 到9结束, 不包括10
    print(y, end=' ')

print("今有物不知其数, 三三数之剩二, 五五数之剩三, 七七数之剩二, 问几何?\n")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件
        print("答曰2: 这个数是 ", number)

# for除了可以循环数值, 也可以逐个遍历字符串
string = '不要再说我不能'  # 定义一个字符串
print(string)
for ch in string:  # 通过for语句依次遍历这个字符串, 并且输出, 设置迭代变量ch, 要迭代的对象是这个字符串
    print("遍历这个字符串得到的结果是: ", ch)  # 输出ch


# 循环语句
# 在Python中主要有两种循环, 一种是while循环, 一种是for循环
# 1. while循环
# while 条件表达式:
#     循环体(在循环体中,是一组被重复执行的语句, 每条语句前必须加一个缩进量, 可以是一个table键或者是四个空格)
# 在进行while语句循环中, 先判断条件表达式的值是否为真, 当值为真的时候执行循环体当中的语句, 语句执行完毕之后重新判断条件表达式的值, 知道表达式的结果为假是才退出循环

print("今有物不知其数, 三三数之剩二, 五五数之剩三, 七七数之剩二, 问几何?\n")
none = True  # 作为循环条件的变量
number = 0  # 计数变量
while none:
    number += 1  # 计数加1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件
        print("答曰: 这个数是", number)
        none = False  # 如果忘记这个语句, 这个循环就是死循环, 会一直运行下去, 虽然找到了符合条件的数, 也不会退出循环
