# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:41
# @Author  : pgl
# @File    : 01_函数的创建和调用.py.py
# @IDE     : PyCharm


# 函数
# 简单理解:函数就是可以完成某项工作的代码块
# 1.函数的创建和调用
# 2.参数传递
# 3.返回值
# 4.变量的作用域
# 5.匿名函数(lambda)

# 创建函数又称为定义函数, 用来创建某种用途的工具, 使用def关键字实现
# def functionname([parameterlist]):
#     ['''comments''']   用来说明函数的功能和参数以及返回值等信息
#     [functionbody]    一个可选参数, 用来指定参数提的, 使用return用来返回

# 创建一个过滤危险字符的函数


def filterchar(string):
    '''
    功能: 过滤危险字符(如 黑客),并且将过滤后的结果输出
    string: 要过滤的字符串
    没有返回值
    '''
    import re  # 导入正则表达式的re模块
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'  # 模式字符串
    sub = re.sub(pattern, "@_@", string)  # 进行模式匹配 pattern:模式字符串    @_@:替换的字符    string:要过滤的字符串
    print(sub)
    # 在定义函数的时候注意函数体的缩进


# 定义一个空函数
def empty():
    pass


# 如何调用函数?
# functionname([parametersvalue])    函数名称(函数的参数,如果有多个参数多个参数之间用','分隔开)如果函数没有参数那么()也不能省略
about = "我是一名程序员,喜欢看黑客方面的书,想研究一下Trojan"
filterchar(about)
about1 = "我是一名黑客."
filterchar(about1)


# 实例: 输出每日一帖
def function_tips():
    '''
    功能: 每天输出一条励志文字
    '''
    import datetime  # 导入日期时间类
    # 下面定义一个列表
    mot = ["今天星期一: \n坚持下去不是因为我很坚强, 而是因为我别无选择.",
           "今天星期二: \n含泪播种的人一定能笑着收获.",
           "今天星期三: \n做对的事情比把事情做对重要",
           "今天星期四: \n命运给予我们的不是失望之酒, 而是机会之杯",
           "今天星期五: \n不要等到明天, 明天太遥远, 今天就行动",
           "今天星期六: \n求知若饥, 虚心若愚",
           "今天星期日: \n成功将属于那些从不说'不可能'的人"]
    day = datetime.datetime.now().weekday()  # 获取当前星期
    print(mot[day])  # 输出媒体一贴


function_tips()  # 调用函数
