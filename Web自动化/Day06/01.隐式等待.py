# 页面或者元素未加载，通过我们指定的时间继续等待，如果超出我们指定的时间还未加载出来抛出异常
# 如果没有需要等待已经加载完成则不需要等到
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(1111)
driver.refresh()
driver.back()
driver.forward()
# driver.find_element(By.ID,'kww').click()
# print(kw.get_attribute("outerHTML"))
driver.quit()
