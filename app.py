from mainpage import MainPage
import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from basepage import BasePage

"""
存放 app应用常用的一些方法：
"""

class App(BasePage):

    def start(self):
        """
        启动APP
        :return:
        """
        if self.driver ==  None :
            #基类定义第一次调用时候driver是null
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['noReset'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['settings[waitForIdleTimeout]'] = 0
            print("初始化完毕")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
            print("开始等待")
            self.driver.implicitly_wait(5)
        #否则直接启动 launch不需要传入任何参数，会直接启动desired_caps定义的active
        #star_activity（packagename,activityname）可以启动其他的
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        """
        重启APP
        :return:
        """
        self.driver.close()
        self.driver.launch_app()
        pass

    def stop(self):
        """
        停止APP
        :return:
        """
        self.driver.quit()
        pass

    def goto_main(self):
        """
        进入首页
        :return:
        """
        return MainPage(self.driver)
