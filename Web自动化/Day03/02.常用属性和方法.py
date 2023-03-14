from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# kw = driver.find_element(By.ID, 'kw')
# # 获取id标识
# print(kw.id)
# # 获取宽高
# print(kw.size)
# # 获取宽高和坐标
# print(kw.rect)
# # 获取标签名
# print(kw.tag_name)
# news = driver.find_element(By.LINK_TEXT,'新闻')
# # 获取文本内容
# print(news.text)
# driver.quit()
#

# kw.send_keys("python自动化")
# time.sleep(3)
# # 清除
# kw.clear()
# kw.send_keys("python")
# sb = driver.find_element(By.ID,'su')
# sb.click()
#
# print(sb.get_attribute("outerHTML"))
# print(sb.get_attribute("name"))

# 判断元素是否可用，返回类型布尔类型
driver.get("https://sahitest.com/demo/clicks.htm")
qw = driver.find_element(By.XPATH,'//input[@value="disable1"]')
print(qw.is_displayed())
# driver.quit()
print(qw.is_enabled())
driver.quit()