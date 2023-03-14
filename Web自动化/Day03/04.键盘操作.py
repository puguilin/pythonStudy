from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
kw = driver.find_element(By.ID,'kw')
sleep(1)
kw.send_keys('天气预报')
kw.send_keys(Keys.CONTROL,'a')
kw.send_keys(Keys.CONTROL,'c')
sleep(5)
driver.get('http://www.so.com')
input = driver.find_element(By.ID,'input')
input.send_keys(Keys.CONTROL,'v')
driver.find_element(By.ID,'search-button').click()
sleep(5)
driver.quit()