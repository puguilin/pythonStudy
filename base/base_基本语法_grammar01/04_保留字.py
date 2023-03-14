#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved
#
# @Time    : 2023/02/12 23:21
# @Author  : pgl
# @File    : 04_保留字.py
# @IDE     : PyCharm
# Python 保留字与标识符

# 保留字是被赋予特定含意的一些单词，不可作为变量、函数、类、模块和其他对象的名称来使用。区分大小写:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 查看Python的保留字, 保留字是区分大小写的
import keyword
print(keyword.kwlist)


# 标识符
# 由大小写字母 下划线_ 数字，并且不能放到第一位，区分大小写。
# 不要使用中文标识符
# _标识符：保护变量
# __标识符：类的私有成员
# __标识符__：专用标识

# 常见错误
# 在开发程序时, 如果使用Python中的保留字作为模块, 类, 函数或者变量的名称时, 将产生无效语法.
# 下面是保留字的错误例子
# if = "坚持下去不是因为我很坚强, 而是因为我别无选择"
# print(if)

# 2. 标识符, Python中可以使用汉字作为标识符,但是不推荐
# 错误的表示符                         正确的表示符
# 300warrior 因为以数字开头             number
# $money 因为以$开头                   name48
# one%two 因为里面含有%                USERID
# User Name 因为里面有空格              O_o
# try 因为使用了关键字作为标识符          Try
# 单下划线+标识符-->保护变量            _标识符 --> 保护变量
# 双下划线+标识符-->类的私有成员         __标识符 --> 类的私有成员
# 双下换线开头和结尾的-->专用标识        __标识符__ --> 专用标识
