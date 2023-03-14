# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:26
# @Author  : pgl
# @File    : 05_跳转语句_break_continue.py.py
# @IDE     : PyCharm


# 跳转语句
# 在前面学习了for循环语句和while循环循环语句, 无论是哪种循环都需要一个跳出循环的条件否则都是死循环
# 晚睡 --> 起床觉得很累 --> 保证以后一定早睡 --> 上网 --> 晚睡,,,,所以一定要设置一个能退出语句的条件
# 在for循环结束迭代之前, 或者是while循环找到结束条件之前, 来提前结束循环
# break语句: 完全退出循环
# continue语句: 只能跳出一次循环

print("今有物不知其数, 三三数之剩二, 五五数之剩三, 七七数之剩二, 问几何?\n")
for number in range(100):
    print(number)
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("答曰: 这个数是 ", number)
        break  # 跳出循环(可以提前退出循环)

# continue语句: 只能跳出一次循环

# 不能完全跳出循环, 只能终止本次循环, 提前进入下一次循环中
# 从1数到99, 出现7以及7的倍数的时候拍一下桌子, 问拍多少下桌子
# 思路: 假定从 1 数到 99, 每个数都拍一下桌子, 一共拍99次, 就把99次保存到一个变量中,之后编写一个 for 循环,
# 从 1 循环到99,每出现一次不拍桌子的情况, 就让这个变量减1, 否则的话就不执行减 1 的操作, 进行下一次循环,最后剩下的次数就是拍桌子的次数
# range()是创建一个整数列表，一般用于for循环当中
# range(start, stop, step)
# start:计数从start开始，默认为0.range(9)和range(0,9)是一样的。
# stop:计数到stop为止，但不包括stop。
# step：步长，也叫间隔
# 首先判断这个数是不是7的倍数, 如果是7的倍数,对它进行求余, 余数是0
total = 99  # 记录拍桌子的次数
for number in range(1, 100):  # 从1循环到99, range()是创建一个整数列表，一般用于for循环当中,
    if number % 7 == 0:  # 是7的倍数
        continue  # 继续下一次循环
    else:  # 否则判断这个数是不是以7开头或者以7结尾的
        string = str(number)  # 首先把这个数转换为字符串
        if string.endswith('7'):  # 判断这个字符串是否以7结尾
            continue  # 继续下一次循环
    total -= 1  # 可拍次数-1
print("从1拍到99共拍桌子: ", total, "次.")
