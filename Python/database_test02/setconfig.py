#!/usr/bin/env python
# coding=utf-8
'''
# 作者：lihuag@neusoft.com
# 软件开发时间：2022年3月9日
# 程序作用：实现数据文件的读取
# 使用方法:
# version： 1.0
# 最近修改时间：2022年3月9日
'''
import configparser
import os


def get_config(section):
    """
    根据要取的项目，获取所有的参数列表
    :param section:
    :return: 包含列表的字典
    """
    # 读取配置文件,利用程序执行的路径，获取配置文件的位置
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, 'dbConfig.ini')
    # 生成ConfigParser对象
    config = configparser.ConfigParser()
    # 读取配置文件
    config.read(config_path, encoding='utf-8')
    dict = {}
    for i in config.options(section):
        dict.update({i: config.get(section, i)})
    return dict


def get_values(section, value_name):
    '''
    根据要取的项目参数名称，获取具体的值
    :param section: 配置的模块名称
    :param value_name: 配置的参数名称
    :return: 具体配置的值
    '''
    # 读取配置文件中某个配置文件的值
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, 'dbConfig.ini')
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    config.get(section, value_name)
    return config.get(section, value_name)
