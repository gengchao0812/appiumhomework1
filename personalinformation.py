from basepage import BasePage
from  appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
import random
from selenium.webdriver.support.ui import WebDriverWait
from contactaddpage import ContactAddPage
"""
点击个人信息页右上角三个点后的跳转界面
"""

class PersonalInformation(BasePage):
    edit_information = (MobileBy.XPATH,"//*[contains(@text,'编辑成员')]")
    def click_edit(self):
        self.find_and_click(self.edit_information)
        return ContactAddPage(self.driver)