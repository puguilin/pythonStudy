from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#
# class Weather:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.url = "https://www.sogou.com/"
#
#     def geturl(self):
#         self.driver.get(self.url)
#         sleep(1.5)
#         self.driver.maximize_window()
#         self.driver.find_element(By.ID,'query').send_keys("湖北天气预报")
#         sleep(2)
#         self.driver.find_element(By.ID,'stb').click()
#         sleep(2.25)
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     hubei = Weather()
#     hubei.geturl()
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(1)
inputs = driver.find_elements(By.TAG_NAME, 'input')
sleep(3)
for i in inputs:
    print(i)
sleep(2)
driver.quit()
