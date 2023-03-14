from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 准备配置
mobileEmulation = {"deviceName":"iPhone SE"}
# 创建options对象
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation",mobileEmulation)
driver = webdriver.Chrome(options=options)
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()