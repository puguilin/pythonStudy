import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/selectTest.htm")
# s1 = driver.find_element(By.ID,'s1')
# # select = Select(s1)
# s1.find_element(By.XPATH,"//select[@id='s1']/option[2]").click()
# time.sleep(2)
# driver.quit()
s2 = driver.find_element(By.ID,'s1')
select = Select(s2)
# 通过索引来定位
select.select_by_index(1)
time.sleep(2)
# driver.quit()
# 通过option
select.select_by_value("49")
time.sleep(2)
select.select_by_visible_text("Mail")
driver.quit()