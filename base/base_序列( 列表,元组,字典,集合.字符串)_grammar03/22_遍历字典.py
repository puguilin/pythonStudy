# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:42
# @Author  : pgl
# @File    : 22_遍历字典.py.py
# @IDE     : PyCharm


# 遍历字典
# 遍历:对所有的内容进行一遍访问,对于字典以键值对的形式存储数据,所以可能用到获取这些键值对,Python提供的遍历字典的方法:items
sign = {'绮梦': '水瓶座', '冷伊一': '射手座', '香凝': '双鱼座', '黛兰': '双子座'}  # 首先定义一个字典
sign.items()  # 返回的是一个可以遍历的列表,每一个列表的元素都是一个元组
print("看一下输出结果法1: ", sign.items())
for item in sign.items():
    print("看一下输出结果方法2:", item)  # 就是每一个循环中都会带一个"看一下输出结果方法2:"

# 如果我们不想得到元组的形式(),想要得到每个键和具体的值的时候:
for key, value in sign.items():
    print("不想要元组形式的输出结果值:", key, "的星座是:", value)

# 得到字典中的键列表,或者是值列表
for key in sign.keys():
    print(key)  # 得到字典中的键列表
print('\n')  # 仅仅起一个分隔的作用
for value in sign.values():
    print(value)  # 得到字典中的值列表
