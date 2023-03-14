# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:19
# @Author  : pgl
# @File    : 35_去除字符串中的空格和特殊字符.py.py
# @IDE     : PyCharm

# 去除字符串中的空格和特殊字符 特殊字符指的是:\t(制表符) \r(回车符) \n(换行符)
# Python中去除字符串中的空格和特殊字符有3种方法

# 1.strip() 中来去除字符串两端的空格和特殊字符
# " 相信自己\n" 在执行完strip()函数之后就会变成 "相信自己",在使用stripe()方法的时候要注意它只去掉字符串两个的字符和空格不会去掉中间的
# " 相信 自己\n" 在使用stri()方法之后"相信 自己"
# str.strip([chars]) chars用来指定去除的参数,如果不指定就默认为"空格.制表符\t,回车符\r,换行符\n"
str1 = " http://www.mingrisoft.com \\t\\n\\r这样呢"  # 如果不在\n等前面加上"\"就会运行这个结果!!所以遇到转义字符就要"\\"
print(str1)
print("不指定参数的stripe()方法输出结果:", str1.strip())
str2 = "* http://www.mingrisoft.com 哈哈\\t\\n\\r这样呢*"
print(str2)
print("只想去掉空格的stripe()方法输出结果:", str2.strip("*"))  # 指定参数的时候"" 或者''都可以

# lstrip() 把字符串前面也就是左侧的空格或者字符去除
# " 相信自己\n"  在执行完 lstrip()方法之后的结果 "相信自己\n", 对于lstrip的语法格式和strip的语法格式很像
# str.lstrip([chars]) 参数chars可以是空格.制表符\t.回车符\r.换行符\n
str3 = " http://www.mingrisoft.com \\t\\n\\r"
print("使用lstrip并且不指定参数的输出结果:", str3.lstrip())

# 和lstrip()相对的rstrip()
str4 = " http://www.mingrisoft.com \\t\\n\\r"
print("使用rstrip并且不指定参数的输出结果:", str4.rstrip())
