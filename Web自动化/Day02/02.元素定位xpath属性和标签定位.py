from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
kw = driver.find_element(By.XPATH,"//input[@id='kw']")
print(kw.get_attribute("outerHTML"))
# driver.quit()
su = driver.find_element(By.XPATH,"//input[@id='su']")
print(su.get_attribute('outerHTML'))
driver.quit()