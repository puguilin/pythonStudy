# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/gyx 10:18
# @Author  : pgl
# @File    : 03_爬取视频详情所有网址.py.py
# @IDE     : PyCharm


import re

import requests

# 获取所有视频详情页网址


url = 'https://www.pearvideo.com/video_1607724'
# 请求网页数据
res = requests.get(url)
# 正则表达式模块 内建模块 本身自带 *？匹配想要的东西
url_now = re.findall('srcUrl="(.*?)"', res.text)[0]
name_mp4 = re.findall(r'<title>(.*?)</title>', res.text)[0]
# print(name_mp4)
# print(url_now)
# print(url_now[8:-1])
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# 服务器返回数据，视频数据
response = requests.get(url_now, headers=headers)
# 自动关闭文件
file_name = f'{name_mp4}.mp4'.replace('-梨视频官网-Pear Video', "")
with open(file_name, mode='wb') as f:
    f.write(response.content)
print(response)
