# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 16:35
# @Author  : pgl
# @File    : 02_折线图对比.py
# @IDE     : PyCharm


from matplotlib import pyplot as plt
# 添加网格
# 选择字体显示中文
plt.rcParams['font.family'] = ['Microsoft YaHei']
# 定义坐标数据
x = [1, 4, 8, 12]
y = [9, 4, 7, 2]
# 第一张表  当有多个图表是才加上这个
plt.subplot(2, 2, 1)
# 传入数据
plt.plot(x, y, color='g', marker='o')
# 添加折线点的值
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', color='r', va='bottom', fontsize=10)
# 添加标题
plt.title("第一张表,加坐标和颜色", color='r', fontsize=15)
# 添加网格
plt.grid()
# 第二张表 当有多个图表是才加上这个
plt.subplot(2, 2, 2)
plt.plot(x, y)
# 添加折线点的值
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', color='r', va='bottom', fontsize=10)
plt.title("垂直网格线,2宽", color='r', fontsize=15)
# 添加竖网格线
plt.grid(axis='x', linewidth=2)
# 第三张表 当有多个图表是才加上这个
plt.subplot(2, 2, 3)
plt.plot(x, y)
# 添加折线点的值
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', color='r', va='bottom', fontsize=10)
plt.title("水平网格线,破折线,4宽", color='r', fontsize=15)
# 添加水平网格虚线
plt.grid(axis='y', linestyle='--', linewidth=4)
# 第四张表 当有多个图表是才加上这个
plt.subplot(2, 2, 4)
plt.plot(x, y)
# 添加折线点的值
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', color='r', va='bottom', fontsize=10)
plt.title("蓝色虚线网格线", color='r', fontsize=15)
# 添加虚网格线
plt.grid(color='b', linestyle=':')
# 总标题
plt.suptitle("网格对比", color='r', fontsize=15)
# 绘图
plt.show()
