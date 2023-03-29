# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/17 17:23
# @Author  : pgl
# @File    : 29_append(), extend(), insert()用法详解区别.py
# @IDE     : PyCharm


# append() 追加单个元素到List的尾部，只接受一个参数，参数可以是任何数据类型，被追加的元素在List中保持着原结构类型。

# list.append(object) 其实就是向列表中添加一个对象object。

list3 = ['h1', 'e1', 'l2', 'l1', 'o1']
list4 = ['0h', '0e', '0l', '05', '06']
list3.append(list4)
print("list3.append(list4)   list4作为一个一个对象object参数 追加到list3 后面 \n", list3)


list1 = ['H', 'E', 'L', 'L', 'O']
list2 = ['1', '2', '3', '4']
list1.append(list2)

# 打印现在的list1
print(" list1.append(list2)   list2作为一个一个对象object参数 追加到list1 后面  \n", list1)
print("list1.append(list2)   list2 不变 \n", list2)

'''
list1.append(list2)   list2作为一个一个对象object参数 追加到list1 后面  
 ['H', 'E', 'L', 'L', 'O', ['1', '2', '3', '4']]
list1.append(list2)   list2 不变 
 ['1', '2', '3', '4']
'''

#  extend() 将一个列表中每个元素分别添加到另一个列表中，只接受一个参数。

extend1 = ['h', 'e', 'l', 'l', 'o']
extend2 = ['1', '2', '3', '4']
extend1.extend(extend2)
print("extend1.extend(extend2) 将一个列表中每个元素分别添加到另一个列表中  extend2中的每个元素追加到extend1 中    \n", extend1)
print("extend1.extend(extend2)  extend2 不变  \n", extend2)

'''
extend1.extend(extend2) 将一个列表中每个元素分别添加到另一个列表中  extend2中的每个元素追加到extend1 中    
 ['h', 'e', 'l', 'l', 'o', '1', '2', '3', '4']
extend1.extend(extend2)  extend2 不变  
 ['1', '2', '3', '4']

'''

# insert() 将一个元素插入到列表中，但其参数有两个（如insert(1,”g”)），第一个参数是索引点，即插入的位置，第二个参数是插入的元素。

insert1 = ['A', 'B', 'C', 'D']
insert2 = ['h', 'e', 'l', 'l', 'o']

# insert(),在list1的第2个元素前插入一个元素'X'
insert1.insert(1, 'X')

print("insert(1,”g”)），第一个参数是索引点，即插入的位置，第二个参数是插入的元素  \n", list1)

#  + 加号，将两个list相加，会返回到一个新的list对象，
#  注意与前三种的区别。前面三种方法（append, extend, insert）可对列表增加元素的操作，他们没有返回值，是直接修改了原数据对象。
#  注意：将两个list相加，需要创建新的list对象，从而需要消耗额外的内存，特别是当list较大时，尽量不要使用“+”来添加list，而应该尽可能使用List的append()方法。
list12 = insert1 + insert2

print("将两个list相加，需要创建新的list对象，从而需要消耗额外的内存  ==>list1 + list2  \n", list12)

'''
将两个list相加，需要创建新的list对象，从而需要消耗额外的内存  ==>list1 + list2  
 ['A', 'B', 'C', 'D', 'h', 'e', 'l', 'l', 'o']
'''



