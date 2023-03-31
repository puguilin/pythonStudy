# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/30 9:02
# @Author  : pgl
# @File    : 02_环状饼图.py
# @IDE     : PyCharm


import matplotlib.pyplot as plt


# 定义饼状图的标签，标签是列表
values = [20, 56, 90, 150, 203, 203]
# 绘制饼图
# 创建画布并设置大小
plt.figure(figsize=(9, 9))
# 为饼图添加标题
plt.title('某院校食堂每日出售食品饼图', fontdict={'fontsize': 24, 'color': 'r'}, y=1.05)
# 为饼图设置标签
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签设置
labels = ['冒菜', '麻辣烫', '鸡腿饭', '牛肉面', '汉堡', '鸡架拌饭']
explode = (0.02, 0.03, 0.04, 0.05, 0.06, 0.07)

plt.pie(
    values,  # 数据
    autopct='%1.1f%%',  # 百分比 设置百分比的格式，这里保留一位小数
    textprops={'fontsize': 12, 'color': 'b'},  # 文本属性。字体大小 字体颜色。默认值为None。
    labels=labels,  # 为每个饼图设置标签名称
    radius=1.5,  # 设置饼图的半径
    # explode=(0.02, 0.03, 0.04, 0.05, 0.06, 0.07),  # 设置饼块分离间距大小 每一块分割出的间隙大小
    shadow=True,  # 饼块分离阴影
    startangle=180,  # 饼块起始角度
    counterclock=False,  # 角度是否逆时针旋转。布尔值。默认值为True
    # pctdistance=1.1,    # 饼块内标签与圆心的距离 若果没有则在饼块内显示
    labeldistance=1.2  # 饼块外标签与圆心的距离。

)
# 为饼图设置图例，Loc 表示边框的位置为左下角，frameon=False 表示去掉图例的边框
plt.rcParams['legend.fontsize'] = 10  # 图例大小

plt.legend(
        loc='lower left',  # 图表的旁边添加一组图例说明   loc =  'upper right' 位于右上角
        # bbox_to_anchor=(0, 0, 0, 1)  # 外边距 上边 右边 下边 左边
        # ncol=2 分两列
        # borderaxespad = 0.3 # 图例的内边距


           )
plt.axis('equal')  # 将横轴纵轴的坐标值设为等同

plt.show()
