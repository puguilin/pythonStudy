# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:50
# @Author  : pgl
# @File    : 03_位置参数.py.py
# @IDE     : PyCharm

# 位置参数
# 位置参数就是必须按照定义时的个数和顺序进行参数传递, 也称必备参数.
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
    if 18.5 <= bmi < 24.9:
        print("体重正好,请基础保持")
    if 24.9 <= bmi < 29.9:
        print("您的体重过重")
    if bmi >= 29.9:
        print("肥胖")


# 调用函数, 这里使用的就是位置参数,第一个指定的参数是姓名,第二个指定的参数是身高,第三个指定的参数是体重
# 如果传递的参数个数过多.过少都报错
# 如果参数的个数符合,但是顺序混淆有可能数据类型不匹配出现数据异常报错
fun_bmi("路人甲", 1.83, 60)
fun_bmi("路人乙", 1.60, 50)
