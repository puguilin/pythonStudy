
# python的第三方库会被安装在site-packages文件夹中，这是很多人都知道的事情，但这个文件夹又在哪里呢？
# 当你的系统里安装了好几python的版本时，往往会搞不清楚自己当前所用的python的目录是哪里，想要进入到site-packages进行一些操作，却发现自己根本不知道。
# 找到所用的python安装目录是一个非常简单的事情，这里给大家介绍两种方法

# 方法1，通过sys.path
# 在交互式解释器里，import sys，然后输出sys.path的内容
# Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> sys.path
# ['', 'D:\\python\\python36.zip', 'D:\\python\\DLLs', 'D:\\python\\lib', 'D:\\python',
# 'D:\\python\\lib\\site-packages', 'D:\\python\\lib\\site-packages\\utility-0.1.9-py3.6.egg',
# 'D:\\python\\lib\\site-packages\\requests-2.21.0-py3.6.egg', 'D:\\python\\lib\\site-packages\\kazoo-2.7.0-py3.6.egg',
# 'D:\\python\\lib\\site-packages\\urllib3-1.24.3-py3.6.egg', 'D:\\python\\lib\\site-packages\\idna-2.8-py3.6.egg',
# 'D:\\python\\lib\\site-packages\\chardet-3.0.4-py3.6.egg', 'D:\\python\\lib\\site-packages\\certifi-2020.4.5.1-py3.6.egg',
# 'D:\\python\\lib\\site-packages\\win32', 'D:\\python\\lib\\site-packages\\win32\\lib', 'D:\\python\\lib\\site-packages\\Pythonwin']

# sys.path包含的是 python的搜索模块的路径集 ，当我们在脚本里执行import语句时，会在sys.path的路径中依次进行查找。

# 方法2，使用sysconfig

# sysconfig模块可以获得python的许多配置参数，在shell里执行
# python -m sysconfig
# 即可获得当前所用python的详细配置参数
# Platform: "win-amd64"
# Python version: "3.6"
# Current installation scheme: "nt"
# ​
# Paths:
#         data = "D:\python"
#         include = "D:\python\Include"
#         platinclude = "D:\python\Include"
#         platlib = "D:\python\Lib\site-packages"
#         platstdlib = "D:\python\Lib"
#         purelib = "D:\python\Lib\site-packages"
#         scripts = "D:\python\Scripts"
#         stdlib = "D:\python\Lib"
# ​
# Variables:
#         BINDIR = "D:\python"
#         BINLIBDEST = "D:\python\Lib"
#         EXE = ".exe"
#         EXT_SUFFIX = ".pyd"
#         INCLUDEPY = "D:\python\Include"
#         LIBDEST = "D:\python\Lib"
#         SO = ".pyd"
#         VERSION = "36"
#         abiflags = ""
#         base_基本语法_grammar01 = "D:\python"
#         exec_prefix = "D:\python"
#         installed_base = "D:\python"
#         installed_platbase = "D:\python"
#         platbase = "D:\python"
#         prefix = "D:\python"
#         projectbase = "D:\python"
#         py_version = "3.6.8"
#         py_version_nodot = "36"
#         py_version_short = "3.6"
#         srcdir = "D:\python"
#         userbase = "C:\Users\zhangdongsheng\AppData\Roaming\Python"
# 输出的信息可能会很多，如果不方便查看，你还可以编写代码输出指定的信息
#
# import sysconfig
# print(sysconfig.get_path("platlib"))  # D:\python\Lib\site-packages
