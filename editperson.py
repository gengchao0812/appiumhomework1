from basepage import BasePage
from  appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
import random
from selenium.webdriver.support.ui import WebDriverWait
from personalinformation import PersonalInformation
"""
搜索结果页点击人员条目后的跳转页 个人信息页
"""

class EditPerson(BasePage):
    more_element = (MobileBy.ID,'com.tencent.wework:id/h9p')
    def click_more(self):
        self.find_and_click(self.more_element)
        return PersonalInformation(self.driver)