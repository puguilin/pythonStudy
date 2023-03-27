# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 17:40
# @Author  : pgl
# @File    : 20_字典的创建和删除.py.py
# @IDE     : PyCharm


# 字典的创建和删除
# 1.1 字典的创建和删除
# 1.2 通过键值对访问字典
# 1.3 遍历字典
# 1.4 添加修改和删除字典元素
# 1.5 字典推导式

# 1.1 字典的创建和删除(字典采用键值对的形式来保存数据的,每个元素包括两个部分:一个是键,一个是值)
# 怎么创建字典?
# 音节索引 --> ['che','chen','cheng','chi']
# 正文汉字 --> ['车','尘','称','吃']
# 定义字典的语法: = {'key1':'value1','key2':'value2',...,'keyn','valuen'}    每个键值对中间使用","分隔开
# 两个列表转化为字典


# 1.1.1 普通定义字典
word = {'che': '车', 'chen': '尘', 'cheng': '称', 'chi': '吃'}  # 定义了一个字典
print("创建字典的方式 1: 普通定义字典 \n", word, '\n', " word的属性是:", type(word))  # '\n'用来换行

# 将两个列表转化为字典类型
# 1.1.2 直接把列表转换为:字典    # zip(list1,list2):zip()函数把这两个列表转化为一个元组,并且返回一个zip对象,然后通过相应的函数转化为相应的类型.字典就使用dict()函数
key = ['che', 'chen', 'cheng', 'chi']
value = ['车', '尘', '称', '吃']
zip1 = zip(key, value)  # zip函数把两个列表中对应位置的元素组合为一个元组,并且返回一个zip对象
print("把两个列表中对应位置的元素组合为一个元组,并且返回一个zip对象: " + str(zip1))
word1 = dict(zip1)  # 转化为字典
print("创建字典的方式 2:  把两个列表中对应位置的元素组合为一个元组,并且返回一个zip对象 通过dict() 方法转化为字典 "
      "\n   列表一是：", key,
      "\n   列表二是：", value,
      "\n   列表转化为字典", word1)

# 创建字典的方法3
dictionary2 = dict(今天='小狗', 明天="小猫", 后天='小鸡')
print("创建字典的方法 3: 通过dict（）方法创建字典  \n", dictionary2)

# 场景模拟
name = ['绮梦', '冷伊一', '香凝', '黛兰']  # 创建的名字列表, 使用''还是""都可以
sign = ['水瓶座', '射手座', '双鱼座', '双鱼座']  # 星座
dictionary = dict(zip(name, sign))  # 转换为字典
print("场景模拟结果: 将两个列表对应值转化为字典 \n ", dictionary)

# 使用元组创建字典, 如果上面是列表不是元组运行就会报错,列表是不能作为字典的键!列表是不能作为字典的键!列表不能作为字典的键!
name1 = ('大黄', '布偶', '泰格', '皮革')
sign1 = ['狗', '猫', '老虎', '猪']
dictionary1 = {name1: sign1}
print("使用元组格式创建字典: ", dictionary1)

# 创建一个空字典, 法1
word2 = {}  # 创建一个空字典
print("创建空字典的方法1:", word2)

word3 = dict()
print("创建空字典的方法2:", word3)

# 使用dict 的fromkeys()方法创建一个值为空的字典, 下面创建一个只包括名字的字典,只有键没有值
name2 = ['周一', '周二', '周三', '周四', '周五']
dictionary3 = dict.fromkeys(name2)
print("使用dict 的fromkeys()方法创建一个值为空的字典:", dictionary3)

# 删除.清空字典
name3 = ['1', '2', '3', '4', '5']
col = ['红', '黄', '蓝', '绿', '紫']
dictionary4 = dict(zip(name3, col))
print(dictionary4)
dictionary5 = dictionary4.clear()  # 清空字典
print("清空字典:", dictionary5)
del dictionary4  # 删除字典,使用del()语句
# print("删除字典:", dictionary4)  # 这里会报错,因为上面的字典已经删除了,再输出就会报错



