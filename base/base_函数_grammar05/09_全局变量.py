# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:08
# @Author  : pgl
# @File    : 09_全局变量.py.py
# @IDE     : PyCharm


# 全局变量
# 全局变量: 能够作用于函数内部和函数外部的变量, 就是指既能在函数内部访问又能在函数体外部访问到
message = "唯有在被追赶的时候, 你才能真正的奔跑."  # 定义一个变量(定义一个全局变量),让它等于一个字符串


def fun_demo():  # 定义一个没有入口参数的变量
    print("函数体内: 输出全局变量message=", message)  # 输出局部变量message的值
    # 我们不能在函数体内改变全局变量的值, 如果改变的化就相当于在函数体内定义了一个局部变量, 改变的只是局部变量的值, 全局变量的值不会改变


fun_demo()  # 调用函数
print("函数体外: 输出全局变量message=", message)

# 我们不能在函数体内改变全局变量的值, 如果改变的话就相当于在函数体内定义了一个局部变量, 改变的只是局部变量的值, 全局变量本身的值不会改变
message1 = "唯有在追赶的时候, 你才能真正奔跑."  # 定义一个全局变量


def fun_demo1():  # 定义一个没有参数的函数
    message1 = "失望之酒,希望之杯"  #
    print("在函数体内输出:全局变量message1=", message1)  # 函数体内不能改变全局变量的值, 输出结果仅是函数


fun_demo1()  # 调用定义的函数
print("函数体外输出: 全局变量message1=", message1)  # 在函数体外输出全局变量的值

# 函数体内不能修改全局变量的值, 如果我们修改该怎么做呢? 这就要我们在函数体内定义一个全局变量, 可以使用global修改这个变量, 把一个局部变量变成全局变量
message2 = "唯有在追赶的时候, 你才能真正奔跑."  # 定义一个全局变量


def fun_demo2():  # 定义一个没有参数的函数
    global message2  # 通过global让局部变量变为全局变量, 也就是重新定义全局变量
    message2 = "哈哈哈哈哈哈, 失望之酒, 希望之杯"  #
    print("在函数体内输出:全局变量message2=", message2)  # 此时可以通过函数体内的局部变量进行修改全局变量了


fun_demo2()  # 调用定义的函数
print("函数体外输出: 全局变量message2=", message2)  # 在函数体外输出全局变量的值

"""
场景模拟: 松树做梦
"""
pineteer = "我是一棵松树"  # 定义一个全局变量


def fun_christmastree():  # 定义一个函数, 没有入口参数的函数
    # 写函数注释
    '''
    功能: 一个梦
    无返回值
    '''
    pineteer = '挂上彩灯.礼物......让它变成一棵圣诞树@^.^@\n'  # 定义了一个局部变量
    print("函数体内的pineteer变量输出: ", pineteer)


print("函数体外的pineteer变量输出: ", pineteer)
print("\n下雪了...\n")
print("=" * 15
      , "开始做梦......", "=" * 15)  # "="*15,输出15个等号
fun_christmastree()  # 调用函数
print("=" * 15, "梦醒了......", "=" * 15)
pineteer = "我身上落满雪花," + pineteer + " -_-"  # 为全局变量赋值
print(pineteer)
