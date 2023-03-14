from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class BrowesOpen:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def window_size(self):
        for i in range(3):
            sleep(1.25)
            self.driver.maximize_window()
            sleep(1.5)
            self.driver.set_window_size(1260,960)
            sleep(2)
            self.driver.minimize_window()

    def refresh(self):
        # 刷新当前页面
        self.driver.refresh()

    def forward_back(self):
        self.driver.get("https://www.taobao.com")
        for i in range(3):
            sleep(2)
            self.driver.back()
            sleep(1.5)
            self.driver.forward()

    # 关闭浏览器
    def quit(self):
        sleep(2)
        self.driver.quit()

    def close(self):

        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        sleep(2)
        # 只关闭打开的页面，后面点击的不承认
        self.driver.close()

if __name__ == '__main__':
    browes = BrowesOpen()
    # browes.window_size()
    # browes.forward_back()
    # browes.refresh()
    browes.close()
    browes.quit()