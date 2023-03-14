from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
print(driver.name)
print(driver.current_url)
print(driver.current_window_handle)
driver.find_element(By.LINK_TEXT,'新闻').click()
# 获取所有的句柄
print(driver.window_handles)
# 获取源码
# print(driver.page_source)
driver.quit()