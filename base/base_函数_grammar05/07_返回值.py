# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 10:03
# @Author  : pgl
# @File    : 07_返回值.py.py
# @IDE     : PyCharm

# 返回值
# 返回值:函数比作榨汁机, 放入参数比作放入水果, 做出来的果汁相当于返回值
# 在Python中, 在函数体中使用return语句, 对于返回值的类型可以是任意类型的, 无论return出现在函数的什么位置, 只要执行都会结束函数的执行
# return[value] value是要返回的值, 可以是1个值, 也可以是多个值,多个值的时候使用','隔离开, 如果没有返回值的时候就会返回None也就是空值
# 对于一个函数我们不指定返回值, 也就是不指定return语句, 他也会返回None值, 我们为函数指定返回值以后再调用这个函数的时候就可以把9它赋给一个变量

'''
场景模拟: 商场打折活动
满500可享受9折优惠
满1000可享受8折优惠
满2000可享受7折优惠
满3000可享受6折优惠
通过函数返回合计金额以及应付金额(打折之后的金额)
'''


def fun_checkout(money):  # 定义一个带返回值的函数实现的
    """
    功能: 计算商品金额并进行折扣处理
    money: 保存商品金额的列表
    返回值: 商品的合计金额和合计后的金额
    """
    money_old = sum(money)  # 计算合计金额
    money_new = money_old
    if 500 <= money_old < 1000:  # 享受9折优惠
        money_new = '{:2f}'.format(money_old * 0.9)  # 对它进行格式化, 格式化为2位小数format
    elif 1000 <= money_old < 2000:  # 享受8折优惠
        money_new = '{:2f}'.format(money_old * 0.8)
    elif 2000 <= money_old < 3000:
        money_new = '{:2f}'.format(money_old * 0.7)
    elif 3000 <= money_old:
        money_new = '{:2f}'.format(money_old * 0.6)
    return money_old, money_new  # 返回总金额以及折扣后的金额


# 调用函数 调用函数的时候需要定义一个列表, 这个列表是定义商品金额的
print("\n我们要进行结算了......\n")
list_money = []
while True:  # 写while循环的目的是可以进行多次输入
    inmoney = float(input("请输入商品金额 (输入0表示输入完毕):"))  # 输入金额转换为浮点型
    if int(inmoney) == 0:
        break  # 退出循环
    else:
        list_money.append(inmoney)
        money = fun_checkout(list_money)
print("合计金额:", money[0], '\n', "应付金额", money[1])
