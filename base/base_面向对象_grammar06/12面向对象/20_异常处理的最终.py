# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:45
# @Author  : pgl
# @File    : 20_异常处理的最终.py.py
# @IDE     : PyCharm


try:
    # 可能发生错误的代码
    f = open('demo1.txt', 'r', encoding='utf-8')
except FileNotFoundError as e:
    # 发生错误执行
    f = open('demo1.txt', 'w', encoding='utf-8')
    print(e)
else:
    # 没有发生错误执行的代码
    content = f.read()
    print(content)
finally:
    # 无论是否发生错误执行的
    f.close()


