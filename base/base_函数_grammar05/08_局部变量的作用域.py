# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:06
# @Author  : pgl
# @File    : 08_局部变量的作用域.py.py
# @IDE     : PyCharm


# 变量的作用域
# 变量的作用域是指代码能够访问变量的区域, 如果超出该区域, 再访问时就会出现错误.
# 在程序当中一般会根据变量的有效范围把变量分为:局部变量和全局变量
# 局部变量: 在函数内部定义并且使用的变量, 只在函数内部有效
def fun_demo():  # 定义一个没有入口参数的变量
    message = "唯有在被追赶的时候, 你才能真正的奔跑."  # 定义一个变量(局部变量),让它等于一个字符串
    print("局部变量message=", message)  # 输出局部变量message的值


fun_demo()  # 调用函数
# print("函数体外输出message",'message=',message)    就会报错
