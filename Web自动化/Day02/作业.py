"""
1. 首页搜索操作
1. 注册操作
1. 登录操作
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random


class Element:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def input(self, by, loc, value):
        e1 = self.driver.find_element(by, loc)
        e1.send_keys(value)

    def geturl(self, url):
        self.driver.get(url=url)

    def click(self, by, loc):
        self.driver.find_element(by, loc).click()

    def set_windows(self):
        self.driver.maximize_window()

    def quit(self):
        sleep(2.5)
        self.driver.quit()


class Ecshop(Element):
    def serach(self):
        self.geturl('https://ecshop.test2.shopex123.com/index.php')
        self.set_windows()
        self.input(By.ID, 'keyword', '欧莱雅')
        self.click(By.NAME, 'imageField')

    def sign_in(self):
        sleep(5)
        self.geturl('https://ecshop.test2.shopex123.com/user.php?act=register')
        self.set_windows()
        self.input(By.ID, 'username', 'sun335')
        self.input(By.ID, 'email', 'self2533@qq.com')
        self.input(By.ID, 'password1', '12345678')
        self.input(By.ID, 'confirm_password', '12345678')
        sleep(3.5)
        self.click(By.NAME, 'Submit')
        self.click(By.LINK_TEXT, '退出')

    def login_in(self):
        sleep(5)
        self.geturl('https://ecshop.test2.shopex123.com/user.php')
        self.set_windows()
        self.input(By.NAME, 'username', 'sun335')
        self.input(By.NAME, 'password', '12345678')
        sleep(3.5)
        self.click(By.ID, 'remember')
        self.click(By.NAME, 'submit')


if __name__ == '__main__':
    es = Ecshop()
    es.serach()
    es.sign_in()
    es.login_in()
    es.quit()
