from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
sing_html = os.path.abspath('html')+'\注册实例.html'
driver.get(sing_html)
driver.maximize_window()
inputs = driver.find_elements(By.TAG_NAME,'input')
inputs[0].send_keys('user1')
inputs[1].send_keys('user1')
inputs[2].send_keys('13000000001')
inputs[3].send_keys('111111@qq.com')
time.sleep(5)
driver.find_element(By.XPATH,"//button[contains(text(),'注册用户')]").click()
time.sleep(3)
# 注册用户A
js1 = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js1)
iframe_A = driver.find_element(By.ID,'idframe1')

driver.switch_to.frame(iframe_A)
driver.find_element(By.ID,'userA').send_keys('user2')
driver.find_element(By.ID,'passwordA').send_keys('user2')
driver.find_element(By.ID,'telA').send_keys('13212739000')
driver.find_element(By.ID,'emailA').send_keys('user2@qq.com')
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(text(),'注册用户')]").click()
time.sleep(2)
# B注册
driver.switch_to.parent_frame()
iframe_B = driver.find_element(By.NAME,"myframe2")
driver.switch_to.frame(iframe_B)
# print(driver.find_element(By.ID,'alertB').get_attribute("outerHTML"))
inputs = driver.find_elements(By.TAG_NAME,'input')
inputs[0].send_keys('userB')
inputs[1].send_keys('userB')
inputs[2].send_keys('13212739100')
inputs[3].send_keys('9968@qq.com')
time.sleep(5)
driver.find_element(By.XPATH,"//button[contains(text(),'用户B')]").click()
time.sleep(5)
# driver.quit()
# select标签选择
driver.switch_to.default_content()
s1 = driver.find_element(By.ID,'select')
select = Select(s1)
s1.find_element(By.XPATH,'//select/option[1]').click()
time.sleep(1.5)
s1.find_element(By.XPATH,'//select/option[2]').click()
time.sleep(1)
select.select_by_index(2)
time.sleep(1.3)
select.select_by_visible_text("重庆")
time.sleep(1.5)
select.select_by_value('gz')
time.sleep(2)
driver.quit()