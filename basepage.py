import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
"""
存放基本方法，比如初始化driver 或者find
"""
class BasePage:
    def __init__(self,driver:webdriver = None):
        self.driver = driver

    def find(self,locator):
        #locator 解元组
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click

    def find_and_sendkeys(self,locator,text):
        self.find(locator).send_keys(text)

    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().test("{text}").instance(0));')

    def webdriver_wait(self, locator,timeout=10):
        element = WebDriverWait(self.driver,timeout).untile(
            lambda x: x.find_element(*locator)
        )
        return element