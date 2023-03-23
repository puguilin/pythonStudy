#!/usr/bin/env python
# coding=utf-8


from sqlalchemy import create_engine
from config.propater import Mysqlpython
import configparser
import time
from util_tools import logger

dbinfo = {}


# 初始化数据库配置
def _init_db():
    config = configparser.ConfigParser()
    config.read('dbConfig.ini', encoding="utf-8-sig")  # 防止中文乱码
    dbinfo.update({"database": config['mysql']['database']})
    dbinfo.update({"host": config['mysql']['host']})
    dbinfo.update({"user": config['mysql']['user']})
    dbinfo.update({"password": config['mysql']['password']})
    dbinfo.update({"port": config['mysql']['port']})


# 根据id条件查询学生信息
def get_test_student():
    print("程序开始执行时间")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    sqlStr = '''
           select * from  student where  ID = 117
          '''
    df = sqlh.querysql_one(sqlStr)
    print("查询结果输出为  ", df)
    logger.logger.info("logger 查询学生结果为 :{}".format(df))



if __name__ == '__main__':
    _init_db()
    # 数据库连接初始化
    sqlh = Mysqlpython(dbinfo["database"], dbinfo["host"], dbinfo["user"], dbinfo["password"], int(dbinfo["port"]))
    engine_str = 'mysql+pymysql://' + dbinfo['user'] + ':' + dbinfo['password'] + '@' + dbinfo['host'] + ':' + dbinfo[
        'port'] + '/' + dbinfo['database'] + '?charset = utf8'
    engine = create_engine(engine_str)
    get_test_student()
