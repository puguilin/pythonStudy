from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 等待返回True，如果等待还返回False,进行报错
# result = WebDriverWait(driver,10,0.5).until(lambda x:True if x.title == '百度一下你就知道' else False,message='标题一致')
# print(result)
# 等待返回结果False，如果等待返回True，进行报错
# result1 = WebDriverWait(driver,8,0.5).until_not(lambda x:True if x.title == '百度一下你就知道' else False,message='标题正确')
result1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element(*locals))
print(result1)
sleep(5)
driver.quit()
# 针对一个元素等待，加载完成即可运行后续代码
# 多个元素需要素设置等待