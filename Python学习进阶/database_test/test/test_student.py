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
    # 查询所有学生信息
    student = DataSourceSql._get_test_student(self="")
    # 过滤 ===> 查询学生id是45 和58的学生信息
    stu = student[student["ID"].isin([45, 58])]
    logger.logger.info("过滤 ===> 查询学生id是45 和58的学生信息:{} \n".format(stu))
    logger.logger.info("查询学生结果为 :{} \n".format(student))

    count = DataSourceSql._get_count(self="")
    logger.logger.info("统计学生结果为:{} \n".format(count))

'''
    ID  SNO   SNAME SSEX          createDate updateDate remark
1  45  333  名称5add    F 2023-01-25 17:59:07        NaT     测试
2  58   10  测试新增前端    F 2023-03-30 11:30:00        NaT     备注

查询学生结果为 :    ID     SNO         SNAME  ...          createDate          updateDate remark
0   43  659625           名称3  ... 2023-02-25 17:59:07                 NaT   测试01
1   45     333        名称5add  ... 2023-01-25 17:59:07                 NaT     测试
2   58      10        测试新增前端  ... 2023-03-30 11:30:00                 NaT     备注
3  102  string        string  ... 2023-01-03 09:59:02 2023-01-03 08:59:47   None
4  116      10   测试对象参数 新增前端  ... 2023-01-03 10:45:05                 NaT   备注对象
5  117      11  测试map参数 新增前端  ... 2023-01-03 10:45:28 2023-01-03 08:59:47  备注map



统计学生结果为:6 

'''