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
#  list.sort(cmp=None, key=None, reverse=False) 和  sorted(iterable, cmp=None, key=None, reverse=False) 理解
# 1.1 使用列表对象的sort()方法   原列表的元素顺序改变.
# 1.2 使用内置的sorted()函数    排序后原列表的元素顺序不变

# 2. 通过key的值来进行数组/字典的排序
# 注意： key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

# 使用sort()方法实现排序后,sort()的默认值就是升序  原列表的元素顺序改变.
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

# 通过key的值来进行数组/字典的升序  key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# 先按照成绩降序排序，相同成绩的按照名字升序排序：

dict_data = [{'no': '30', 'name': 'alice', 'score': 38}, {'no': '05', 'name': 'bob', 'score': 18}, {'no': '26', 'name': 'darl', 'score': 28},
             {'no': '28', 'name': 'christ', 'score': 28}]
dict_sorted = sorted(dict_data, key=lambda x: (-x['score'], x['name']))
print("列表 先按照成绩降序排序，相同成绩的按照名字升序排序 " + str(dict_sorted))

# 列表按照年龄升序排列 x["age"]   降序 -x["age"]
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array_data = sorted(array, key=lambda x: -x["age"])
print("通过key的值来进行数组/字典的升序 按照年龄升序排列 " + str(array_data))
