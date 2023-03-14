
# 1. __import__
# 当你使用import关键字导入模块时，底层实现默认调用的是__import__，
# 直接使用该函数的情况很少见，一般用于动态加载。假设有这样一个场景，项目里有两份配置文件，一份是线下开发环境配置
# 不同的环境需要加载不同的配置文件，这种情况就可以使用__import__来动态加载
# 在mac电脑上执行这段代码时将加载offline模块，其他系统上会加载online模块。如下所示

import platform

if platform.uname().system == 'Darwin':     # mac电脑
    config = __import__('conf.offline')
else:
    config = __import__('conf.online')

print(config)


# 2. fromlist
# __import__有很多参数，其中name是必须的，其他参数中fromlist是一个比较重要的参数。在第一节的示例中，两份配置文件与引入模块的文件在同一个文件夹下，现在，我更改项目结构
#
# ├── conf
# │   ├── __init__.py
# │   ├── offline.py
# │   └── online.py
# └── demo.py
# 继续使用上面的方法则需要修改 __import__函数中的name 需要使用fromlist参数

if platform.uname().system == 'Darwin':     # mac电脑
    config = __import__('conf.offline', fromlist=('offline'))
else:
    config = __import__('conf.online', fromlist=('online'))

print(config)

# 3. importlib.import_module
# importlib模块的import_module方法相比于__import__更加友好，使用起来更加方便。下图是项目的结构
#
# ├── conf
# │   ├── __init__.py
# │   ├── offline.py
# │   └── online.py
# └── demo.py
# 在文件中根据系统来加载不同的模块，使用import_module方法的示例代码如下
# 使用相对导入时，务必在name前面加一个点
import importlib

if platform.uname().system == 'Darwin3':     # mac电脑
    config = importlib.import_module('conf.offline')    # 绝对导入
else:
    config = importlib.import_module('.online', package='conf')     # 相对导入

print(config.host)





