from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
input = driver.find_element(By.XPATH,'//form/span/input')
print(input.get_attribute('outerHTML'))
driver.quit()