# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 9:59
# @Author  : pgl
# @File    : 06_可变参数.py.py
# @IDE     : PyCharm

# 可变参数
# 可变参数 -->  是个数不固定的参数, 可以传递0个.1个.2个......n个参数
# 在定义可变参数的时候主要有两种形式,1:*parameter 2:**parameter
# *parameter: 可以接收任意多个实际参数,并且把他们放到一个实际元组当中
def coffee(*coffeename):  # 输出咖啡名称的函数
    print("\n①我喜欢的咖啡有: ")
    for item in coffeename:
        print(item)


coffee("蓝山")  # 调用函数, 这个时候可以指定咖啡名称
coffee("蓝山", "卡布奇诺", "巴西")


# 如果我们使用一个存在的列表作为函数的可变参数, 我们可以执行下面操作
def coffee1(*coffeename1):  # 输出咖啡名称的函数
    print("\n②我喜欢的咖啡有: ")
    for item in coffeename1:
        print(item)


list1 = ["蓝山", "卡布奇诺", "巴西"]
coffee1(*list1)


# 场景模拟, 计算社团中每个人的BMI指数
def fun_bmi(*person):  # 指定一个可变参数
    '''
    功能: 根据身高和体重计算BMI指数(共享升级版)
    persion: 可变参数, 需要传递带3个值的列表,
    分别为: 姓名.身高(单位:米),体重(单位:千克)
    '''
    for list_person in person:
        for item in list_person:
            person = item[0]  # 索引值为0的那个值
            height = item[1]  # 索引值为1的那个值
            weight = item[2]
            print(person + "的身高: " + str(height) + "米 \n 体重:" + str(weight) + "千克")

            bmi = weight / (height * height)  # 用于计算BMI指数, 公式为"体重/身高^2"
            print("您的BMI指数为: " + str(bmi))  # 输出MBI指数
            # 判断身材是否合理
            if bmi < 18.5:
                print("您的体重过轻")
            if 18.5 <= bmi < 24.9:
                print("您的体重正常")
            if 24.9 <= bmi < 29.9:
                print("您的体重稍微有点重")
            if bmi >= 29.9:
                print("肥胖")


# 调用这个函数, 调用函数要先定义列表
list_w = [['绮梦', 1.70, 65], ['凌宇', 1.78, 50], ['黛兰', 1.72, 66]]  # 列表中是每一个人的信息
list_m = [['梓轩', 1.80, 75], ['周一', 1.75, 70]]
fun_bmi(list_w, list_m)  # 计算bmi指数


# **parameter(使用2个*的可变参数)
# 接收人任意多个类似关键字参数一样显式赋值的实际参数, 并将其放到一个字典中
def sign(**sign):  # 使用两个*的参数输出结果是一个字典, 想要输出字典中的内容就要输出它的键和值
    print()
    for key, value in sign.items():  # 遍历字典
        print(key, "的星座是: ", value)


sign(绮梦='水瓶座', 冷意='射手座')  # 调用这个函数
sign(香凝='双语座', 黛兰='双子座', 琪琪='巨蟹座')  # 调用这个函数


# 我们也可以把已经存在的字典作为关键字参数
def sign1(**sign1):  # 使用两个*的参数输出结果是一个字典, 想要输出字典中的内容就要输出它的键和值
    print()
    for key, value in sign1.items():  # 遍历字典
        print(key, "的星座是: ", value)


dict = {"香凝": '双语座', "黛兰": '双子座', "琪琪": '巨蟹座'}
sign1(**dict)

# 带1个*的可变参数: 类似于按照位置进行传递, 接收到的参数值是列表
# 带2个*的可变参数: 类似于按照关键字参数进行传递, 接收到的值是字典
