# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:39
# @Author  : pgl
# @File    : 18_元组元素推导式.py.py
# @IDE     : PyCharm

# 元素推导式
# 在使用元组推导式的时候,生成结果是一个生成器对象,不是元组,如果想要得到元组要使用tuple函数进行转换, 如果不想视同tuple函数还想得到结果就要使用for循环遍历
# 元组推导式可以快速生成一个元组, 或者根据某个元组生成满足指定需求的元组(就是快速生成元组的)
# 元组推导式和列表推导式很像, 就是把[]换成()

import random  # 导入随机数模块

# 生成一个包含10个随机数的元组
randomnunber1 = (random.randint(10, 100) for i in range(10))  # random.randint(10,100) 在10到100产生随机数
print("tuple()函数生成结果: ", tuple(randomnunber1))  # 如果不使用tuple函数, 就看不到生成元组的样子

# 不想使用tuple()函数还想看到元组, 就要使用for循环
randomnunber2 = (random.randint(10, 100) for i in range(9))
for i in randomnunber2:
    print(i, end=' ')  # 可以看到输出结果但不是一个元组

print("\n")  # 单纯加入一个空行行,没其它想法和作用
# 使用__next__看生成器中的元素
randomnunber3 = (random.randint(10, 100) for i in range(8))
print(randomnunber3.__next__())  # 输出的是第1个元素
print(randomnunber3.__next__())  # 输出的是第2个元素
print(randomnunber3.__next__())  # 输出的是第3个元素
print(randomnunber3.__next__())  # 输出的是第4个元素
print(randomnunber3.__next__())  # 输出的是第5个元素
