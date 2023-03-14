from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print(driver.find_element(By.XPATH, '//input[@id="kw" and @name="wd"]').get_attribute("outerHTML"))
driver.quit()