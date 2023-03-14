from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
id = driver.find_element(By.CSS_SELECTOR, '#wrapper_wrapper')
print(id.get_attribute("outerHTML"))
# driver.quit()
# search_class = driver.find_element(By.CSS_SELECTOR, '.s_pit')
search_box_name = driver.find_element(By.CSS_SELECTOR,'input[name="wd]')
print(search_box_name.get_attribute('outerHTML'))
# 2.层级
input1 = driver.find_element(By.CSS_SELECTOR,'form[id="form"]input')
for i in input1:
    print(i.get_attribute('outerHTML'))
input2 = driver.find_element(By.CSS_SELECTOR,'form[id="form"]>input')
for i in input2:
    print(i.get_attribute('outerHTML'))


span = driver.find_element(By.CSS_SELECTOR,'form[id="form]:nth-child(8)')
print(span.get_attribute('outerHTML'))
input_element = driver.find_element(By.CSS_SELECTOR,'form[id="form"] input:nth-of-type(8)')
print(input_element.get_attribute('outerHTML'))
elemet1 = driver.find_element(By.CSS_SELECTOR,'input[name*="_idx"]')
print(elemet1.get_attribute('outerHTML'))
elemet2 = driver.find_element(By.CSS_SELECTOR,'input[name="wd"][autocomplete="off"]')
print(elemet2.get_attribute('outerHTML'))
driver.quit()