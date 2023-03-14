import unittest

# 实例化套件对象unitest.TestSuite()
from web自动化day06.testdemo import TestDemo1

suite = unittest.TestSuite()
# suite.addTest(TestDemo1('test_method1'))
# suite.addTest(TestDemo1('test_method2'))
suite.addTest(unittest.makeSuite(TestDemo1))
# 实例化执行对象unittest.TextTestRunner()
runner = unittest.TextTestRunner()
# 执行对象
runner.run(suite)