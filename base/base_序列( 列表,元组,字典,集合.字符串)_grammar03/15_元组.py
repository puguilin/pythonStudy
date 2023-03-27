# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:33
# @Author  : pgl
# @File    : 15_元组.py.py
# @IDE     : PyCharm


# 元组
# 元组和列表比较类似可以放置各种类型的数据(整数, 实数, 布尔值, 字符串, 序列, 对象), 但是元组是不可变的, 不能随便更改元组中的内容
# 元组: (), 两个相邻元素采用,分割(元组1, 元组2...元组n)
# 1.元组的创建和删除
# 2.访问元组中的元素
# 3.修改元组元素
# 4.元组推导式
# 5.元组和列表的区别

# 1.元组的创建和删除
# 1.1使用赋值运算符直接创建元组
# 1.2创建空元组
# 1.3创建数值元组

# 1.1使用赋值运算符直接创建元组
# 语法: tuplename = (元素1, 元素2,...,元素n)
number = (7, 14, 21, 28, 35, 42)  # 创建数值类型元组
print(" 定义创建数值类型元组 " + str(number))
zifu = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")  # 创建字符串类型元组
print("创建字符串类型元组 " + str(zifu))
# 在列表中可以创建混合类型的列表, 在元组中也可以定义混合类型的元组
nutile = ("嘿嘿呦嘿嘿", 15, ("人生苦短", "我用Python"), ["爬虫", "云计算", "游戏"])  # 混合类型的元组, 字符串,整型,元组,列表(列表中是字符串)
print(" 混合类型的元组 " + str(nutile))
verse = "一片冰心在玉壶"  # 定义值包括一个元素的元组, 其实是字符串,不是元组, 这个()就不是起到定义元组的作用只是依次连接的作用
print(verse, "的数据类型是:", type(verse))
# 真正创建只有一个元素的元组 需要注意的一点是，当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,，否则 Python 解释器会将它视为字符串
verse1 = ("一片冰心在玉壶",)  # 定义值包括一个元素的元组, 其实是字符串,不是元组, 这个()就不是起到定义元组的作用只是依次连接的作用
print(verse1, "真正只有一个元素的元组: 注意 当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,", type(verse1))

coffeename = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', "麝香猫", "哥伦比亚")  # 直接定义一个元组
print("直接定义一个字符元组 " + str(coffeename))

# 1.2创建空元组, 主要为函数传递空值或者是返回空值
emptytuple = ()
print("创建一个空元组: ", emptytuple)

# 1.3创建数值元组,通过tuple()函数转换
tuple1 = tuple(range(2, 21, 2))  # 起始值是2,结束值是21,步长是2
print("通过puple()函数创建数值元组: ", tuple1)

# 2.其他类型数据转化为元组

# 2.1.将字符串转换成元组
tup1 = tuple("hello")
print("将字符串转换成元组 " + str(tup1))
# 2.2.将列表转换成元组
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print("将列表转换成元组 " + str(tup2))
# 2.3.将字典转换成元组
dict1 = {"Name": "JYH", "Age": 18}

print("将字典转换成元组获取key: " + str(tuple(dict1)))
print("将字典转换成元组获取values: " + str(tuple(dict1.values())))

# 2.4.将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
print("将区间tuple(range(1, 6))转换成元组 " + str(tup4))

# 2.del()语句删除元组
# del (name)
name = ("2021年",)
print(name)
del name
# print(name)    # 这次会报错,因为name已经被del语句删除了
