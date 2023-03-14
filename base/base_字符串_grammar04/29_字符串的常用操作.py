# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 8:49
# @Author  : pgl
# @File    : 29_字符串的常用操作.py.py
# @IDE     : PyCharm


# 拼接字符串
# 字符串的常用操作
# 定义字符串时候有 ''      " "      ''' '''三种,且作用一样
# 区别: '' ""两种的内容必须写在一行, ''' '''的内容可以是多行

# 1.1 拼接字符串
# 1.2 计算字符串的长度
# 1.3 截取字符串
# 1.4 分隔.合并字符串
# 1.5 检索字符串
# 1.6 字母的大小写转换
# 1.7 去除字符串中的空格和特殊字符
# 1.8 格式化字符串

# 1.1 拼接字符串 使用 +
# 字符串1 + 字符串2 = 字符串1字符串2
hi = "Hi!"
account = "heiheiyouheihei"
print("使用+连接两个字符串的结果:", hi + account)

# pycharm的光标变成小方块,摁下"insert"键
str1 = "我今天一共走了"
num = 1780
str2 = "步"
print("字符串+数字的输出:", str1 + str(num), str2)  # 要把数字转化为字符串才能相加,使用str()

# 情景模拟
print("\n", "情景模拟")
programmar_1 = "程序员甲:搞IT太辛苦了,我想换行怎么办?"
programmar_2 = "程序员乙:敲一下回车键"
print(programmar_1 + "\n" + programmar_2)  # 注意一下这个换行的方式,没有使用,使用的+
