# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:03
# @Author  : pgl
# @File    : 31_截取字符串.py.py
# @IDE     : PyCharm

# 截取字符串
# 字符串也属于序列, 在截取字符串的时候也可以采用序列的方式进行
# string[start : end : step]
# 字符串的名称[起始位置(包括): 结束位置(不包括):步长,如果省略默认值为1],在使用切片的时候要知道字符串的索引,从0开始索引
str1 = "人生苦短,我用Python!"
print(str1[2])  # 获取第三个字符,它的索引值为2
print(str1[5:])  # 从第6个字符开始截取,一直到结束
print(str1[:5])  # 从左边开始,省略起始值, 一直截取到第6个元素(截取内容不包括第6个元素)
print(str1[2:5])  # 从第3个元素(包括)到第6个元素(不包括)
print(str1[:5:2])  # 从第1个元素(包括)到第6个元素(不包括),步长为2
print(str1[2::2])  # 只指定第3个字符和步长,可以省略第二个元素但是不能省略:
print(str1[15:])  # 通过切片进行截取,没有这个值是不会报错的
# print(str1[15])    # 直接通过索引没有这个值是会报错的
# 如果不想抛出这样的语句就使用try...except语句进行捕获异常
try:
    print(str1[15])
except IndexError:
    print("索引不存在")

p1 = "你知道我的生日吗?"
print("程序员甲说:", p1)
p2 = "输入你的身份证号码."
print("程序员乙说:", p2)
idcard = "123456199006277879"
print("程序员甲说: ", idcard)
birthday = idcard[6:10] + "年" + idcard[10:12] + "月" + idcard[12:14] + "日"
print("程序员乙说:你是" + birthday + "出生的,所以你的生日是" + birthday[5:])
