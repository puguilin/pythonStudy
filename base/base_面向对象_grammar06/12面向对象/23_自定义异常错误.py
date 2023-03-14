# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:48
# @Author  : pgl
# @File    : 23_自定义异常错误.py.py
# @IDE     : PyCharm


# raise 自定义错误通过 raise  来说明

class LenError(Exception):
    def __str__(self):
        return "长度输入错误"


class FexError(Exception):
    def __str__(self):
        return "不知道的错误名"


try:
    username = input("请输入自定义名字")
    if 8 < len(username) < 16:
        print(f'你当前输入的名字为{username}')
    else:
        raise LenError  # raise 自定义错误通过 raise  来说明
except LenError as e:
    print(e)
