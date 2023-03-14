# 1. 单行注释内容，一般写在要注释的上一行，Python解释器将会忽略（快捷键：Ctrl + /）

# 输出
print("测试输出")  # 一般不要这样写在最后

# 1.语法特点
# 1.1 注释规则
# 1.1.1单行注释
# 在IDLE开发环境中,不是pycharm,不是pycharm, 可以使用快捷键Alt+3/Alt+4快捷键添加/取消注释.
# 1.1.2多行注释
# 在Python中将包含在一堆三引号('''......''')或者("""......""")之间, 并且不属于任何语句的内容认为是多注释
# 1.1.3中文编码声明注释

'''
2. 多行注释，单引号
一般用在模块、类、功能说明、文件说明、版权说明等。
'''

"""
多行注释，双引号。
可以在Pycharm 编辑器里 Settings → Editor → File and Code Templates → Python Script添加如下信息，
这样就可以每次创建新文件自带版本信息。

#!/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) ${YEAR} - ${YEAR} pgl, Inc. All Rights Reserved 
#
# @Time    : ${DATE} ${TIME}
# @Author  : pgl
# @File    : ${NAME}.py
# @IDE     : ${PRODUCT_NAME}

"""
