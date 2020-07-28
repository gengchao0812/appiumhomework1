import  pytest
from appium import  webdriver
import time
import sys
from  appium.webdriver.common.touch_action import TouchAction
import random
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append("..")

class TestDw():
    def setup_class(self):
        print("调起setup")
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

    def teardown_class(self):
        self.driver.quit()

    def get_mobile(self):
        """
        随机生成一个手机号，格式为186xxxxxxxx
        """
        mobile = '158'
        i = 0
        while (i < 8):
            num = random.choice('0123456789')
            mobile += num
            i += 1
        # print(mobile)
        return mobile


    def getname(self):
        """
        实现姓名为霍格沃兹-0 霍格沃兹-1
        :return:
        """
        i = [0]

        def counter():
            i[0] += 1
            return i[0]
        return('霍格沃兹' + '-' + str(i[0]))
    
#这里参数化pytest
    @pytest.mark.run(order=1)
    def test_add(self):
        """
        增加员工操作
        姓名和手机号精确赋值待实现
        考虑用number_before字段中 共X人，做删除成功断言，待实现
        :return:
        """
        # xpath定位通讯录并点击
        self.getname()
        time.sleep(1)
        mail_list = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView').click()

        #点击手动添加需要 滚动查找
        print("点击手动添加")
        self.driver.implicitly_wait(1)
        add_manually = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[last()]/android.widget.RelativeLayout/android.widget.ImageView').click()
        print("添加成员界面的手动输入添加")
        self.driver.implicitly_wait(1)
        add_manually1 = self.driver.find_element_by_id('com.tencent.wework:id/hgx').click()
        self.driver.implicitly_wait(1)
        #给姓名赋值 待扩充，累加 如：霍格沃兹_01
        name = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText').send_keys(self.getname())
        #给性别赋值
        self.driver.implicitly_wait(1)
        gender = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        self.driver.implicitly_wait(1)
        man = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        # woman = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        #给手机号赋值
        self.driver.implicitly_wait(1)
        #手机号输入待扩充，累加还是随机数
        mobile = self.driver.find_element_by_id('com.tencent.wework:id/f1e').send_keys(self.get_mobile())
        #取消发送通知勾选框
        self.driver.implicitly_wait(1)
        send_message = self.driver.find_element_by_id('com.tencent.wework:id/ern').click()
        #保存
        save = self.driver.find_element_by_id('com.tencent.wework:id/h9w').click()
        print("保存成功")
        #断言 toast 保存成功 采用显示等待
        WebDriverWait(self.driver,10).untile(lambda x:x.find_element)
        self.driver.implicitly_wait(1)

    @pytest.mark.run(order=2)
    def test_delete(self):
        """
        删除用户操作

        考虑用number_before字段中 共X人，做删除成功断言，待实现
        :return:
        """
        #添加成员的界面左上角返回按钮
        time.sleep(2)
        print("点击返回")
        return_button = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').click()
        self.driver.implicitly_wait(1)
        #点击更多
        #number_before = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView').text
        more = self.driver.find_element_by_id('com.tencent.wework:id/h9u').click()
        #选取界面排序最后的一个人点击编辑
        edit_members = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[last()]/android.widget.RelativeLayout').click()
        #删除成员
        delete_members = self.driver.find_element_by_id('com.tencent.wework:id/e3f').click()
        #确认删除
        confirm_delete = self.driver.find_element_by_id('com.tencent.wework:id/bci').click()




