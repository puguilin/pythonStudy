# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/gyx 10:09
# @Author  : pgl
# @File    : 02_视频爬取.py.py
# @IDE     : PyCharm


# 梨视频爬取
'''
二进制数据流：视频，图片，音频
'''
import requests

# 请求网站
mp4_url = 'https://video.pearvideo.com/mp4/third/20191004/cont-1609023-10703582-181430-hd.mp4'
# 加上请求头，伪装成浏览器
# 原来浏览器请求头：{'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# 服务器返回数据，视频数据
response = requests.get(mp4_url, headers=headers)
# 网页编码 请求头 服务器的链接数据（应对乱码问题）
# response.encoding=response.apparent_encoding
"""#手动关闭文件
 
f = open('工业飞速发展，彰显我们国家实力！.mp4', mode='wb')
# 二进制数据
f.write(response.content)
f.close()"""
# 自动关闭文件
with open('./res' + '/工业飞速发展，彰显我们国家实力！.avi', mode='wb') as f:
    f.write(response.content)
print(response)

