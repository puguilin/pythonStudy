# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 8:59
# @Author  : pgl
# @File    : 01_loc函数.py
# @IDE     : PyCharm


import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1'],
    ['back', 'xxl', 16, 'class3'],
    ['yellow', 'Ml', 20, 'class5'],
])
print(df)
# 数据集为以下内容，所有操作均对df进行
'''

        0    1     2       3
0   green    M  10.1  class1
1     red    L  13.5  class2
2    blue   XL  15.3  class1
3    back  xxl  16.0  class3
4  yellow   Ml  20.0  class5

'''
# 获取第0行及之后的行，df的全部数据
print(" df[0:] 获取第0行及之后的行，df的全部数据 结果是：  \n")
print(df[0:])
# 获取第3行之前的数据不包含第三行 左开右闭
print("df[:2] 获取第3行之前的数据不包含第三行（获取前两行） 左闭右开 结果是：  \n")
print(df[:2])
# 获取第0行
print("df[0:1] 获取第0行 结果是：  \n")
print(df[0:1])
# 获取第2行到第3行（不含第4行）
print("df[1:3] 获取第2行到第3行（不含第4行） 结果是：  \n")
print(df[1:3])
# 获取最后一行
print("df[-1:] 获取最后一行 结果是：  \n")
print(df[-1:])
# 获取倒数第3行和倒数第2行,因为没有-0,所以没有最后一行
print("df[-3:-1] 获取倒数第3行和倒数第2行,因为没有-0,所以没有最后一行 结果是：  \n")
print(df[-3:-1])

df.loc[df[1] == 'M', 2] = 10.2

print(" loc[df[1] == 'M', 2] 根据匹配的列值改变满足条件的行信息 结果是：  \n")
print(df)
'''
loc函数主要通过行标签索引行数据，划重点，标签！标签！标签！
loc[1] 选择行标签是1的（从0、1、2、3这几个行标签中）

'''
print("loc[1] 选择行标签是1的 索引行数据 即取 取第一 行数据 \n " + str(df.loc[1]))  # red   L  13.5  class2

'''
loc[0:1] 和 loc[0,1]的区别 
loc[0:1]  ：表示获取的是行记录
loc[0,1]  , 表示获取的是列信息
loc[]中的数字其实是行索引，所以算是前闭加后闭
ilocloc[]中的数字其实是行索引，所以算是前闭加后开
获取取第一和第二行，
'''
print(" loc[0:1] 获取取第一行和第二行 标签（：表示获取的是行记录  0:1 表示索引从0 开始获取两列 ）  \n" + str(df.loc[0:1]))  # 取第一和第二行，loc[]中的数字其实是行索引 左闭右闭

print(" iloc[0:1] 获取第一行数据  序列  \n" + str(df.iloc[0:1]))

print(" loc[0,1] 获取第一行第二列的数据值（ , 表示获取的是列信息 相当于是单元格） loc[0,1]  \n" + str(df.loc[0, 1]))

'''
获取索引某两列数据，loc[:,0:1]，还是标签，注意，如果列标签是个字符，比如'a'，loc['a']是不行的，必须为loc[:，'a']。
但如果行标签是'a',选取这一行，用loc['a']是可以的。

'''
print("loc[:,0:1] 获取索引某两列数据，（ , 表示获取的是列信息  0:1 表示索引从0 开始获取两列 ） \n" + str(df.loc[:, 0:1]))
