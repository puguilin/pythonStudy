import configparser
import os
import shutil
import sys
import time


def create_file_path(dir_name, file_name):
    '''传入目录名和文件名，在程序根目录创建目录和文件，并返回文件名称的绝对路径
        :param dir_name: 要创建的目录名
        :param file_name: 要创建的目文件名
        :return: 文件名称的绝对路径
    '''
    # 获取程序的基础路径
    root_dir = os.path.split(os.path.dirname(__file__))[0]
    base_dir = os.path.join(root_dir, dir_name)
    # 如果如果目录不存在，创建
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return os.path.join(base_dir, file_name)


def get_format_time(format='%Y-%m-%d %H:%M:%S'):
    '''
    获取现行时间格式化后的时间文本
    :param format: 传入format，默认为%Y-%m-%d %H:%M:%S
    【常用format代码指引】
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
    :return: 返回现行时间格式化后的文本字符串
    '''
    return time.strftime(format, time.localtime())


# cron时间表达式相关操作包

'''
 文件挪目录
 srcfile:需要挪的文件，带上目录
 dstpath：挪到的目标目录
 '''


def movefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件


# 获取指定目录下的文件名
def getFileName(workDir):
    L = []
    try:
        for file in os.listdir(workDir):
            print('filename===', file)
            L.append(file)
    except:
        print('不存在' + workDir + '目录')
    return L
