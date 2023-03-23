# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/gyx 17:58
# @Author  : pgl
# @File    : psutil介绍.py.py
# @IDE     : PyCharm

import datetime

import psutil

# 1.获取CPU信息
# 1）逻辑CPU核心数
print(psutil.cpu_count())
# 2）物理CPU核心数
print(psutil.cpu_count(logical=False))
# 3）CPU的使用率
print(psutil.cpu_percent(interval=1))
# 4）每个逻辑核心的使用率
print(psutil.cpu_percent(interval=1, percpu=True))

# 2.获取内存信息
# 1）内存的整体信息
print(psutil.virtual_memory())
# 2）内存的使用率
print(psutil.virtual_memory().percent)

# 3.获取磁盘信息
# 1）磁盘的分区信息
print(psutil.disk_partitions(all=True))
# 2）指定目录的磁盘信息
print(psutil.disk_usage('C:'))
# 3）磁盘的使用率
print(psutil.disk_usage('C:').percent)

# 4.获取网络信息
print(psutil.net_io_counters())

# 5.获取重启时间
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S'))

# 6.获取用户信息
print(psutil.users())

