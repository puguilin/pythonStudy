# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:28
# @Author  : pgl
# @File    : 37_字符串编码转换.py.py
# @IDE     : PyCharm


# 字符串编码转换
# 最早的字符串编码是ASCII码, 只包括0--9的数字和大写的26个英文字母以及小写的26个英文字母,以及: 空格/制表/换行符等其他符号
# GBK/GB2312编码 是我国制定的中文编码标准,1个字节表示英文字母, 2个字节表示中文字符
# UTF-8 国际通用的编码, 支持所有国家语言 1个字节表示英文字符, 3个字节表示中文 Python3中默认采用的UTF-8编码
# 在Python中有2中常用的字符类型 str和bytes
# str:表示Unicode字符, 一个字符对应若干个字节, 比如字符串"拼博到感动自己"
# bytes:二进制数据
# str 和 bytes两种字符串不能拼接在一起使用, 如果拼接就要把str转化为bytes类型
# str 和 bytes的相互转换需要使用encode()方法和decode()方法, 这两种方法是互逆的过程
# 1. 使用encode()方法进行编码
# 2. 使用decode()方法进行解码

# 使用encode()方法进行编码, encode()方法就是把一个字符串转化为一个2进制数据,这个过程也称为编码
# str.encode([encoding = "utf-8"][,errors = "strict"])  strict:strict,ignore,replace,xmlcharrefreplace
# 要转化的字符串.使用的方法名([参数1][参数2])
# 参数1: encoding:编码时采用的编码,默认采用的是utf-8编码,如果想使用简体中文可以使用JB-2312,当只有一个参数的时候可以省略:encoding和"="
# 参数2: 用来指定错误处理方式的,可选参数有:
# strict: 遇到不合理字符就抛出异常
# ignore: 忽略异常字符
# replace: 用?替代不合理字符
# xmlcharrefreplace: 使用xml的字符引用

str1 = "野渡无人舟自横"  # 定义一个字符串
byte1 = str1.encode("GBK")  # 采用GBK编码把str1转换为2进制数据,并且不进行异常处理
print("原字符串: ", str1)  # 输出原字符串
print("GBK编码转换后字符串: ", byte1)  # 转换之后的字符串
# 在使用encode进行字符串转换的时候并不会源字符串的内容
# 如果想修改原字符串的内容就要对它重新赋值
byte2 = str1.encode("utf-8")  # 采用utf-8编码把str1转换为2进制
print("utf-8编码转换后字符串: ", byte2)

# 对比GBK和utf-8两种情况,发现utf-8转换之后的字符串比GBK转换之后的字符串长,因为采用utf-8一个汉字占3个字节,采用GBK一个汉字占2个字节
