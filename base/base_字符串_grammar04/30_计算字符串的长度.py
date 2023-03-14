# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:02
# @Author  : pgl
# @File    : 30_计算字符串的长度.py.py
# @IDE     : PyCharm


# 1.2 计算字符串的长度
# 中文汉字根据编码不同占的字节数也不同,一般占2--4个字节, 使用UTF-8编码中文占3个字节,英文占1个字节; 使用GBK编码中文占2个字节,英文占1个字节
str1 = "人生苦短, 我用Python!"
print("计算UTF-8编码下的str1字符串长度: ", len(str1.encode()))  # encode()表示采用UTF-8编码
print("计算GBK编码下的str1字符串长度: ", len(str1.encode("gbk")))  # encode("gbk")表示采用gbk编码







