# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 10:03
# @Author  : pgl
# @File    : test_student_sql.py
# @IDE     : PyCharm

import sys

sys.path.append("..")
from database.db_test import DbBase_test
from sqlalchemy import text  # 引入text 函数 这个是用来防止 返回查询结果 为 select  * 时报错



class DataSourceSql:

    def __init__(self):
        pass

    def _get_test_student(self):
        sqlStr = '''
         select * from  student /*where  ID = 117*/
        '''
        df = DbBase_test().db_pd_read(text(sqlStr))
        return df

    def _get_count(self):
        sqlStr = '''
                select count(*) from  student
               '''
        df = DbBase_test().get_count(sqlStr)
        return df
