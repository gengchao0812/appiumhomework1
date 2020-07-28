import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait
from contactlistpage import ContactListPage
from appium.webdriver.common.mobileby import MobileBy
"""
主界面
"""
from basepage import BasePage
from addmemberpage import AddMemberPage
class MainPage(BasePage):
    #不要暴露内部界面元素给外部
    #定义位置和调用要分开
    contactlist = (MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")

    def goto_contactlist(self):

        """
        进入到通讯录
        :return:
        """
        # time.sleep(1)
        # mail_list = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView').click()
        self.find_and_click(self.contactlist)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass