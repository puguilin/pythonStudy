# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:28
# @Author  : pgl
# @File    : 06_pass语句.py.py
# @IDE     : PyCharm


# pass 语句
# pass语句, 表示空语句, 它不做任何事情, 一般起到占位作用.
# 应用for循环语句, 输出1 到10 之间的偶数, 并且不是偶数的时候占个位置, 方便以后对不是偶数的数进行处理
for i in range(1, 10):
    if i % 2 == 0:  # 判断能不能被2整除,如果能被2整除,则就是偶数, 输出这个偶数
        print(i, end=' ')  # 在一行输出偶数, 并用空格
    else:
        pass  # 占位, 不做任何事情
