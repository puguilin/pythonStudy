from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

html = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'html', 'frame.html')
driver = webdriver.Chrome()
driver.get(html)
f1 = driver.find_element(By.ID,'f1')
driver.switch_to.frame(f1)
print(driver.find_element(By.XPATH,'//h3').get_attribute('outerHTML'))
# frame嵌套需要一层层去定位
f2 = driver.find_element(By.ID,'f2')
driver.switch_to.frame(f2)
# print(driver.find_element(By.XPATH, '//iframe').get_attribute('outetHTML'))
# 切换到父级
driver.switch_to.parent_frame()
# 切换到主页面
driver.switch_to.default_content()
sleep(2)
driver.quit()
