from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait
from contactlistpage import ContactListPage
from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage

class SearchPage(BasePage):
    search_element = (MobileBy.XPATH,"//*[contains(@text , '搜索')]")
    def search(self,name):
        self.find_and_sendkeys(self.search_element,name)
