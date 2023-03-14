# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 14:58
# @Author  : pgl
# @File    : 07_字符串类型及换行.py.py
# @IDE     : PyCharm


# 字符串, 就是连续的字符序列, 可以是计算机所能表示的一切字符的集合.
# 我们日常生活中看到的文字. 数字. 字母. 符号等都是字符串, 在Python中是不可变序列
# 通常用单引号, 双引号, 三引号括起来, 单引号双引号的内容只能在同一行中, 三引号的内容可以是连续的多行

# 要么使用的是单引号, 要么使用的是双引号或者三引号, 不能混用
title = '我喜欢的名言'  # 使用单引号
mot_cn = "命运给予我们的不是失望之酒, 而是机会之杯."  # 使用双引号
mot_en = '''Our destiny offers not the cup of despair,
but the chances of opportunity. '''  # 使用三引号
print(title)
print(mot_cn)
print(mot_en)
# 可以在单引号中嵌套双引号
temp = 'py"th"on'
print(temp)

# 如果我们在单引号或者双引号中的内容太长, 想分两行写,但是输出的时候还是在同一行,该怎么做呢? 可以使用反斜杠或者小括号来实现

# 法1:  就在想换行的字符前面加上"\"
no1 = "Our destiny offers not the cup of despair,\
but the chances of opportunity."
print(no1)
# 法2:  加入()
no2 = ("Our destiny offers not the cup of despair,"
       "but the chances of opportunity. ")
print(no2)

# 如果在我们输出的字符串中需要一个单引号怎么办? 那么就在要加入的单引号前面加入一个反斜杠
title2 = '我喜欢的\'名言'  # 实际上\就是转义字符
print(title2)
# 转义字符: 是指使用"\"对一些特殊的字符进行转义.
# \     续航符
# \n    换行符
# \0    空
# \t    水平制表符, 用于横向跳到下一制表位
# \"    双引号
# \'    单引号
# \\    一个反斜杠
# \f    换页
# \0dd  八进制数, dd代表的字符, 如\012代表换行
# \xhh  十六进制数, hh代表的字符, 如\x0a代表换行
# 如果想输出转义字符, 在转义字符前面加上r

print("""
                    ▶▶▶
                    |
             __\--__|_
II=====0000[/ ★007___|               
       _____\_____|/-----.
     /____mingrisoft.com__|
      \@@@@@@@@@@@@@@@@@@/
""")
