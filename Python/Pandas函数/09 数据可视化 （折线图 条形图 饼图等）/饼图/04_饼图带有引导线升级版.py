# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/30 16:32
# @Author  : pgl
# @File    : 04_饼图带有引导线升级版.py
# @IDE     : PyCharm


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 定义饼状图的标签，标签是列表
values = [20, 56, 90, 120, 160, 203]
# 绘制饼图
# 创建画布并设置大小
plt.figure(figsize=(9, 9))
# 为饼图添加标题
plt.title('某院校食堂每日出售食品饼图', fontdict={'fontsize': 24, 'color': 'r'}, y=1.05)
# 为饼图设置标签
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签设置
labels = ['冒菜', '麻辣烫', '鸡腿饭', '牛肉面', '汉堡', '鸡架拌饭']
explode = (0.02, 0.03, 0.04, 0.05, 0.06, 0.07)

# 绘制圆环图目的是为了显示引导线 这个要放在下面plt.pie()这个参数的前面
wedges, texts = plt.pie(
    values,
    wedgeprops={"width": 0.5},
)


# 这里才是饼图参数的设置
plt.pie(
    values,
    autopct='%1.1f%%',  # 百分比 设置百分比的格式，这里保留一位小数
    textprops={'fontsize': 12, 'color': 'b'},  # 文本属性。字体大小 字体颜色。默认值为None。
    labels=labels,  # 为每个饼图设置标签名称
    radius=1.1,  # 设置饼图的半径
    # explode=(0.02, 0.03, 0.04, 0.05, 0.06, 0.07),  # 设置饼块分离间距大小 每一块分割出的间隙大小
    shadow=True,  # 饼块分离阴影
    # startangle=0,  # 饼块起始角度
    # counterclock=False,  # 角度是否逆时针旋转。布尔值。默认值为True
    # pctdistance=1.1,    # 饼块内标签与圆心的距离 若果没有则在饼块内显示
    # labeldistance=1.2  # 饼块外标签与圆心的距离。

)


# 构造annotate函数的**kwargs参数，设置引导线线型
data = dict(zip(labels, values))
data = pd.DataFrame([data])
print(data)
print(data.iloc[0])
kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")
# 遍历饼块绘制注释标签和引导线
for i, p in enumerate(wedges):
    # 根据matplotlib.patches.Wedge对象的theta1和theta2参数计算饼块均分点的角度
    ang = (p.theta2 - p.theta1) / 1.0 + p.theta1
    # 根据角度的弧度计算 饼块均分点的坐标（引导线的起点）
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    # print(p.theta1, p.theta2, ang, np.deg2rad(ang), x, y)
    # 演示引导线起点位置
    # plt.plot(x, y, "or")
    # 根据x的值即角度所在象限确定引导线的对齐方式
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    # 设置引导线的连接方式
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    # 绘制注释标签和引导线
    plt.annotate(
        data.columns[i],
        xy=(x, y),  # xy 为被注释的坐标点
        xytext=(1.35 * np.sign(x), 1.4 * y),  # xytext 为注释文字的坐标位置
        horizontalalignment=horizontalalignment,
        color='red',  # color 设置字体颜色

        **kw
    )
'''
s 为注释文本内容


xycoords and textcoords 是坐标xy与xytext的说明
weight 设置字体线型
color 设置字体颜色
arrowprops #箭头参数,参数类型为字典dict
bbox给标题增加外框 

'''
plt.show()
plt.axis('equal')  # 将横轴纵轴的坐标值设为等同
