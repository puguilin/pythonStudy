import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class MouseOperation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.find_elements(by,loc)
        self.ac = ActionChains(self.driver)

    def quit(self, send=3):
        time.sleep(send)
        self.driver.quit()

    def click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        self.driver.find_element(By.XPATH, '//form/input[3]').click()
        time.sleep(3)
        # quit()
        # 方法二
        input1 = self.driver.find_element(By.XPATH, '//form/input[3]')
        self.ac.click(input1).perform()
        quit()

    def context_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        input2 = self.driver.find_element(By.XPATH, '//form/input[4]')
        self.ac.context_click(input2).perform()
        time.sleep(3)
        quit()

    def double_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        input3 = self.driver.find_element(By.XPATH, '//form/input[2]')
        self.ac.double_click(input3).perform()
        time.sleep(3)
        quit()

    def drag_and_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        source = self.driver.find_element(By.ID, 'dragger')
        target = self.driver.find_element(By.XPATH, '//div[4]')
        self.ac.drag_and_drop(source, target).perform()
        time.sleep(3)
        quit()

    def mouseover(self):
        self.driver.get('https://sahitest.com/demo/mouseover.htm')
        time.sleep(2)
        input1 = self.driver.find_element(By.XPATH, '//form/input[1]')
        self.ac.move_to_element(input1).perform()
        div1 = self.driver.find_element(By.XPATH, '//div/div')
        self.ac.move_to_element(div1).perform()
        quit()

    def click_to_hold(self, ):
        file = "file:///" + os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/html/mouse_hold.html"
        self.driver.get(file)
        bt1 = self.driver.find_element(By.ID, 'btn1')
        self.ac.click_and_hold(bt1).perform()
        time.sleep(12)
        quit()


if __name__ == '__main__':
    mo = MouseOperation()
    # mo.click()
    # mo.context_click()
    # mo.double_click()
    # mo.drag_and_drop()
    # mo.mouseover()
    mo.click_to_hold()
    # print(os.path.abspath(__file__))
    # print(../os.path.dirname(os.path.abspath(__file__)))
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))
