from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问
driver.get('https://www.so.com/?src=so.com')
# 输入
driver.find_element(By.ID, 'input').send_keys('python自动化测试')
# 点击
driver.find_element(By.ID, 'search-button').click()
sleep(5)
# 获取标题
print(driver.title)
if 'python' in driver.title:
    print('找到了')
else:
    print('没找到')
driver.quit()
