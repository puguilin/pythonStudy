# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:45
# @Author  : pgl
# @File    : 26_集合的添加和删除.py.py
# @IDE     : PyCharm

# 集合的添加和删除
# 由于集合是可变序列,所以可以向集合中添加或者元素
# 1.向集合中添加元素 add()
# setname.add(element)
# 集合名称.add(添加元素),添加元素不能是列表.元组等可迭代对象
mr = set(["零基础学Java", "零基础学Android", "零基础学C语言", "零基础学PHP"])  # 定义一个集合
mr.add("零基础学Python")
print("添加'零基础学Python'之后的结果", mr)
mr.add("零基础学Python")
print("添加原来集合中有的元素之后的结果", mr)  # 不能添加重复的元素

# 2.从集合中删除元素
# 2.1 remove()删除指定元素
# 2.2 pop()随机删除一个元素
# 2.3 clear()删除所有元素,可以把集合清空
nr = set(["零基础学Java", "零基础学Android", "零基础学C语言", "零基础学PHP"])
nr.remove("零基础学Java")
print("删除'零基础学Java'之后的结果", nr)
print('\n')
# 删除集合中不存在的元素就会报错
# nr.remove("零基础学PHP")
# 在删除元素的时候可以进行if语句的判断
if "零基础学PHP" in nr:
    nr.remove("零基础学PHP")
else:
    print("'零基础学PHP不在nr这个集合中'")
print("'零基础学PHP'在nr这个集合中,删除后的结果是:", nr)

set1 = set(["零基础学Java", "零基础学Android", "零基础学C语言", "零基础学PHP"])
de = set1.pop()  # 在集合set1中随机删除一个元素
print("看下删除的元素:", de)
print("随机删除后的结果:", set1)

# clear方法会删除集合中所有元素,使这个集合成为一个空的集合
set1.clear()  # 清空集合
print("clear集合之后的结果:", set1)
# del删除之后这个集合就不存在了, 就不是空集合了

print('\n', "情景模拟")
# 情景模拟
python = set(['绮梦', '冷伊一', '香凝', '梓轩'])
c = set(['冷伊一', '凌宇', '梓轩', '盛博'])
python.add("凌宇")  # 添加一个元素
c.remove("凌宇")  # 删除一个元素
print("选择Python的学生名字:", python)
print("选择c语言的名字:", c)
