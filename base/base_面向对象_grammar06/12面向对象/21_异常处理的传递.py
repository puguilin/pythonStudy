# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:46
# @Author  : pgl
# @File    : 21_异常处理的传递.py.py
# @IDE     : PyCharm


def fn1():
    print("这是fn1函数执行的")
    return 1 / 0


def fn2():
    print("这是fn2函数执行的")
    fn1()


def fn3():
    try:
        print("这是fn3函数执行的")
        fn2()
    except Exception as e:
        print(f'发生了{e}')
    # print("这是函数fn3执行的")
    # fn2()


fn3()
# 发生错误可以传递


