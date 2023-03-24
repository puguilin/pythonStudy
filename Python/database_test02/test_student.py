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
    config.read('config/dbConfig.ini', encoding="utf-8-sig")  # 防止中文乱码
    dbinfo.update({"database": config['mysql']['database']})
    dbinfo.update({"host": config['mysql']['host']})
    dbinfo.update({"user": config['mysql']['user']})
    dbinfo.update({"password": config['mysql']['password']})
    dbinfo.update({"port": config['mysql']['port']})


# 根据id条件查询学生信息
def get_test_student(id):
    print("程序开始执行时间" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 程序开始执行时间2023-03-24 10:41:23
    # sql_str = '''
    #        select * from  student where  ID = '{}'   两种方式都可以
    #       '''
    sql_str = '''
             select * from  student where id = {}
            '''
    sql = sql_str.format(id)
    df = sqlh.querysql_one(sql)
    # print("查询结果输出为  ", df)
    logger.logger.info("根据id查询学生结果为 :{}".format(df))


# 查询所有学生信息
def get_test_student_all():
    sql_str = '''
           select * from  student 
          '''
    df = sqlh.querysql_all(sql_str)
    logger.logger.info("logger 查询所有学生信息结果为 :{}".format(df))


# 根据数组查询所有学生信息
def get_query_all_arr(ids):
    sql_str = '''
           select * from  student  where id in {}
          '''
    sql = sql_str.format(ids)
    df = sqlh.query_all_arr(sql)
    logger.logger.info("logger 根据数组查询所有学生信息 :{}".format(df))


# 新增学生记录数据信息   insert插入变量用 '{}' 替代 多个参数变量也是一样的 注意下面 format中参数的顺序
def db_pd_insert():
    no = '16'
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print("insert数据 程序开始执行时间" + date_time)  # 程序开始执行时间2023-03-24 10:41:23
    insert_sql = '''
        INSERT INTO student ( SNO, SNAME, SSEX, createDate, updateDate, remark) VALUES( '{}', 'python新增', '男', '{}' , null, 'python新增01')
        '''
    sql = insert_sql.format(no, date_time)  # insert插入变量用 '{}' 替代  注意下面 format中参数的顺序
    res = sqlh.executesql(sql)
    logger.logger.info("成功新增了:{} 一条 学生信息 ".format(res))


def db_pd_insert_dict(dict_ars):
    insert_sql_dict = '''
           INSERT INTO student ( SNO, SNAME, SSEX, createDate, updateDate, remark) VALUES( '{}', '{}', '{}', '{}' , '{}' ,'{}')
           '''
    sql = insert_sql_dict.format(dict_ars['SNO'], dict_ars['SNAME'], dict_ars['SSEX'], dict_ars['createDate'],
                                 dict_ars['updateDate'], dict_ars['remark'])
    res = sqlh.executesql(sql)
    logger.logger.info("通过字典dict形式新增了:{} 一条记录 新增学生信息是:{} ".format(res, dict_ars))


def db_pd_delete(id):
    delete_sql = '''
        delete from student where id = '{}'
    '''
    sql = delete_sql.format(id)
    res = sqlh.executesql(sql)
    logger.logger.info("成功删除id为:{} 的共:{}条 学生信息记录 ".format(id, res))


if __name__ == '__main__':
    _init_db()
    # 数据库连接初始化
    sqlh = Mysqlpython(dbinfo["database"], dbinfo["host"], dbinfo["user"], dbinfo["password"], int(dbinfo["port"]))
    engine_str = 'mysql+pymysql://' + dbinfo['user'] + ':' + dbinfo['password'] + '@' + dbinfo['host'] + ':' + dbinfo[
        'port'] + '/' + dbinfo['database'] + '?charset = utf8'
    engine = create_engine(engine_str)

    # 根据id查询学生信息
    # get_test_student(120)

    # 查询所有学生信息
    # get_test_student_all()

    # 插入一条记录
    # db_pd_insert()

    # 字典形式的插入一条记录
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dict_ars = {'SNO': '15', 'SNAME': 'python_dict增加记录', 'SSEX': '女', 'createDate': date_time, 'updateDate': date_time,
                'remark': 'python_dict增加记录'}
    db_pd_insert_dict(dict_ars)

    # 根据数组查询多条
    # id = ["116", "117"]
    # # id = [116, 117] # 两种方式都可以
    # ids = tuple(id)    # ids = ("116", "117")  转化为元组 应为后面参数 .format只能是字符串
    # get_query_all_arr(ids)

    # 删除一条记录
    # db_pd_delete(43)
