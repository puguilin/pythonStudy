# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:37
# @Author  : pgl
# @File    : 16_访问元组元素.py.py
# @IDE     : PyCharm


# 访问元组元素
# 访问元组元素就是获取元组内容, 通常有3种方法
# 1.直接使用print()函数输出
# 2.索引来输出, 一次只能输出一个内容
# 3.通过切片来输出, 可以输出一个也可以输出多个,根据指定的值来输出

# 1.直接使用print()函数输出

untile = ("Python", 28, ("人生苦短", "我用Python"), ["爬虫", "云计算", "游戏"])
print(untile)
untile[1]  # 从0开始数, 1是第二个元素, 输出值是 28
print(untile[1])
untile[1:3]  # 1:3, 有1,2连个元素, 切片选取的时候是第2第3一共两个元素
print(untile[1:3])

coffeename = ("蓝山", "卡布奇诺", "曼特宁", "麝香猫", "哥伦比亚")  # 定义一个字符元组
print("您好, 欢迎光临~伊米卡米~\n\n我店有: \n")  # \n换行作用
for name in coffeename:
    print(name + "咖啡", end=" ")
# print(,end"")用法
# 1.设置end=' '时，print()输出不换行，以空格结尾。
# 2.设置end=''时，print()输出不换行，以无字符结尾。
# 3.设置end='*'时，print()输出不换行，以*结尾。


print("分两列显示2017~2018赛季NBA西部联赛前八名球队。")
team = ("火箭", "勇士", "开拓者", "雷霆", "爵士", "鹈鹕", "马刺", "森林狼")  # 定义一个元组
# 下面通过for循环和enumerate()函数遍历这个元组,实现分两列输出
for index, item in enumerate(team):  # for关键字, 索引的变量index, 球队的名称item, in关键字, 函数名称enumerate(),参数是元组team
    # 因为要通过两行输出, 所以要进行索引判断, 看元素能否被2整除
    if index % 2 == 0:  # 如果能被2整除, 不换行输出
        print(item + "\t\t\t\t", end=" ")  # 不换行输出
    else:
        print(item + "\n")  # 换行输出

# for index,item in enumerate(listname):
# 输出index和item
# 参数说明：
# index：用于保存元素的索引
# item：用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可。
# listname:列表名称。
team = [521, 477, "你好", "热爱和平"]
for index, item in enumerate(team):
    print(index + 1, item)
