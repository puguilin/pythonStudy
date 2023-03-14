# 导入包
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问百度
driver.get("https://www.baidu.com")
# 休眠
sleep(5)
driver.quit()
