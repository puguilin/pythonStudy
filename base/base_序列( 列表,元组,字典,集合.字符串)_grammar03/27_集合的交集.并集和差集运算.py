# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:45
# @Author  : pgl
# @File    : 27_集合的交集.并集和差集运算.py.py
# @IDE     : PyCharm


# 集合的交集.并集和差集运算
# 交集: & 两个集合中相交的部分
# 并集: |
# 差集: - 只在其中一个集合中出现,并不在另外一个集合中出现
# 对称差集: ^ 只在一个集合中出现
python = set(['绮梦', '冷伊一', '香凝', '梓轩'])
c = set(['冷伊一', '凌宇', '梓轩', '盛博'])
print("输出两个集合的内容:", '\n', '选择python的学生名字:', python, '\n', '选择c语言的学生姓名:', c)
print("交集运算:", "既选择python又选择c", python & c)
print("并集运算:", "也就是全部学生名字", python | c)
print("差集运算:", "选择了python没有选择c的学生名字", python - c)
print("对称差运算:", "只选择python或者c的学生名字", python ^ c)
