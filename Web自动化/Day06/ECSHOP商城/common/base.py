import time
from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException, InvalidArgumentException
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化浏览器
    def __init__(self, browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Edge':
            self.driver = webdriver.Edge()
        else:
            print("不支持当前浏览器")
            self.driver = None
        self.driver.maximize_window()


    # 请求网页
    def base_get(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e)
            print("输入的网址存在问题")

    # 自定义元素定位方法
    def base_find(self, locator):
        try:
            # ele = self.driver.find_element(*locator)
            # ele = WebDriverWait(self.driver,10,1).until(lambda x:x.find_element(*locator))
            ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return ele
        except NoSuchElementException:
            print("没有找到当前元素")

    # 自定义元素输入方法
    def base_send(self, locator, value):
        ele = self.base_find(locator)
        if ele is not None:
            ele.send_keys(value)
        else:
            print("没有找到当前元素")

    #  自定义元素点击方法
    def base_click(self, locator):
        ele = self.base_find(locator)
        if ele is not None:
            ele.click()
        else:
            print("没有找到当前元素")

    # 关闭所有浏览器
    def base_quit(self, secods=3):
        time.sleep(secods)
        self.driver.quit()

    # 前进
    def forward(self):
        self.driver.forward()

    # 后退
    def back(self):
        self.driver.back()

    # 刷新
    def refresh(self):
        self.driver.refresh()

    # 元素属性方法
    def get_attribute(self, locator):
        ele = self.base_find(locator)
        if ele is not None:
            return ele.get_attribute("outerHTML")
        else:
            print("没有找到当前元素")

    # 获取属性方法
    def get_text(self, locator):
        ele = self.base_find(locator)
        if ele is not None:
            text = ele.text()
            if text is not None:
                return text
            else:
                print("当前元素没有文本内容")
        else:
            print("没有找到当前元素")


if __name__ == '__main__':
    base = Base("Chrome")
    # base_基本语法_grammar01.base_get("http://www.baidu.com")
    # base_基本语法_grammar01.base_get("http://www.taobao.com")
    # base_基本语法_grammar01.back()
    # time.sleep(2)
    # base_基本语法_grammar01.forward()
    # time.sleep(2)
    base.base_send((By.ID, 'kw'), 'python')
    # base_基本语法_grammar01.driver.find
    # base_基本语法_grammar01.base_quit()
    pass
