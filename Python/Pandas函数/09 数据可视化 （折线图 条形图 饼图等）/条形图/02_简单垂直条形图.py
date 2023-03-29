# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 16:15
# @Author  : pgl
# @File    : 02_简单垂直条形图.py
# @IDE     : PyCharm

# 导入模块
import matplotlib.pyplot as plt

# 构建数据
GDP = [12406.8, 13908.57, 9386.87, 9143.64]
# 中文乱码处理
plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams['axes.unicode_minus'] = False
# 绘图  bar 垂直条形图
plt.bar(range(4), GDP, align="center", color="steelblue", alpha=0.6)

# 添加y轴标签
plt.ylabel("GDP")
# 设置Y轴的刻度范围
plt.ylim([4000, 15000])

# 添加x轴刻度标签
plt.xticks(range(4), ['北京市', '上海市', '天津市', '重庆市'])

# 添加标题
plt.title('四个直辖市GDP大比拼')


# 为每个条形图添加数值标签
for x, y in enumerate(GDP):
    plt.text(x, y + 300, '%s' % round(y, 1), ha='center')  # y+300 数值离开 条形图的距离

# 显示图形
plt.show()



