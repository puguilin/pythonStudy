# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:26
# @Author  : pgl
# @File    : 11_对列表进行统计计算.py.py
# @IDE     : PyCharm


# 对列表进行统计计算
# Python中进行统计计算主要有三个函数,
# count() 获取指定元素出现次数
# index() 用来获取指定元素首次出现所在下标, 也就是索引, 位置
# sum() 用来统计数值列表中各元素和

# listname(列表的名称).count(要判断是否存在的对象)
song = ["第三极", "老街", "new boy", "蓝莲花", "老街", "new boy", "蓝莲花", "new boy", "曾经的你"]  # 歌曲名称
number = song.count("new boy")  # 判断"new boy"出现的次数
print("new boy出现的次数", number)

# listname(列表的名称).index(要判断的对象), 在使用之前可以加一个if的判断, 看要判断对象是否在这个列表中
position = song.index("老街")  # 判断"老街"首次出现的位置,索引值
print("老街首次出现的位置: ", position)
# 加if语句判断
if "蓝莲花" in song:
    position = song.index("蓝莲花")
    print("蓝莲花首次出现的位置: ", position)
else:
    print("蓝莲花不在song列表中")

# sum(iterable[,start])
# sum(要统计的列表[,将统计结果加上start所指定的数,没有写那就默认为0])
grade = [89, 69, 78, 100, 23]  # 定义一个数值列表
total = sum(grade)  # 计算总的成绩
print("总成绩:", total)
total1 = sum(grade, 10000)
print("带上参数start的输出结果: ", total1)
