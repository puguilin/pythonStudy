# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:28
# @Author  : pgl
# @File    : 12_对列表进行排序.py.py
# @IDE     : PyCharm

# 对列表进行排序
# 在Python中有升序和降序两种排序方法
# 1.使用列表对象的sort()方法   原列表的元素顺序改变.
# 2.使用内置的sorted()函数    排序后原列表的元素顺序不变

# 使用sort()方法实现排序后, 原列表的元素顺序改变.
# listname(列表名称).sort(key=None, reverse=False)  reverse指定是升序还是降序排列, False代表升序排列, True是降序排列
grade = [96, 99, 89, 79, 97, 63, 100, 94, 100]  # 保存成绩的列表
print("原列表: ", grade)
grade.sort()  # 进行升序排列, sort()的默认值就是升序
print("升序排列的结果: ", grade)
grade.sort(reverse=True)
print("降序排列的结果: ", grade)

# 对字符串列表进行排序,按照abcde...
char = ["cat", "Tom", "pet", 'dog']  # 定义一个字符串列表
char.sort(reverse=False)  # 进行升序排列, 不设置reverse则默认升序排列, 不设置key则默认区分大小写
print("字符串升序:", char)
char.sort(reverse=True)  # 进行降序排列
print("字符串降序:", char)
# 如果换成中文汉字则不能进行排序(方法比较复杂)

# 使用sorted()函数实现排序后原列表的元素顺序不变
# sorted(iterable,key=None,reverse=False), iterable表示列表名称, reverse是规定升序还是降序
char2 = ["dog", "cat", "Pig", "pet"]
char2_1 = sorted(char2)  # 定义一个新的列表char2_1用来存储新的排序结果, 不设置key则默认区分大小写,不设置reserve则默认升序
print("sorted升序结果: ", char2_1)
char2_2 = sorted(char2, reverse=True)  # reverse = True 则是降序
print("sorted降序结果: ", char2_2)
print("原列表内容: ", char2, "可见原列表结果没有改变")
