import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
result = WebDriverWait(driver,10,1).until(EC.title_is('百度一下，你就知道'),message='超时报错')
print(result)

time.sleep(2)
driver.quit()

