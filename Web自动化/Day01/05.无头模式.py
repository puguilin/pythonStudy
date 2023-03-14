from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument('-headless')
driver = webdriver.Chrome(options=options)
driver.get("http://www.zhongxicloud.com/")
sleep(3)
print(driver.title)
sleep(1)
driver.quit()
