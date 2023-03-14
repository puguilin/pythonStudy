# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/21 17:30
# @Author  : pgl
# @File    : 01_util.py.py
# @IDE     : PyCharm

import math
from math import sqrt
from random import randint
import time

"""
    1.1 将华氏温度转换为摄氏温度
    F = 1.8C + 32
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
    1.2 输入半径计算圆的周长和面积 
"""

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

"""
    1.3 判断是否是润年 
"""
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

"""
    1.4 英制单位英寸和公制单位厘米互换 
"""
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')

"""
    1.5 判断输入的边长能否构成三角形
        如果能则计算出三角形的周长和面积 
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')

"""
    1.6 输入一个正整数判断它是不是素数 
"""

num = int(input('请输入一个正整数: '))
# 求平方根
end = int(sqrt(num))
print('%d<<' % end)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
    else:
        print('%d是除数' % x)
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


"""
    1.7 输入两个正整数计算最大公约数和最小公倍数

"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

"""
    1.8 打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()



"""
    1.9 求解《百钱百鸡》问题
        1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
        问公鸡 母鸡 小鸡各有多少只

"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# 要理解程序背后的算法 - 穷举法


"""
2.0 Craps赌博游戏
    玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
    如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
    玩家再次要色子 如果摇出7点 庄家胜
    如果摇出第一次摇的点数 玩家胜
    否则游戏继续 玩家继续摇色子
    玩家进入游戏时有1000元的赌注 全部输光游戏结束


"""



money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')



"""
2.1 输出斐波那契数列的前20个数
    1 1 2 3 5 8 13 21 ...
"""

a = 0
b = 1
for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')


"""
2.2 猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')


"""
2.4 找出100~999之间的所有水仙花数
    水仙花数是各位立方和等于这个数本身的数
    如: 153 = 1**3 + 5**3 + 3**3

"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""
2.5 判断输入的正整数是不是回文数
    回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)


"""
2.6 找出1~9999之间的所有完美数
    完美数是除自身外其他所有因子的和正好等于这个数本身的数
    例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

"""
start = time.clock()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if 1 < factor != num / factor:
                sum += num / factor
    if sum == num:
        print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")

# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性


"""
2.7 输出2~99之间的素数

"""

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')


"""
3.0 输出乘法口诀表(九九表)
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()


