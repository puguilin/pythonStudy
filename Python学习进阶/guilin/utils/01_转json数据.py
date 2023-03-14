# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 16:54
# @Author  : pgl
# @File    : 01_转json数据.py.py
# @IDE     : PyCharm

import json

# 准备列表，列表内每个元素都是字典，将其转化为JSON
data = [{"name": "张三", "age": "14"}, {"name": "李四", "age": "24"}, {"name": "王五", "age": "45"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# [{"name": "张三", "age": "14"}, {"name": "李四", "age": "24"}, {"name": "王五", "age": "45"}]

# 准备字典，将字典转化为JSON
d = {"name": "刘某", "age": "45"}
json_str1 = json.dumps(d, ensure_ascii=False)
print("----------------------------------------")
print(type(json_str1))
print(json_str1)

# 将JSON转化为Python数据类型
d2 = '[{"name": "张三", "age": "14"}, {"name": "李四", "age": "24"}, {"name": "王五", "age": "45"}]'
l = json.loads(d2)
print(type(l))
print(l)

