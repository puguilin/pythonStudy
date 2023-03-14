import unittest
# 实例化加载对象并加载用例，得到套件对象
suite = unittest.TestLoader().discover('.','testdemo*.py')
# runner = unittest.TextTestRunner()
# runner.run(suite)
unittest.TextTestRunner().run(suite)