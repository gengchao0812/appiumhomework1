import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
import logging
"""
存放基本方法，比如初始化driver 或者find
"""
class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:webdriver = None):
        self.driver = driver

    def find(self,locator):
        logging.info(f'find: {locator}')
        #locator 解元组
        return self.driver.find_element(*locator)

    def finds(self,locator):
        logging.info(f'find: {locator}')
        #locator 解元组
        return self.driver.find_elements(*locator)

    def find_and_click(self,locator):
        logging.info('click')
        self.find(locator).click()

    def find_and_sendkeys(self,locator,text):
        logging.info(f'sendkeys : {text}')
        self.find(locator).send_keys(text)


    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')



    def webdriver_wait(self, locator,timeout=10):
        element = WebDriverWait(self.driver,timeout).untile(
            lambda x: x.find_element(*locator)
        )
        return element


    def back(self, num):
        logging.info(f"back：{num}")
        for i in range(num):
            self.driver.back()