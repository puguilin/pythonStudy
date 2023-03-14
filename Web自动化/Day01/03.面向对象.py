from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Test:
    def __init__(self):
        # mobileEulation = {"deviceName":"iPhone SE"}
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("mobileEulation",mobileEulation)
        self.driver = webdriver.Chrome()

    def geturl(self):
        self.driver.get('https://www.so.com/?src=so.com')
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'input').send_keys('python')
        self.driver.find_element(By.ID, 'search-button').click()
        sleep(5)
        print(self.driver.title)
        # self.driver.quit()

    def quit(self, seconds=3):
        sleep(seconds)
        self.driver.quit()


if __name__ == '__main__':
    case = Test()
    case.geturl()
    case.quit()
