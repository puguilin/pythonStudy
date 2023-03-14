from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.find_element(By.XPATH, '//a[contains(text(),"hao")]').get_attribute("outerHTML"))
print(driver.find_element(By.XPATH, '//*[contains(@id,"k")]').get_attribute("outerHTML"))
driver.quit()