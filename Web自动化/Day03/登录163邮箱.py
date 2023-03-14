from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://mail.163.com/")
driver.maximize_window()
iframe = driver.find_element(By.XPATH,'//iframe[contains(@id,"x-URS-iframe")]')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,"//input[contains(@id,'auto-id')]").send_keys('ppeterjian')
driver.find_element(By.NAME,'password').send_keys('')
driver.find_element(By.NAME,'un-login').click()
driver.find_element(By.ID,'dologin').click()
time.sleep(5)
driver.find_element(By.XPATH,"//li/span[contains(text(),'写')]").click()
# driver.find_element(By.XPATH,"//a[contains(@id,'_mail_emailcontainer_')]").send_keys("996805873@qq.com")
# time.sleep(5)

driver.quit()