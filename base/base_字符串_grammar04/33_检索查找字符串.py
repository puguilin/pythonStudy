# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:16
# @Author  : pgl
# @File    : 33_检索查找字符串.py.py
# @IDE     : PyCharm

# 检索字符串

# 检索字符串也是字符串查找,在Python提供了多种字符串查找的方法
# 1.count() 检索一个字符串在另外一个字符串中出现的次数
# 2.find() 是否包含子字符串的
# 3.index() 和find()方法比较类似,也是用来检索是否包含子字符串的
# 4.startswith() 用来检索是否以指定字符串开头的
# 5.endswitch() 用来检索是否以指点字符串结尾的

# count()用来检索指定的字符串在另一个字符串当中出现的次数,如果检索的字符串不存在返回值是0
# str.count(sub[,start[,end]])    sub:用来指出检索的子字符串, start:检索的起始位置, end:检索的结束位置, 如果省略end就会一直检索到结束, 如果省略start和end就会检索全部
str1 = "@明日科技 @扎克伯格 @俞敏洪 @勤奋的天使"
print("@出现的次数:", str1.count("@"))

# find()用来检索是否包含子字符串的,
# str.find(sub[,start[,end]]) sub:用来指定检索的子字符串的
print("在这个字符串中是否包含@符号,并且指出首次出现的位置", str1.find("@"))  # 首次出现@的索引值是0
print("指定不存在的字符:返回值是-1", str1.find("%"))  # 如果索引值是-1说明不存在这个值
print("使用in关键字,判断一个字符是否在另一个字符中", "@" in str1)  # 如果在里面就输出True, 不在就输出False
print("rfind,返回字符串最后一次出现的位置(从右向左查询)", str1.rfind("@"))  # rfind()函数用于返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回“-1”

# index()用来检索是否包含指定的字符串,只不过在使用index方法的时候,指定字符串不存在的时候会抛出一个异常值
# str.index(sub[,start[,end]])    # sub:用来判断的子字符串,
print("index判断@是否存在,如果存在返回的是第一次出现这个符号的索引位置", str1.index("@"))  # 如果存在返回的是第一次出现这个符号的索引位置
# print("index判断,如果查找的字符串不在被查找字符串当中,就会报错",str1.index("$"))    # '$'不在str1中,就会抛出异常
# rindex从右边开始查找
print("rindex从右边开始查找第一次出现这个符号的索引位置", str1.rindex("@"))

# startswitch()这个方法用来检索一个字符串以指定的字符串开头,如果是就返回True,,不是就返回False
# 字符串对象,方法的名称,三个参数, 第一个参数指定查找的字符串, 第二个参数用来指定从哪里开始,第三个参数指定从哪里结束
print("startswitch方法判断是否以@开头的结果,存在是True:", str1.startswith("@"))
print("startswitch方法判断是否以$开头的结果,不存在是False:", str1.startswith("$"))

# endswitch()用来判断是否以指定的字符串结束
# str.endswitch(suffix[,start[,end]])    suffix:用来判断的对象,......
print("endswitch,判断字符串是否以指定'@'字符串结束,False:不是以这个符号结束", str1.endswith("@"))
print("endswitch,判断字符串是否以指定'使'字符串结束,True:是以这个符号结束", str1.endswith(""))
