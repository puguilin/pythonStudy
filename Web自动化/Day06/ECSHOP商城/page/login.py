import time
import unittest
from common.base import Base
from selenium.webdriver.common.by import By


class Login(Base):
    def input_uesrname(self, username):
        self.base_send((By.NAME, 'username'), username)

    def input_password(self, password):
        self.base_send((By.NAME, 'password'), password)

    def remeber(self):
        self.base_click((By.NAME, 'remember'))

    def submit(self):
        self.base_click((By.NAME, 'submit'))


if __name__ == '__main__':
    login = Login('Chrome')
    login.base_get('https://ecshop.test2.shopex123.com/user.php')
    login.input_uesrname('fine1')
    time.sleep(2)
    login.input_password('123456')
    time.sleep(2)
    # login.refresh()
    login.remeber()
    login.submit()
    login.base_quit()
