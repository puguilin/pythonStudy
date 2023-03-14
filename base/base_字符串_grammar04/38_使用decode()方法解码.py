# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:29
# @Author  : pgl
# @File    : 38_使用decode()方法解码.py.py
# @IDE     : PyCharm


# 使用decode()方法解码
# encode()是编码,decode()是把encode()编码的二进制代码转换为字符串
# str.decode([encoding = "utf-8"][,errors = "strict"])
# 参数1: 指定解码方式,这个解码方式要和编码时候设置的方式一致,这里默认采用utf-8编码方式,如果想使用简体中文就要设置为JGB或者GB2312,如果只有一个参数可以省略=
# 参数2: 表示发生错误时候的处理方式, stric有这几个可选参数strict. ignore. replace. xmlcharrefreplace
# strict: 遇到违规字符抛出异常
# ignore: 忽略违规异常
# replace: 用?替换违规异常
# xmlcharrefreplace: 使用xml的字符引用

# 使用utf-8编码把转化为2进制编码的字符再转回来
str1 = "夜渡无人舟自横"
byte = str1.encode("utf-8")  # 采用UTF-8编码转换称为2进制编码
print("源字符串: ", str1)  # 源字符串
print("转换后: ", byte)  # 转换后的2进制字符串
newstr = byte.decode("utf-8")  # 解码,如果解码方式和编码方式就会异常报错
print("解码后: ", newstr)
# 在使用decode()方法进行解码的时候也encode()方法一样,不会对原来字符串内容进行修改,如果修改需要自己重新赋值


