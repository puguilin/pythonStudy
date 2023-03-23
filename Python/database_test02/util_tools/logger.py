#!/usr/bin/env python
# coding=utf-8
'''
# 程序作用：获取输出日志对象.
# 使用方法:直接导入包如from util_tools.logs import logger
# logger.info('正在读取配置')
'''

import logging
import time
from logging.handlers import TimedRotatingFileHandler
import threading
import os
from setconfig import get_config



class SigLog(object):
    '''
    初始化多进程的logger信息
    #在创建一个类对象实例的过程中，new()方法作用在构造方法__init__()之前。
    # new()函数执行后会返回实例对象（self），然后将self作为第一个参数传给该类的初始化方法__init__()方法。
    '''

    def __init__(self):
        pass

    def __new__(cls):
        mutex = threading.Lock()
        mutex.acquire()  # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(SigLog, cls).__new__(cls)
            config = get_config('LOGGING')
            cls.instance.log_dir = config.get('log_file')
            # 获取程序的基础路径
            base_dir = os.path.split(os.path.dirname(__file__))[0]
            log_dir = os.path.join(base_dir, 'logs')
            file_name = config.get('logger_name') + '_' + time.strftime('%Y%m%d', time.localtime()) + '.logs'

            # 如果存在日志配置信息

            if not os.path.exists('../logs'):  # 如果不存在，创建文件目录
                os.mkdir('../logs/')

            # if cls.instance.log_dir:
            #     if not os.path.exists(cls.instance.log_dir):
            #         print('日志路径不存在，终止程序')
            #         exit()
            #     log_dir = cls.instance.log_dir

            cls.instance.log_filename = os.path.join(log_dir, file_name)

            cls.instance.max_bytes_each = int(config.get('max_bytes_each'))
            cls.instance.backup_count = int(config.get('backup_count'))
            cls.instance.fmt = config.get('fmt')
            cls.instance.datefmt = config.get('datefmt')
            cls.instance.log_level_in_console = int(config.get('log_level_in_console'))
            cls.instance.log_level_in_logfile = int(config.get('log_level_in_logfile'))
            cls.instance.logger_name = config.get('logger_name')
            cls.instance.console_log_on = int(config.get('console_log_on'))
            cls.instance.logfile_log_on = int(config.get('logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
            # logging包默认对输出分成了6个等级,如果我们在设置默认格式的时候设置的等级比之后调用是的要高，那么调用的logging语句将不会输出；
            # 反之，输出时默认等级也会被调用语句的等级覆盖。
            # 所以要先设置一个第一点的默认值，但是这个值不能不设置，因为为空也不输出
            cls.instance.logger.setLevel(1)
        mutex.release()
        return cls.instance

    def get_logger(self):
        '''
        logger设置的时候，要设置如下的值。logger.setLevel代表最上层
        logger.setLevel(level=logging.INFO)
        handler.setLevel(logging.INFO)
        console.setLevel(logging.INFO)
        '''
        return self.logger

    def __config_logger(self):
        # 设置日志格式
        formatter = logging.Formatter(self.fmt, self.datefmt)

        # 如果开启控制台日志
        if self.console_log_on == 1:
            # StreamHandler -> 控制台输出
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            console.setLevel(self.log_level_in_console)
            self.logger.addHandler(console)
        # 如果开启文件日志
        if self.logfile_log_on == 1:
            # RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
            # TimedRotatingFileHandler -> 按照时间自动分割日志文件
            rt_file_handler = TimedRotatingFileHandler(self.log_filename, when='D', interval=1,
                                                       backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            rt_file_handler.setLevel(self.log_level_in_logfile)
            self.logger.addHandler(rt_file_handler)


signletonlog = SigLog()

logger = signletonlog.get_logger()
