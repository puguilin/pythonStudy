
# 你可以使用下面的导入方式
# from ... import *

# 1 不建议你这么做，使用这种方式会将目标模块里的所有内容都导入，除了以下划线开始的变量。
# 使用这种方式导入模块，会导入很多你原本不需要的东西，比如函数，类，造成一些不必要的麻烦。
# 如果你编写的模块可能会被其他人使用，你可以通过在模块里定义列表__all__
# 来防止对方导入不需要的模块或者你不希望被其他人导入的模块。

def check_phone(phone):
    print('check_phone')

def check_id_no(id_no):
    print('check_phone')

__all__ = []

# 定义__all__为空列表，如果其他模块在导入my_utils模块时使用from ... import *的方式，那么任何内容都无法正常导入，逼迫对方导入指定的函数
#
# from my_utils import check_phone
# 即便__all__是空列表，只要导入模块时指定要导入的函数就可以通过编译。
#
# 如果你想稍稍放开限制，允许其他人是用from ... import *的方式，但是限制可以导入的内容，
# 那么只需要在__all__填写你允许被* 导入的内容即可，比如你允许导入check_phone 函数，那么可以这样来定义
#
# __all__ = ['check_phone']
# 这样，即便使用了from ... import *的方式，也只能导入check_phone这一个函数
#
# from my_utils import *
# check_phone('')
# 使用其他函数都是不被允许的。
