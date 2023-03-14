from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class OutHtml:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def id(self):
        kw = self.driver.find_element(By.ID,'kw')
        print(kw.get_attribute('outerHTML'))
        # get.attribute获取元素
        print(kw.get_attribute('class'))

    def class_name(self):
        ipt = self.driver.find_element(By.CLASS_NAME,'s_ipt')
        print(ipt.get_attribute('outerHTML'))
        print(ipt.get_attribute('id'))

    # 通过链接文本定位
    def link(self):
        news = self.driver.find_element(By.LINK_TEXT,'新闻')
        print(news.get_attribute('outerHTML'))

    def pr_link(self):
        hao123 = self.driver.find_element(By.PARTIAL_LINK_TEXT,'23')
        print(hao123.get_attribute('outerHTML'))
        wangpan = self.driver.find_element(By.PARTIAL_LINK_TEXT,'网')
        print(wangpan.get_attribute('outerHTML'))

    def tag_name(self):
        input = self.driver.find_element(By.TAG_NAME,'input')
        print(input.get_attribute('outerHTML'))
        inputs = self.driver.find_elements(By.TAG_NAME,'input')
        for i in inputs:
            print(i.get_attribute('outerHTML'))

    def name_id(self):
        name_id = self.driver.find_element(By.NAME,'rqlang')
        print(name_id.get_attribute('outerHTML'))


    def quit(self, sencod=3):
        sleep(sencod)
        self.driver.quit()

    def partial_link_text(self):
        news = self.driver.find_element(By.PARTIAL_LINK_TEXT,'新')
        print(news.get_attribute('outerHTML'))

if __name__ == '__main__':
    test = OutHtml()
    # test.id()
    # test.class_name()
    # test.link()
    # test.pr_link()
    # test.tag_name()
    # test.name_id()
    test.partial_link_text()
    test.quit()
