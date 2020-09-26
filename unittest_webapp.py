#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 12:24\
#@Author : YJY
#@File : unittest_webapp.py
#@Software : PyCharm


from appium import webdriver
from time import sleep
import pandas
import unittest

driver = None

class WebAPP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设备信息
        device={}
        device['deviceName'] = '192.168.197.101:5555'
        device['platformName'] = 'Android'
        device['platformVersion'] = '9'
        device['appPackage'] = 'com.android.quicksearchbox'
        device['appActivity'] = 'com.android.quicksearchbox.SearchActivity'
        device['noReset'] = True
        device['unicodeKeyboard'] = True
        device['resetKeyboard'] = True

        #打开app
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub",device)

    def testBaidu(self):
        global driver
        #操作元素
        driver.find_element_by_id("com.android.quicksearchbox:id/search_src_text").send_keys("www.baidu.com")
        driver.press_keycode(66)
        sleep(3)
        driver.find_element_by_id("org.chromium.webview_shell:id/url_field").clear()
        driver.find_element_by_id("org.chromium.webview_shell:id/url_field").send_keys("www.baidu.com")
        sleep(3)
        driver.find_element_by_accessibility_id("Load URL").click()
        sleep(3)


        #driver.find_element_by_id("index-kw").click()
        #driver.find_element_by_id("index-kw").send_keys("python编程")
        #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText').click()
        #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText').send_keys("python编程")
        #driver.press_keycode(66)
        #sleep(3)
        content = driver.page_source
        sleep(5)
        assert "幽门螺杆菌" in content
        self.assertIn("幽门螺杆菌",content)
    @classmethod
    def tearDownClass(cls):
        global driver
        #关闭app
        driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)
