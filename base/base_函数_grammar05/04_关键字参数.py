# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:50
# @Author  : pgl
# @File    : 04_关键字参数.py.py
# @IDE     : PyCharm

# 关键字参数
# 关键字参数是指使用形式参数的名字来确定输入的参数值, 这样就不用与形式参数的位置一致了, 只要把参数名字写正确就可以了

def fun_bmi(persion, height, weight):
    '''
    功能: 根据身高和体重计算BMI指数
    persion: 姓名
    height: 身高    单位:米
    weight: 体重    单位:千克
    '''
    print(persion + "的身高:" + str(height) + "米 \t 体重:" + str(weight) + "千克")
    bmi = weight / (height * height)  # 用于计算BMI指数, 公式为"体重/身高的平方"
    print("您的BMI指数为: " + str(bmi))
    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻")
    if bmi >= 18.5 and bmi < 24.9:
        print("体重正好,请基础保持")
    if bmi >= 24.9 and bmi < 29.9:
        print("您的体重过重")
    if bmi >= 29.9:
        print("肥胖")


# 这里使用关键字参数进行调用

fun_bmi(persion="路人甲", height=1.60, weight=50)  # 如果使用关键字参数参数进行调用必须全部使用关键字参数, 不能位置参数与关键字参数混淆使用

fun_bmi(persion="路人乙", weight=60, height=1.56)  # 如果使用关键字参数参数进行调用必须全部使用关键字参数, 不能位置参数与关键字参数混淆使用
