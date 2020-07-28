# from contactaddpage import ContactAddPage
"""
添加成员页
"""
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage

class AddMemberPage(BasePage):

    add_manual_element = (MobileBy.XPATH,"//android.widget.TextView[@text='手动输入添加']")
    success_toast_element = (MobileBy.XPATH,"//*[@class='android.widget.Toast']")
    def add_menual(self):
        """
        手动添加成员
        :return:
        """
        from contactaddpage import ContactAddPage
        # self.driver.find_element_by_id('com.tencent.wework:id/hgx').click()
        self.find_and_click(self.add_manual_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        element = self.webdriver_wait(self.success_toast_element)
        result = element.text
        return  result