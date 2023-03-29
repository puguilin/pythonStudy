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


'''

2. 修改折线样式和宽度
修改折线样式 linestyle = ‘-’
以下四种常用
直线 linestyle = '-'或省略
破折线 linestyle = '–'或linestyle = ‘dashed’
点划线 linestyle = '-.'或linestyle = ‘dashdot’
虚线 linestyle = '：'或linestyle = ‘dotted’
修改折线颜色color=‘颜色英文或其首字母’
color=‘r’ == color=‘red’

3. 修改点坐标的样式
修改折线样式 marker=‘o’
以下六种常用
圆圈 marker=‘o’
五角星 marker=‘*’
三角形 marker=‘^’
倒三角形 marker=‘v’
叉号 marker=‘x’
加号 marker=‘+’

4. 添加并修改标题和标签字体大小和颜色
添加标题 plt.title()
字体大小 fontsize=num
字体颜色 color=‘str’
调用字体样式fontdict=c_dict # c_dict 为字典样式colors={“color”:“y”,“size”:10}


添加网格 plt.grid()
只显示垂直网格线 plt.grid(axis=‘x’)
只显示水平网格线 plt.grid(axis=‘y’)
网格样式 linestyle=‘-’ 和折线样式相同常用这四种：
直线 linestyle = ‘-’ 或省略
破折线 linestyle = ‘–’ 或 linestyle = ‘dashed’
点划线 linestyle = ‘-.’ 或 linestyle = ‘dashdot’
虚线 linestyle = ‘：’ 或 linestyle = ‘dotted’
网格线宽度linewidth=num


'''
# 选择字体显示中文
plt.rcParams['font.family'] = ['Microsoft YaHei']
# 定义坐标数据
x = [1, 4, 8, 12]
y = [9, 4, 7, 2]

# 传入数据
plt.plot(x, y, linestyle='dashed', color='g', marker='o')

# 添加折线点的值
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', color='r', va='bottom', fontsize=20)
# 添加标题
plt.title("第一张表,加坐标和颜色", color='r', fontsize=15)
# 添加网格
plt.grid()
# 调整图与y的边距
plt.margins(0.05)
# 添加X轴标签
plt.xlabel(u"Hyperparameter C")
# 添加Y轴标签
plt.ylabel("Accuracy%")
# 总标题
plt.suptitle("折线图示例", color='r', fontsize=15)
# 绘图
plt.show()

