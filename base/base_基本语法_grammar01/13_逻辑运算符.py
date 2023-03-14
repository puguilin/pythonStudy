# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/20 15:08
# @Author  : pgl
# @File    : 13_逻辑运算符.py.py
# @IDE     : PyCharm


# 逻辑运算符
# 常用三个逻辑运算符
# 逻辑与: and (一假则假)
# 逻辑或: or (只要一个条件真就为真, 只有全部为假的时候才为假) (一真则真)
# 逻辑非: not (条件为真的时候结果为假, 条件为假的时候结果是真) (真变假, 假变真)
print("\n手机店打折活动进行中......")  # \n 换行
strWeek = input("请输入中文星期(如: 星期一): ")  # 输入星期
intTime = int(input("请输入时间中的小时 (范围: 0~23,且为整数):"))  # 输入时间
if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11)) or (strWeek == "星期五" and (intTime >= 14 and intTime <= 15)):
    print("恭喜您, 获得了折扣参与资格! ")  # == :----> 比较运算符
else:
    print("对不起, 您来晚一步, 期待下次活动 ......")
