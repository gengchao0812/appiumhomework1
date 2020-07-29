import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait
from basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class ContactAddPage(BasePage):

    name_element = (MobileBy.XPATH,"//*[contains(@text , '姓名')]/../*[@class='android.widget.EditText']")

    gender_element = (MobileBy.XPATH,"//*[contains(@text , '性别')]/..//*[@text ='男']")
    male_element=(MobileBy.XPATH,"//*[contains(@text , '男')]")
    female_element=(MobileBy.XPATH,"//*[contains(@text , '女')]")
    phonemenum = (MobileBy.XPATH,"//*[@text='手机号']")
    save = (MobileBy.ID,"com.tencent.wework:id/h9w")
    delete_element = (MobileBy.XPATH,"//*[contains(@text , '删除成员')]")
    enter_element = (MobileBy.XPATH,"//*[contains(@text , '确定')]")

    def set_name(self,name):
        # name = self.driver.find_element_by_xpath(
        #     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText').send_keys(
        #     name)
        self.find_and_sendkeys(self.name_element,name)
        return self

    def set_gender(self,gender):
        # gender = self.driver.find_element_by_xpath(
        #     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        self.find_and_click(self.gender_element)
        if gender == '男':
            self.find_and_click(self.male_element)
        #self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()

        else:
            self.find_and_click(self.female_element)
            # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()

        return self

    def set_phonnum(self,phonnum):
        self.find_and_sendkeys(self.phonemenum,phonnum)
        # mobile = self.driver.find_element_by_id('com.tencent.wework:id/f1e').send_keys(phonnum)

        return self

    def click_save(self):
        from addmemberpage import AddMemberPage
        # save = self.driver.find_element_by_id('com.tencent.wework:id/h9w').click()
        self.find_and_click(self.save)
        return AddMemberPage(self.driver)

    def click_delete(self):
        from addmemberpage import AddMemberPage
        self.find_and_click(self.delete_element)
        self.find_and_click(self.enter_element)
        return AddMemberPage(self.driver)



