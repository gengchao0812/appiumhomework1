import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
import random
from selenium.webdriver.support.ui import WebDriverWait
from basepage import BasePage

from addmemberpage import AddMemberPage
"""
通讯录列表页
"""
class ContactListPage(BasePage):
    add_contact_element = "添加成员"
    def add_contact(self):
        """
        添加联系人界面
        :return:
        """
        #滚动查找
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UIScrollable(new UISelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UISelector()'
        #                          '.test("添加成员").instance(0));').click()
        self.find_by_scroll(self.add_contact_element).click()
        return AddMemberPage(self.driver)

    def search_contact(self):
        pass