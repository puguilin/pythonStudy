# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/gyx 10:28
# @Author  : pgl
# @File    : 04_视频下载.py.py
# @IDE     : PyCharm


import re

import requests


# 定义函数 函数名 代码块
# 方法专门下载视频的
def download(url):
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
    file_name = f'./res/ + {name_mp4}.mp4'.replace('-梨视频官网-Pear Video', "")
    with open(file_name, mode='wb') as f:
        f.write(response.content)


page_url = 'https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=4&start=36&mrd=0.31215140672549024&filterIds=1609587,1609671,1609693,1607569,1607531,1607465,1607199,1607074,1607109,1607051,1606977,1606694,1606871,1606830,1606777'
response = requests.get(page_url)
# print(response.text)
categoryem = re.findall(r'<a href="(.*?)" class="vervideo-lilink actplay">', response.text)
# print(categoryem)
j = 0
for i in categoryem:
    download("https://www.pearvideo.com/" + i)
    j += 1;
    print(j)


