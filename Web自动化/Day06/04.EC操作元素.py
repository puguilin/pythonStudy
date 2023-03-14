from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
kw = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
# print(kw)
print(kw.get_attribute("outerHTML"))
driver.quit()