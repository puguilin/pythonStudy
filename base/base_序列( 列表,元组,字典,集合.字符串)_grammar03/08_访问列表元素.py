# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:04
# @Author  : pgl
# @File    : 08_访问列表元素.py.py
# @IDE     : PyCharm


# 访问列表元素
# 访问列表元素就是获取列表的内容, 主要有3种方法,
# 1. 直接使用print()函数输出
# 2. 索引来获取指定位置的元素
# 3. 通过切片获取部分元素

python = ["Python", 28, "人生苦短", ["爬虫", "自动化运维", "云计算", "web开发"]]  # 定义一个列表,列表中的元素 [字符串类型, 整型, 字符串,[列表]]
print(python)
# 如果想获取"人生苦短", 索引值是2, 从结果中可以看出通过索引值获取指定的元素如果这个元素是字符串内容的, 它输出的时候不包括左右的",只输出字符串
print("通过索引值为2 的 访问元素" + python[2])

# 通过切片来访问指定范围的列表, 从索引值起始值为1和索引值为2的元素, 因为不包括结束值就是2+1=3
print("通过切片python[1:3] 索引值从1到2 不包括索引值为3的 （左闭右开）来访问指定范围的列表  " + str(python[1:3]))

# 从指定的范围的列表中找出某个值(object)第一匹配的索引值
list1 = ['name', 'age', 'address']
index = list1.index('address')
print("找出从列表中匹配指定的值 第一次出现的索引值 " + str(index))
# 输出每日一帖
# 今天星期一: 坚持下去不是因为我很坚强, 而是因为我别无选择!(根据当前的星期, 输出不同的文字)

import datetime  # 先导入日期时间类

mot = ["今天星期一: \n坚持下去不是因为我很坚强,而是因为我别无选择.",
       "今天星期二: \n含泪播种的人一定能笑着收获",
       "今天星期三: \n做对的事情比把事情做对更重要",
       "今天星期四: \n命运给予我们的不是失望之酒, 而是希望之杯",
       "今天星期五: \n不要等到明天, 明天太遥远, 今天就行动",
       "今天星期六: \n求知若饥, 虚心若愚",
       "今天星期日: \n成功将属于哪些从不说'不可能'的人"
       ]
day = datetime.datetime.now().weekday()  # 获取当前的星期
print("输出day: ", day)
print(mot[day])  # mot[day],我们把当前星期作为索引值获取内容

# 看一下现在的时间: datetime.datetime.now()
# 看一下现在的年份: datetime.datetime.now().year
# 看一下现在的月份,只有月份: datetime.datetime.now().month
day1 = datetime.datetime.now().year
print(day1)
