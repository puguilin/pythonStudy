# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/22 11:54
# @Author  : pgl
# @File    : 热力图.py.py
# @IDE     : PyCharm


from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

# 基础数据
quxian = ['东川区', '晋宁区', '宜良县', '西山区', '盘龙区', '五华区', '石林彝族自治县', '官渡区', '呈贡区', '安宁市', '寻甸县', '禄劝县', '富民县', '嵩明县']

values3 = [25600, 22721, 20916, 19521.13322632424, 18398.762941176472, 17736.794297352342, 16500.0, 16089.533692722373, 14591.25462962963, 13967.380434782608, 11700.0, 11583.333333333334, 10392.857142857143, 7546.875]

c = (
    Map()
        .add("昆明", [list(z) for z in zip(quxian, values3)], "昆明")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="昆明地区热力图"), visualmap_opts=opts.VisualMapOpts(is_piecewise=True,split_number = 10, max_=30000)

    )
        .render("招聘人数地区热力图.html")
)
# 打开html
# os.system("贵阳.html")