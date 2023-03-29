# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 16:26
# @Author  : pgl
# @File    : 04_水平交错条形图.py
# @IDE     : PyCharm

# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np

# 构建数据
Y2016 = [15600, 12700, 11300, 4270, 3620]
Y2017 = [17400, 14800, 12000, 5200, 4020]
labels = ['北京', '上海', '香港', '深圳', '广州']
bar_width = 0.35

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ["KaiTi"]
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.bar(np.arange(5), Y2016, label='2016', color='steelblue', alpha=0.8, width=bar_width)
plt.bar(np.arange(5) + bar_width, Y2017, label='2017', color='indianred', alpha=0.8, width=bar_width)
# 添加轴标签
plt.xlabel('Top5城市')
plt.ylabel('家庭数量')
# 添加标题
plt.title('亿万财富家庭数Top5城市分布')
# 添加刻度标签
plt.xticks(np.arange(5) + bar_width, labels)
# 设置Y轴的刻度范围
plt.ylim([2500, 19000])

# 为每个条形图添加数值标签距离
for x2016, y2016 in enumerate(Y2016):
    plt.text(x2016 - 0.2, y2016 + 100, '%s' % y2016)

for x2017, y2017 in enumerate(Y2017):
    plt.text(x2017 + bar_width - 0.2, y2017 + 100, '%s' % y2017)
# 显示图例
plt.legend()
# 显示图形
plt.show()
