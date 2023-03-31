# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/30 8:47
# @Author  : pgl
# @File    : 01_简单饼图.py
# @IDE     : PyCharm


import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'

x = [1, 5, 4, 3, 2]
labels = ["小明", "小红", "张三", "李四", "王五"]
# explode = [-0.1, 0, 0.1, 0.1, 0]
colors = ['r', 'b']

plt.pie(x,
        labels=labels, labeldistance=1.2, rotatelabels=True,  # 外标签相关属性
        autopct='%1.1f%%', pctdistance=0.4, startangle=30,  # 内标签相关属性，起始角度设置为30
        # explode=explode, colors=colors, shadow=True,  # 饼块分离、颜色循环、阴影
        radius=1.2, counterclock=False,  # 修改饼图半径、角度顺时针旋转

        )

plt.title('饼图标题')

plt.show()

'''
pie()函数的参数如下：

x：各个饼块的尺寸。类1维数组结构。
explode：每个饼块相对于饼圆半径的偏移距离，取值为小数。类1维数组结构。默认值为None。
labels：每个饼块的标签。字符串列表。默认值为None。
colors：每个冰块的颜色。类数组结构。**颜色会循环使用。**默认值为None，使用当前色彩循环。
autopct：饼块内标签。None或字符串或可调用对象。默认值为None。如果值为格式字符串，标签将被格式化，如果值为函数，将被直接调用。
pctdistance：饼块内标签与圆心的距离。浮点数。默认值为0.6，autopct不为None该参数生效。
shadow：饼图下是否有阴影。布尔值。默认值为False。
labeldistance：饼块外标签与圆心的距离。浮点值或None。默认值为1.1。如果设置为None，标签不会显示，但是图例可以使用标签。
startangle：饼块起始角度。浮点数。默认值为0，即从x轴开始。角度逆时针旋转。
radius：饼图半径。浮点数。默认值为1.
counterclock：角度是否逆时针旋转。布尔值。默认值为True。
wedgeprops：饼块属性。字典。默认值为None。具体见matplotlib.patches.Wedge 。
textprops：文本属性。字典。默认值为None。
center：饼图中心坐标。(float,float)浮点数二元组。默认值为(0,0)。
frame：是否绘制子图边框。布尔值。默认为False。
rotatelabels：饼块外标签是否按饼块角度旋转。布尔值。默认为False。
normalize：是否归一化。布尔值或None。默认值为None。
True：完全饼图，对x进行归一化，sum(x)==1。
False：如果sum(x)<=1，绘制不完全饼图。如果sum(x)>1，抛出ValueError异常。
None：如果sum(x)>=1，默认值为True。如果sum(x)<1，默认值为False。
注意：未来版本（当前版本3.3.3），默认值将改为True。绘制不完全饼图，需要明确传递normalize=False。

'''