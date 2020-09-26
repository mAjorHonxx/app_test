#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 10:23\
#@Author : YJY
#@File : WebAPP_test.py
#@Software : PyCharm


from appium import webdriver
from time import sleep

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
driver = webdriver.Remote("http://localhost:4723/wd/hub",device)

driver.find_element_by_id("com.android.quicksearchbox:id/search_src_text").send_keys("www.baidu.com")
driver.press_keycode(66)
sleep(2)
driver.find_element_by_id("org.chromium.webview_shell:id/url_field").clear()
driver.find_element_by_id("org.chromium.webview_shell:id/url_field").send_keys("www.baidu.com")
sleep(2)
driver.find_element_by_accessibility_id("Load URL").click()
sleep(3)


#driver.find_element_by_id("index-kw").click()
#driver.find_element_by_id("index-kw").send_keys("python编程")
#driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText').click()
#driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText').send_keys("python编程")
#driver.press_keycode(66)
print(driver.page_source)
sleep(3)


driver.quit()
