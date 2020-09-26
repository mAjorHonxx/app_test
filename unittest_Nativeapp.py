#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 12:37\
#@Author : YJY
#@File : unittest_Nativeapp.py
#@Software : PyCharm


from appium import webdriver
from time import sleep
import pandas
import unittest
import parameterized

driver = None
data = pandas.read_excel("E:/calc.xls", sheet_name=0, names=['s1', 'op', 's2', 's3'],
                         dtype={'s1': str, 'op': str, 's2': str, 's3': str}, header=None)
data = data.values.tolist()

class NativeApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        #指定设备信息
        device={}
        #设备端口号
        device['deviceName'] = '192.168.197.101:5555'
        #操作系统种类
        device['platformName'] = 'Android'
        #操作系统版本
        device['platformVersion'] = '9'
        #指定APP程序包
        device['appPackage'] = 'com.android.calculator2'
        #device['appPackage'] = 'com.android.quicksearchbox'
        #指定启动页的名字
        device['appActivity'] = 'com.android.calculator2.Calculator'
        #device['appActivity'] = 'com.android.quicksearchbox.SearchActivity'
        #指定每次测试前不重装app
        device['noReset'] = True

        #打开APP
        driver = webdriver.Remote("http://localhost:4723/wd/hub",device)


    @parameterized.parameterized.expand(data)
    def testCalcApp(self,a,op,b,yq):
        # data = [
        #     ['123','+','45','168'],
        #     ['23','-','6','17'],
        #     ['6','*','8','48'],
        #     ['49','/','7','7']
        #]

        #读txt文件
        # data = []
        # file = open("E:/calc.txt","r")
        # for i in file:
        #     data.append(i.split())
        # print(data)
        # file.close()
        global driver
        if op == '+':
            oper = 'add'
        elif op == '-':
            oper = 'sub'
        elif op == '*':
            oper = 'mul'
        else:
            oper = 'div'

        for i in a:
             driver.find_element_by_id("com.android.calculator2:id/digit_"+i).click()
        driver.find_element_by_id("com.android.calculator2:id/op_" + oper).click()
        for i in b:
            driver.find_element_by_id("com.android.calculator2:id/digit_" + i).click()

        #driver.press_keycode(66)
        driver.find_element_by_id("com.android.calculator2:id/eq").click()
        jg = driver.find_element_by_id("com.android.calculator2:id/result").text
        sleep(3)
        assert jg == yq
        self.assertEqual(jg,yq)

        # #操作元素
        # driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
        # driver.find_element_by_id("com.android.calculator2:id/digit_3").click()
        # driver.find_element_by_id("com.android.calculator2:id/op_add").click()
        # driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
        # driver.find_element_by_id("com.android.calculator2:id/digit_0").click()
        # #driver.find_element_by_id("com.android.calculator2:id/eq").click()
        # driver.press_keycode(66)
        # jg=driver.find_element_by_id("com.android.calculator2:id/result").text
        #
        # # driver.find_element_by_id("com.android.quicksearchbox:id/search_src_text").send_keys("手机测试")
        # # driver.press_keycode(66)
        #
        # sleep(3)
        # if jg == "103":
        #     print("测试通过")
        # else:
        #     print("测试失败")

    @classmethod
    def tearDownClass(cls):
        global driver
        #关闭APP
        driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)