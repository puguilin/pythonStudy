# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:08
# @Author  : pgl
# @File    : 09_遍历列表.py.py
# @IDE     : PyCharm

# 遍历列表
# 遍历列表就是把列表中的所有元素访问一遍, 在Python中访问列表的方法有多种, 现在主要介绍两种
# 1.直接使用for循环
# 2.使用for循环和enumerate()函数

# 1. 直接使用for循环, 这种只能输出元素的值
# for item(获取到的元素值) in listname(列表的名称):
#     # 输出item

# 通过遍历列表的方式输出2018年NBA常规赛西部球队排名(主要输出前5名)

# 直接通过for循环
print("2018年NBA常规赛西部排名: ")
team = ["火箭", "勇士", "开拓者", "雷霆", "爵士"]  # 定义一个列表
for item in team:
    print(item)  # 输出每一个球队的名称

# 有时候不仅仅需要元素值这一项, 也需要元素的索引值, 需要借助for循环和enumerate()函数实现
# for item in enumerate(listname):
# 通过index输出检索内容,通过item输出索引值
team = ["火箭", "勇士", "开拓者", "雷霆", "爵士"]  # 定义了一个字符串类型的列表
for index, item in enumerate(team):  # index是代表索引值的对象
    print("enumerate函数:", index + 1, item)  # 索引值是从0开始的,想要输出球队的排名,就要从1开始,所以要index+1, 之后再输出球队的名称

# a = [1,2,3]
# b = ["一","二","三"]
# print(a,b)
# print(a,'\n',b)

# 分两列显示2017--2018赛季NBA西部联盟前八名球队.
print("2017--2018赛季NBA西部联盟排名:\n")
team = ["火箭", "勇士", "开拓者", "雷霆", "醍醐", "马刺", "森林狼"]
for index, item in enumerate(team):
    # 由于要分两列进行输出, 我们要进行判断, 通过if语句判断这个索引值是否能被2整除, 如果能被2整除,就不换行输出, 直接输出item
    if index % 2 == 0:
        print(item + "\t\t", end='')  # , end=''表示不换行输出
    # 否则就换行输出
    else:
        print(item + "\n")
