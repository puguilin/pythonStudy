# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/3/7 9:57
# @Author  : pgl
# @File    : test_student.py
# @IDE     : PyCharm  学生信息表

from test_student_sql import DataSourceSql
from util_tools import logger
if __name__ == "__main__":
    # 查询学生信息
    student = DataSourceSql._get_test_student(self="")
    logger.logger.info("查询学生结果为 :{}".format(student))

    count = DataSourceSql._get_count(self="")
    logger.logger.info("统计学生结果为:{} ".format(count))

