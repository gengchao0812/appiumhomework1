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
from editperson import EditPerson
"""
通讯录列表页
"""
class ContactListPage(BasePage):

    add_contact_element = "添加成员"
    edit_contact_element = (MobileBy.ID,'com.tencent.wework:id/h9z')
    select_contact_element = (MobileBy.XPATH,'//*[@class="android.widget.EditText"]')

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

    def search_contact(self,name):
        result_contact_element = (MobileBy.XPATH, f'//*[contains(@text,"{name}")]')
        # result_null_element = (MobileBy.XPATH, '//*[@text="无搜索结果"]')
        self.find_and_click(self.edit_contact_element)
        self.find_and_sendkeys(self.select_contact_element,name)
        time.sleep(1)
        result_more_element = (MobileBy.XPATH, f'//*[@class="android.widget.TextView" and @text="{name}"]')
        assert len(self.finds(result_more_element))!=0,"搜索结果为空，没有用户可以被删除"
        # if len(self.finds(self.result_null_element))>0:
        #     print('搜索无结果')
        #     return
        # else:
        self.find_and_click(result_more_element)
        return EditPerson(self.driver)

    def assert_contact(self,name):
        result_more_element = (MobileBy.XPATH, f'//*[@class="android.widget.TextView" and @text="{name}"]')
        assert len(self.finds(result_more_element))>0,"删除用户失败"