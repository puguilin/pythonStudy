# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:54
# @Author  : pgl
# @File    : 05_为参数设置默认值.py.py
# @IDE     : PyCharm


# 为参数设置默认值
# def functionname(...,[parameter1 = defaultvalue1]):[functionbody]
# def 函数名称(...,参数列表用','进行分隔, 如果参数没有指定就使用参数的默认值, 参数的默认值都要放在所有参数的最后面,不然会产生语法错误):功能题
def fun_bmi(height, weight, persion='路人'):
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
fun_bmi(height=1.60, weight=50)  # 这里的persion使用的默认值"路人甲", 如果调用的时候指定了这个值, 就使用默认值


# 如果我们不知道参数的默认值可以使用下面函数看到Python自动设置的默认值
# print(fun_bmi.__defaults__)    # 输出一个元组("路人"),元组中包含一个元素'路人', 这个路人就是函数的默认值

# 目前位置我们为参数设置默认值的时候采用的都是不可变对象, 如果使用的是可变对象下面展示
def demo(obj=[]):  # 定义函数并为参数设置默认值:一个空的列表
    print("obj的值: ", obj)  # 在函数体重输出这个参数,obj
    obj.append(1)  # 为列表添加一个值为1的元素


demo()  # 调用这个参数, 不指定参数值,使用它的默认值
demo()  # 再次调用这个参数, 同样不指定参数值, 联系两次调用这个参数的默认值,就会看到参数的默认值发生改变, 为了防止这种情况发生, 尝试使用none值作为默认参数


def demo1(obj1=None):
    if obj1 == None:
        obj1 = []
    print("obj1的值: ", obj1)
    obj1 = []


demo1()  # 两次输出的obj1都是none
demo1()
