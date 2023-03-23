# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 9:48
# @Author  : pgl
# @File    : db_test.py
# @IDE     : PyCharm  创建连接数据库对象，并获取表的内容
import traceback

import pymysql
import datetime
import random
import re
import shlex
from threading import Lock
from pandas import DataFrame
from sqlalchemy import create_engine
import pandas as pd
from config.config import get_value
from util_tools import logger


RE_INSERT_VALUES = re.compile(r"\s*((?:INSERT|REPLACE)\b.+\bVALUES?\s*)(\(.*\))", re.IGNORECASE | re.DOTALL, )


class DbBase_test:

    _mysql_passwd = get_value('db_info', 'db_passwd_str')
    _sqlalchemy_passwd = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'. \
        format(**eval('dict(' + _mysql_passwd + ')'))
    _engine = create_engine(_sqlalchemy_passwd)
    _conn = eval('pymysql.connect(' + _mysql_passwd + ')')

    # 增加线程锁功能，多线程时用到
    lock = Lock()

    def __init__(self):
        pass

    def db_pd_read(self, sql) -> DataFrame:
        """
        通过dataframe自己的方法，将数据督导df里
        """
        df = pd.read_sql(sql, con=self._engine.connect())
        return df

    def db_pd_insert(self, df, table_name):
        """
        通过dataframe自己的方法，insert数据，如果表存在，就追加，不存在就创建
        """
        df.to_sql(table_name, self._engine, index=False, if_exists='append', chunksize=10000)

    def db_pd_replace_insert(self, df, table_name):
        """
        通过dataframe自己的方法，insert数据，如果表存在，就删除替换，不存在就创建
        """
        df.to_sql(table_name, self._engine, index=False, if_exists='replace', chunksize=10000)

        # 单条更新命令

    def get_count(self, sql) -> int:
        # type: (str) -> int
        """执行count查询，返回count值，int"""
        try:
            # 通过pymysql获取mysql的数据连接
            _cur = self._conn.cursor()
            _curs = _cur.execute(sql)
            count = _cur.fetchall()[0][0]
            return count
        except Exception as e:
            logger.logger.error('执行count查询，返回count值：:{}'.format(e))
            try:
                _cur.close()
                self._conn.close()
            except Exception as e:
                logger.logger.error('关闭数据库连接失败：:{}' .format(e))
        finally:
            _cur.close()
            self._conn.close()

        # 单条更新命令
        def execute(self, sql, params) -> None:
            """单条插入数据库，传入的参数只是只有一行的list"""
            try:
                # 通过pymysql获取mysql的数据连接
                _cur = self._conn.cursor()
                _cur.execute(sql, params)
                self._conn.commit()
            except Exception as e:
                logger.logger.error('insert或更新数据信息失败：:{}' .format(e))
                try:
                    self._conn.rollback()
                    _cur.close()
                except Exception as e:
                    logger.logger.error('关闭数据库连接失败：:{}' . format(e))
            finally:
                _cur.close()

        # 批量更新命令
        def executemany(self, sql, data_list: []) -> None:
            """
            批量插入数据库，传入的参数必须是一个list,同时，每一条记录是一个Tuple
            但是有一个bug，updae不能批量，如果变量里不是都是%是%s，也不会走批量！
            切记！
            """
            try:
                # 通过pymysql获取mysql的数据连接
                _cur = self._conn.cursor()
                _cur.executemany(sql, data_list)
                self._conn.commit()
            except Exception as e:
                logger.logger.error('insert或更新数据信息失败：:{}' . fromat(e))
                try:
                    self._conn.rollback()
                    _cur.close()
                except Exception as e:
                    logger.logger.error('关闭数据库连接失败：:{}' .format(e))
            finally:
                _cur.close()

        # executemany不好用的时候，批量insert
        def insert_many(self, sql, data_list: [], _arraysize=1000) -> None:
            # type: (str, list) -> None
            """
            一定要注意，传进来的list是tuple类型的list
            有些时候，insert的时候需要有一些固定值，这样就导致了无法做到使用类库自带的批量更新
            只能自己写一个，能支持单次的最大条数，取决于mysql数据库的max_allowed_packet的大小

            """
            if not data_list:
                return
            m = RE_INSERT_VALUES.match(sql)
            if m:
                q_prefix = m.group(1) % ()
                q_values = m.group(2).rstrip()

            num = 0
            strs = ''
            new_sql = ''
            for line in data_list:
                num = num + 1
                # 针对非数字类型不加引号，其它类型要加上引号
                line = [x if type(x) == int or x == 'NUll' or x == 'null'
                        else "\'" + str(x) + "\'" for x in line]
                strs = strs + str(q_values % tuple(line)) + ','
                # 每5000条提交一次
                if num > _arraysize:
                    strs = strs.rstrip(',') + ';'
                    new_sql = q_prefix + strs
                    self.execute(new_sql)
                    strs = ''
                    new_sql = ''
                    num = 0
            if num > 0:
                strs = strs.rstrip(',') + ';'
                new_sql = q_prefix + strs
                self.execute(new_sql)

        # executemany不好用的时候，批量delete
        def delete_many(self, sql, data_list: [], _arraysize=1000) -> None:
            # type: (str, list, int) -> None
            """
            一定要注意，传进来的list是tuple类型的list
            delete很慢，没有起到真正批量的形式，所以决定自己写一个，批量的模型选用in的方式
            也就是需要前面传入的sql串，针对要删除的字段，采用in的模型
            能支持的最大条数，取决于mysql数据库的max_allowed_packet的大小,sql写法：
            sns = "delete from  order_data_test where (contact_id,group_id) in (%s) "
            sns = "delete from  order_data_test where contact_id in (%s) "
            """
            if not data_list or sql.lower().find(" in ") < 0:
                return
            num = 0
            strs = ''
            new_sql = ''
            for line in data_list:
                num = num + 1
                if (type(line) == tuple or type(line) == list) and len(line) > 1:
                    strs = strs + str(tuple(line)) + ','
                else:
                    if type(line) == int or line == 'NUll' or line == 'null':
                        pass
                    elif type(line) == list or type(line) == tuple:
                        line = '\'' + str(line[0]) + '\''
                    else:
                        line = '\'' + str(line) + '\''
                    strs = strs + str(line) + ','
                # 每5000条提交一次
                if num > _arraysize:
                    strs = strs.rstrip(',')
                    new_sql = sql % strs
                    self.execute(new_sql)
                    strs = ''
                    new_sql = ''
                    num = 0
            if num > 0:
                strs = strs.rstrip(',')
                new_sql = sql % strs
                # logger(new_sql)
                self.execute(new_sql)

    def update_many(self, sql, data_list: [], col_num) -> None:
        # type: (str, list, int) -> None
        """
        col_num ： 把传入数据的第几列作为索引列，很重要，数据量大了，一定要指定索引列
        比如你传的list总共有3列，如果第二列是关键索引列，那就传2，update_many(sql,list,2)
        批量update，不支持特别复杂的多表关联的update，只支持单表update
        通过创建临时表的方式，进行update操作
        临时表的名字_neusoft_update_temp_x，用完下次再用，就会干掉
        目前不支持多进程，不支持多进程!!
        """
        if not data_list or sql.lower().find("where") < 0:
            logger.logger.info("update语句没有where条件，或者没有值，请检查！")
            return
        # 临时表
        uniqueNum = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(0, 10000)).zfill(5)
        temp_table = '_update_temp_' + uniqueNum
        # temp_table = '_update_temp_' + datetime.datetime.now().strftime("%Y%m%d")
        # 获取sql需要多少变量
        count = sql.count("%s")
        # 把数据转化为df
        df = pd.DataFrame(data_list)
        # 成建表需要的列
        column = ['_xxx_' + str(i + 1) for i in range(count)]
        df.columns = column
        try:
            # 创建表并插入数据
            self.db_pd_replace_insert(df, temp_table)
            if not col_num or col_num > count:
                logger.logger.info('没有指定索引，或者指定的索引超过列的最大个数')
            else:
                # 哪列是索引列，很关键，决定了更新的速度
                creat_index_str = "CREATE INDEX _update_temp_%s_IDX USING BTREE " \
                                  "ON %s(`%s`(250));" % (col_num, temp_table, column[col_num - 1])
                logger.info('开始创建索引：%s' % creat_index_str)
                # 创建索引
                self.execute(creat_index_str)
            # 把sql串解析为list表
            sql = re.sub(r"(\s*=\s*)", "=", sql)
            sql = sql.replace(',', ' ')
            sql_list = shlex.split(sql.lower())
            # logger(sql_list)
            # 获取第几列的位置
            num = 0
            # 循环次数,没有别名，从3开始
            index = 3
            # 判断表有没有别名
            if sql_list[2] == 'set':  # 没有别名
                sql_list[1] = sql_list[1] + ' a, ' + temp_table + ' b'
                # 第一次循环，循环到where前
                for i in sql_list[index:]:
                    if i == 'where':
                        sql_list[index - 1] = sql_list[index - 1].rstrip(',')
                        break
                    if i.find("%s") > 0:
                        sql_list[index] = 'a.' + i.split('=')[0] + ' = b.' + column[num] + ','
                        num = num + 1
                    else:
                        sql_list[index] = 'a.' + i + ','
                    index = index + 1

                # 第二次循环，从where后开始
                index = index + 1
                for i in sql_list[index:]:
                    # 如果有绑定变量，就更改赋值
                    if i.find("%s") > 0:
                        sql_list[index] = 'a.' + i.split('=')[0] + ' = b.' + column[num]
                        num = num + 1
                    elif i.find("=") > 0:
                        sql_list[index] = 'a.' + i
                    index = index + 1

            else:  # 如果原来的sql语句中的表有别名
                # 循环次数,没有别名，从4开始
                index = 4
                sql_list[2] = sql_list[2] + ' , ' + temp_table + ' b'
                # 第一次循环，循环到where前
                for i in sql_list[index:]:
                    if i == 'where':
                        sql_list[index - 1] = sql_list[index - 1].rstrip(',')
                        break
                    if i.find("%s") > 0:
                        sql_list[index] = i.split('=')[0] + ' = b.' + column[num] + ','
                        num = num + 1
                    else:
                        sql_list[index] = i + ','
                    index = index + 1

                # 第二次循环，从where后开始
                index = index + 1
                for i in sql_list[index:]:
                    # 如果有绑定变量，就更改赋值
                    if i.find("%s") > 0:
                        sql_list[index] = i.split('=')[0] + ' = b.' + column[num]
                        num = num + 1
                    index = index + 1
            new_sql = ' '.join(sql_list)
            # 去掉最后一个可能存在的逗号20220328
            # new_sql = new_sql.rstrip(',')
            logger(new_sql)
            self.execute(new_sql)
        except Exception as e:
            logger.logger.info('update数据信息失败：' + str(e.args))
        finally:
            # 删除临时表
            sql = "drop table %s" % temp_table
            self.execute(sql)

        # 单条更新命令--多线程
        def execute_mutiThread(self, sql, params) -> None:
            """单条插入数据库，传入的参数只是只有一行的list"""
            try:
                # 通过pymysql获取mysql的数据连接
                self.lock.acquire()
                _cur = self._conn.cursor()
                _cur.execute(sql, params)
                self._conn.commit()
                self.lock.release()
                self._conn.close()
            except Exception as e:
                logger.logger.error('insert或更新数据信息失败：:{}' .format(e))
                try:
                    self._conn.rollback()
                    _cur.close()
                    self._conn.close()
                except Exception as e:
                    logger.logger.error('关闭数据库连接失败：:{}' .format(e))
                finally:
                    _cur.close()
                    self.lock.release()
                    self._conn.close()
            finally:
                _cur.close()
                self.lock.release()
                self._conn.close()

        # 单条更新命令

    def execute(self, sql) -> None:
        """单条插入数据库，传入的参数只是只有一行的list"""
        try:
            # 通过pymysql获取mysql的数据连接
            _cur = self._conn.cursor()
            _cur.execute(sql)
            self._conn.commit()
        except Exception as e:
            logger.logger.error('insert或更新数据信息失败：:{}' .format(e))
            try:
                self._conn.rollback()
                _cur.close()
                # self._conn.close()
            except Exception as e:
                logger.logger.error('关闭数据库连接失败：:{}' .format(e))
