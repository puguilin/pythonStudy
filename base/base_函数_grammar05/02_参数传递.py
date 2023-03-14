# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:45
# @Author  : pgl
# @File    : 02_参数传递.py.py
# @IDE     : PyCharm


# 参数传递
# 如果把函数比作榨汁机, 那么放入水果就相当于参数传递, 榨汁机可以根据放入的水果榨出不同的水果, 函数可以根据不同的数得出不用的结果
# 函数的参数放在函数名之后的一对"()"中 def 函数名 (函数参数)
# 从5个方面介绍函数的参数传递
# 1. 了解形式参数和实际参数
# 2. 位置参数
# 3. 关键字参数
# 4. 为参数设置默认值
# 5. 可变参数

# 1. 形式参数与实际参数
# 如果把榨汁机比作函数, 那么设置的预留放置水果入口就是形式参数, 实际放入的水果是实际参数
# def demo(obj):    # 这里的obj就是形式参数
#     print(obj)
# mot = "唯有在被追赶的的时候, 你才能真正地奔跑."
# demo(mot)    # 这里的mot就是实际参数
# list1 = ['绮梦','冷伊一','香凝','黛兰']
# demo(list1)    # 这里的list1就是实际参数

# '值传递' 与 '引用传递'
# 值传递:当实际参数为不可变对象时进行的传递, 不改变形式参数的值
# 引用传递:当实际参数为可变对象时进行的传递, 改变形式参数的值

def demo(obj):  # demo:函数的名称, obj: 形式参数
    print("原值: ", obj)
    obj += obj


# 调用函数
print("=" * 10, "值传递", "=" * 10)  # 10个"="值传递10个"="
mot = "唯有在追赶的时候, 你才能真正地奔跑"  # 不可变对象
print("不可变对象的函数调用前: ", mot)
demo(mot)  # 调用函数
print("不可变对象的函数调用后: ", mot)
print('\n')

print("=" * 10, "引用传递", "=" * 10)
list1 = ["绮梦", "冷伊一", "香凝", "黛兰"]  # 可变对象
print("可变对象的函数调用前:", list1)
demo(list1)  # 调用函数
print("可变对象的函数调用后:", list1)


# 实例: 根据身高.体重计算BMI指数
def fun_bmi(person, height, weight):
    '''
    功能: 根据身高和体重计算BMI指数
    person:姓名
    height:身高  单位:米
    weight:体重  单位:千克
    '''
    print(person + "的身高" + str(height) + "米 \t 体重; " + str(weight) + "千克")
    bmi = weight / (height * height)  # 用于计算BMI指数, 公式为"体重/身高的平方"
    print("您的BMI指数为: ", str(bmi))
    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻 ~@_@~")
    if bmi >= 18.5 and bmi < 24.9:
        print("您的体重正常, 注意保持 (^_^)")
    if bmi > 24.9 and bmi < 29.9:
        print("您的体重过重 @_@")
    if bmi >= 29.9:
        print("肥胖 `@_@`")


# 函数编写完成了,下面调用函数
fun_bmi("路人甲", 1.73, 60)  # 计算路人甲的BMI指数
fun_bmi("路人乙", 1.60, 50)  # 计算路人甲的BMI指数
