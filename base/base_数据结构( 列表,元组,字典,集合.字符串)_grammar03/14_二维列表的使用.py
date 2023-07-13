#!/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:32
# @Author  : pgl
# @File    : 14_二维列表的使用.py.py
# @IDE     : PyCharm


# 二维列表的使用
# 我们想要获取一个二维列表的元素 room[行下标][列下标]  room[2][3] 获取第二行第三列的坐标
# 如何定义一个二维列表? 二维列表的每一个元素又是一个列表
room = [[1101, 1102, 1103, 1104, 1105, 1106, 1107],  # 二维列表的第一个元素
        [2101, 2102, 2103, 2104, 2105, 2106, 2107],  # 二维列表的第二个元素
        [3101, 3102, 3103, 3104, 3105, 3106, 3107],
        [4101, 4102, 4103, 4104, 4105, 4106, 4107]
        ]
print(room)

# 定义一个有规律的房间号
room1 = []
for i in range(1, 5):  # 使用for循环,定义最外层的列表, 即定义楼层
    room1.append([])  # 往room1里面每次添加一个空列表
    for j in range(1, 8):  # 这个是每一层房间数, 每个楼层有个房间
        room1[i - 1].append(i * 1000 + 100 + j)  # 为每一层的列表添加元素
        # 由于列表的索引是从0开始的,所以楼层是i-1。添加元素的内容是(楼层数*1000+100+当前房间数)
print(room1)

# 用列表推导式定义列表
room2 = [[i * 1000 + 100 + j for j in range(1, 8)] for i in range(1, 5)]  # [[生成列表元素的表达式,定义房间数量] 定义楼层数]
print(room2)

# 使用二维列表生成不同版式的故事
str1 = "千山鸟飞绝"
str2 = "万径人踪灭"
str3 = "孤舟蓑笠翁"
str4 = "独钓寒江雪"
list1 = [list(str1), list(str2), list(str3), list(str4)]
list2 = [list(str1), list(str2), list(str3), list(str4)]  # 这个list2为了检测逆序函数输出语法以及竖版排列写的

print("\n --横版的: --\n")
for i in range(4):  # 循环故事的行, 循环4次
    for j in range(5):  # 循环每一行的字, 循环5次
        if j == 4:  # 表示一行中的最后一个字, 需要换行
            print(list1[i][j])  # 换行输出
        else:
            print(list1[i][j], end="")  # 不换行输出 end""输出不换行, 在这个循环下的输出不换行
# print(,end"")用法
# 1.设置end=' '时，print()输出不换行，以空格结尾。
# 2.设置end=''时，print()输出不换行，以无字符结尾。
# 3.设置end='*'时，print()输出不换行，以*结尾。

list2.reverse()  # 使用reverse逆序函数
print("看一下列表1", list1)
print("看一下列表2的逆序排列", list2)  # 使用reverse逆序函数的时候直接输出原函数的名称就行

print("\n --竖版输出: --\n")  # 在竖版输出的时候要对列表进行逆序排列
for i in range(5):  # 对于竖版的, 它最外层的循环是循环的每一个字, 循环5次, 外层循环控制每一列的读取
    for j in range(4):  # 内层循环是循环每一个行数, 循环4次, 内层循环控制每一行的读取
        if j == 3:  # 如果j=3就代表最后一行, 换行输出
            print(list2[j][i])  # 换行输出结果
        else:
            print(list2[j][i], end="")  # 不换行输出

