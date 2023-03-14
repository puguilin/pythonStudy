# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:25
# @Author  : pgl
# @File    : 04_嵌套循环.py.py
# @IDE     : PyCharm

# 循环嵌套
# 我们在电影院中找座位号, 需要知道第几排第几列才能知道自己的座位号, 比如先找行, 再找列, 寻找座位的过程就类似于循环嵌套
# 首先写的最外层的循环
for row in range(1, 5):  # 不包括第5排
    print("当前坐在排: ", row)
    if 2 == row:  # 判断排数是否等于2
        print("第二排是我们座位所在的排数! ")  # 已经找打第二排了, 下面找一下第二排所在的列
        # 在if 语句块中嵌套一个寻找列的循环
        for column in range(1, 8):  # 不包括第8列
            print("当前所在的列: ", column)
            if 3 == column:
                print("第三列, 这是您的座位")
                break  # 跳出循环
        break  # 跳出循环

# 循环语句前嵌套不止上面一种, 下面介绍几种循环嵌套
# while 条件表达式1:
#     while 条件表达式2:
#         循环体2
#     循环体1
#
# while 条件表达式:
#     for 迭代变量 in 对象:
#         循环体2
#     循环体1
#
# for 迭代变量 in 对象:
#     while 条件表达式:
#         循环体2
#     循环体1

# 使用for循环嵌套打印九九乘法表(需要使用双重的for循环进行)
for i in range(1, 10):  # 最外层控制的是行数, 第1行到第9行, 输出结果1,2,3,4,5,6,7,8,9
    for j in range(1, i + 1):  # 这层控制的是列数, 输出与行数相等的列
        print(str(j) + "×" + str(i) + "=" + str(j * i) + "\t", end='')  # \t是加上一个table键,
    print(" ")  # 输出
