from selenium.webdriver.support.wait import WebDriverWait
import allure
class Base:
    # 初始化driver
    def __init__(self,driver):
        self.driver = driver
    # 定位单个元素
    def find_element(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    # 定位一组元素
    def  find_elements(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    # 点击元素
    def click_element(self,loc):
        self.find_element(loc).click()
    # 清空输入框且输入内容
    def send_keys_text(self,loc,text):
        input_box = self.find_element(loc)
        input_box.clear()
        input_box.send_keys(text)
    # 获取单个text值
    def gain_single_text(self,loc):
        single_text = self.find_element(loc)
        return single_text.text
    # 获取一组text值
    def gain_a_group_text(self,loc):
        a_group_text = self.find_elements(loc)
        for i in a_group_text:
            return i.text

