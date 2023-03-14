# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:18
# @Author  : pgl
# @File    : 34_字母大小写转换.py.py
# @IDE     : PyCharm

# 字母大小写转换
# 1.大写字母转小写字母  ABC -->  abc  使用lower()转换
# 2.小写字母转大写字母  abc --> ABC 使用upper()转换
str1 = "WWW.MingriSoft.com"
print("把str1中的大写字母转化为小写字母:", str1.lower())
print("把str1中的小写字母转化为大写字母:", str1.upper())

# 场景模拟
username_1 = "|MingMi|mr|minrisoft|MRSoft|WGH"  # 已经存在的用户名
username_2 = username_1.lower()  # 全部转化为小写字母
regname_1 = input("输入要注册的会员名称: ")  # 输入会员名称
regname_2 = "|" + regname_1.lower() + "|"  # 输入的会员名称转换为小写
if regname_2 in username_2:
    print(regname_2, "已经存在")
else:
    print(regname_2, "可以注册")
