# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/29 14:41
# @Author  : pgl
# @File    : 分组聚合.py
# @IDE     : PyCharm


from pandas import DataFrame

df = DataFrame({'name': ['张三', '李四', '王五', '赵六'],
                'gender': ['男', '女', '男', '女'],
                'age': [22, 11, 22, 33]})
print(df)
'''
  name gender  age
0   张三      男   22
1   李四      女   11
2   王五      男   22
3   赵六      女   33
'''
# 根据 age 分组
gp_age = df.groupby('age')
print("\n 根据 age 分组: ")
print(gp_age)
print("\n 根据 age 分组的数量: ")
print(gp_age.count())
'''
 根据 age 分组的数量: 
     name  gender
age              
11      1       1
22      2       2
33      1       1
'''

# 根据 age、gender 分组
gp_age_gender = df.groupby(['age', 'gender'])
print("\n 根据 age、gender 分组:")
print(gp_age_gender)
print("\n 根据 22、男 分组:")
print(gp_age_gender.get_group((22, '男')))
'''
 根据 22、男 分组:
  name gender  age
0   张三      男   22
2   王五      男   22
'''
print('---------')

