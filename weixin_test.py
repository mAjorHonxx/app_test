#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 18:07\
#@Author : YJY
#@File : weixin_test.py
#@Software : PyCharm


from appium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = None

class WeixinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设备信息
        device={}
        device['deviceName'] = '192.168.197.101:5555'
        device['platformName'] = 'Android'
        device['platformVersion'] = '9'
        device['appPackage'] = 'com.tencent.mm'
        device['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        device['noReset'] = True
        device['unicodeKeyboard'] = True
        device['resetKeyboard'] = True
        #关闭app自动启动
        device['autoLaunch'] = False

        #打开app
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub",device)

    def testWeixin(self):
        global driver
        print(driver.context)
        sleep(3)
        # #重置app并启动
        # #driver.reset()
        # #手动启动app
        # driver.launch_app()
        # sleep(5)
        # #手动关闭app
        # driver.close_app()

        #手动启动一个app窗口
        driver.start_activity("com.tencent.mm","com.tencent.mm.ui.LauncherUI")

        '''
        #print(driver.current_activity)
        # 1.if driver.current_activity == '.permission.ui.GrantPermissionsActivity':
            #弹窗
        win = driver.wait_activity(".permission.ui.GrantPermissionsActivity",5)
        # 2.
        if win:
            toast = ('xpath','//*[contains(@text,"ALLOW")]')
            t = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located(toast))
            t.click()
            driver.wait_activity("com.android.packageinstaller.permission.ui.GrantPermissionsActivity",5)
            toast = ('xpath','//*[contains(@text,"ALLOW")]')
            t = WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located(toast))
            t.click()
        #登录界面
        driver.wait_activity("/com.tencent.mm.ui.LauncherUI",5)
        #点击login
        driver.find_element_by_id("com.tencent.mm:id/drp").click()
        sleep(3)

        #点击地区选择
        #driver.find_element_by_id("com.tencent.mm:id/a0u").click()
        driver.find_element_by_xpath('//*[contains(@text,"United States（+1）")]').click()
        sleep(3)
        #滑屏
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        for i in range(1,6):
            driver.swipe(width/2, height*3/4, width/2, height/4, 1000) #1000ms
        #找到China选项
        driver.wait_activity("com.tencent.mm.ui.tools.CountryCodeUI",5)
        driver.find_element_by_xpath('//*[contains(@text,"China")]').click()
        sleep(3)
        #填写手机号
        driver.find_element_by_id("com.tencent.mm:id/ji").send_keys("13012345678")
        #点击Next
        driver.find_element_by_xpath('//*[contains(@text,"Next")]').click()
        sleep(10)
        '''


    # @classmethod
    # def tearDownClass(cls):
    #     global driver
    #     #关闭app
    #     driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)
