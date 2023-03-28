# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:43
# @Author  : pgl
# @File    : 23_添加.修改和删除字典元素.py.py
# @IDE     : PyCharm

# 添加.修改和删除字典元素
# 字典是可变序列,可以随时向其中添加元素,也就是键值对
# 语法: dictionary[key] = value    # 字典的名称,键 = 值 键必须是唯一的,值可以不是唯一的,并且这个值可以是任何数据类型
sign = {'绮梦': '水瓶座', '冷伊一': '射手座', '香凝': '双鱼座', '黛兰': '双子座'}  # 首先定义一个字典
# 向里面添加一个"荸荠"他的星座是"巨蟹座"
sign["荸荠"] = "巨蟹座"  # 添加一个元素
print("字典修改添加元素 dictionary[key] = value   添加键后的结果", sign)
# 如果向字典中添加的键已经存在了,就会更新键的值
sign["荸荠"] = "处女座"  # 添加已经存在的一个元素
print("如果向字典中添加的键已经存在了,就会更新键的值 ", sign)

# update（）方法更新字典
dict01 = {'Name': 'Zara', 'Age': 7}
dict02 = {'Sex': 'female'}
dict01.update(dict02)
print(" update（）方法更新字典 " + str(dict01))

# update（）方法更新字典  有相同的键update就会被替换
dict03 = {'Age': 18, 'Sex': 'female'}
dict01.update(dict03)
print(" update（）方法更新字典  有相同的键update就会被替换 " + str(dict01))
# 删除字典元素
del sign["荸荠"]  # 删除"荸荠"这个字典元素
print("删除键'荸荠'之后的结果", sign)
print('\n')
# 删除不存在的键就会报错!!!
# 在删除元素的时候最好加上一个判断,看下该元素是否存在,防止该元素不存在,出现报错
if "小香凝" in sign:
    del sign["小香凝"]
else:
    print("小香凝不在该字典中")
print("使用if语句判断之后的结果", sign)
