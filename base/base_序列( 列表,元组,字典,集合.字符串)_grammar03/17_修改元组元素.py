# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:38
# @Author  : pgl
# @File    : 17_修改元组元素.py.py
# @IDE     : PyCharm


# 修改元组元素, 使用索引修改元组元素
coffeename = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '麝香猫', '哥伦比亚')
# coffeename[4] = "拿铁"    这样写会报错, 因为元组是不可修改序列,不能对其单个元素进行修改
# print(coffeename)
# 1.对整个元组重新赋值
coffeename = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '麝香猫', '哥伦比亚')
coffeename = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '拿铁', '哥伦比亚')
print(coffeename)

# 2.还可以队员组进行连接组合
coffeename1 = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '麝香猫', '哥伦比亚')
coffeename1 = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '拿铁', '哥伦比亚')  # 对上面元组进行重新赋值,删除'麝香猫'
newcoffeename = ('麝香猫', '维也纳')  # 定义一个新的元组用来元组重组
allcoffeename = coffeename1 + newcoffeename  # 我们可以进行元组的相加, 但是不能是元组和字符串相加
print(allcoffeename)
# 我们可以进行元组的相加, 但是不能是元组和字符串相加
# print("合并后的:"+allcoffeename)    这样就会报错


