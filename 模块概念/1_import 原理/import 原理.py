
# python中有大量第三方库可用“pip install 。。。”进行有需要的安装
# 在使用库函数时，需要导入，有两种方法：
#   1. import 模块名【as 别名】
# 使用这种方式导入后，需要在使用的对象前加上前缀 “模块名 . 对项名”的方式进行访问，也可以用“别名 . 对象名”的方式使用其中的对象
#   2.from 模块名 import 对象名【as 别名】
# 使用这种方式仅导入使用的对象，并且可以为这个对象起一个别名，这种方法可以减少查询次数，减少程序员的代码量，不需要使用模块名作为前缀

import math
from math import sin as f

print(math.sin(3))
print(f(3))




# 1. 导入过程
# 执行import语句时，只有两个步骤，第一步是搜索模块，第二步是将搜索结果绑定到局部命名空间。

# 搜索时，分为两步：
#
# 搜索sys.modules
# 搜索sys.meta_path
# 导入一个模块时，会将这个导入的模块以及这个模块里调用的其他模块信息以字典的形式保存到sys.modules中，
# 如果再次导入词模块，则优先从sys.modules查找模块，你可以在脚本里执行print(sys.modules)查看已经加载的模块,我们甚至可以直接修改sys.modules里的内容
import os
import sys

sys.modules['fos'] = os
import fos
print(fos.getpid())

# 执行import fos时，会先到sys.modules里查找是否有该模块，'fos'做key,找到的value是os模块，因此可以调用getpid方法。
#
# 如果在sys.modules模块中找不到目标模块，则从sys.meta_path中继续寻找。
# sys.meta_path是一个list，里面的对象是importer对象，importer对象是指实现了finders 和 loaders 接口的对象，
# 输出sys.meta_path里的内容可以查看有什么

#   <class '_frozen_importlib.BuiltinImporter'>
#   <class '_frozen_importlib.FrozenImporter'>
#   <class '_frozen_importlib_external.PathFinder'>
# 这三个importer对象分别查找及导入build-in模块，frozen模块（即已编译为Unix可执行文件的模块），
# import path中的模块，如果都找不到，就会报ModuleNotFoundError的错误。

# 2. sys.path
# 导入模块时，首先会去sys.modules里查看，如果查不到会使用sys.meta_path里的importer继续查找，
# 这些importer首先会查找内置模块，然后查找frozen模块，最后会根据sys.path里的路径进行查找。

# 3. import hooks
# 我们可以通过一些技术手段来扩展import的行为，为了让你有一个直观的理解，推荐一个第三方库pypi,此模块实现了一个神奇的功能，你可以在代码里导入根本不存在的模块，
# 遗憾的是还不能使用pip来安装这个模块，你可以直接将pypi.py文件放在site-packages文件下或者直接放在项目里，

