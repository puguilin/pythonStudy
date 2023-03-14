from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://hmshop-test.itheima.net/Home/user/login.html")
input = driver.find_elements(By.TAG_NAME, 'input')
input[0].send_keys('15800000001')
input[1].send_keys('123456')
input[2].send_keys('8888')
sleep(5)
driver.find_element(By.XPATH, '//a[@name="sbtbutton"]').click()

sleep(5)
driver.quit()
