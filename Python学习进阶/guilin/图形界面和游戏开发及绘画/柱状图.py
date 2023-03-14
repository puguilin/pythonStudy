# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/22 11:13
# @Author  : pgl
# @File    : 柱状图.py.py
# @IDE     : PyCharm


import xlrd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

bar = Bar()
"""
x=["浑南", "沈北", "苏家屯", "辽中", "新民","康平", "法库"]
y1=[5, 12, 18, 7, 15, 7, 9,10]
bar.add_xaxis(x)
bar.add_yaxis("10月21日降雨量", y1,itemstyle_opts = opts.ItemStyleOpts(color = "#106473"))
"""

# execl文件读取方法
filename = "沈阳常规气象站年降水量（1951-2019）.xlsx"
book = xlrd.open_workbook(filename)
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
# print('表格总行数',nrows)
ncols = sheet1.ncols
# print('表格总列数',ncols)

row1_values = sheet1.row_values(0)

# print('第1行值',row1_values)
col1_values = sheet1.col_values(colx=0, start_rowx=1)
# print('第1列值',col1_values)
x = col1_values
col2_values = sheet1.col_values(colx=1, start_rowx=1)
col3_values = sheet1.col_values(colx=2, start_rowx=1)
# print('第2列值',col2_values)

y1 = col2_values
y2 = col3_values

'''
#逐项例举法
bar.add_xaxis(x)
bar.add_yaxis("年降雨量", y1,itemstyle_opts = opts.ItemStyleOpts(color = "#106473"))
'''

# 链式写法
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))  # LIGHT
        .add_xaxis(x)
        .add_yaxis("浑南降雨量", y1)
        .add_yaxis("新民降雨量", y2)
        # 下行的设置 与+6的设置方法相同，增加了更详细的参数
        .set_global_opts(title_opts=opts.TitleOpts(title="降雨量", subtitle="mm"))

)

# 标注标题、放大滑块
bar.set_global_opts(title_opts=opts.TitleOpts(title="年降雨量", subtitle="mm",
                                              title_link="https://www.baidu.com",
                                              pos_left='center'),
                    xaxis_opts=opts.AxisOpts(name_rotate=90),
                    datazoom_opts=opts.DataZoomOpts(is_show=True),
                    legend_opts=opts.LegendOpts(pos_left="right"), )

# 标注最大值和最小值
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False), markpoint_opts=opts.MarkPointOpts(
    data=[opts.MarkPointItem(type_="max", name="最大值"),
          opts.MarkPointItem(type_="min", name="最小值"),
          ]))

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("bar.html")
bar.render_notebook()

