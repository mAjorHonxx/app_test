#-*- codeing = utf-8 -*-
#@Time : 2020/8/13 22:09\
#@Author : YJY
#@File : test1.py
#@Software : PyCharm
#查看app报名  adb指令 adb shell dumpsys window w | findstr \/ | findstr name=

from appium import webdriver
from time import sleep
import pandas
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

#读excel文件
data = pandas.read_excel("E:/calc.xls",sheet_name=0,names=['s1','op','s2','s3'],
                         dtype={'s1':str,'op':str,'s2':str,'s3':str},header=None)
data = data.values.tolist()

for i in range(0,len(data)):
    if data[i][1] == '+':
        data[i][1] = 'add'
    elif data[i][1] == '-':
        data[i][1] = 'sub'
    elif data[i][1] == '*':
        data[i][1] = 'mul'
    else:
        data[i][1] = 'div'
for i in data:
    for j in range(0,len(i)-1):
        x = i[j]
        if j != 1:
            for a in x:
                driver.find_element_by_id("com.android.calculator2:id/digit_"+a).click()
        else:
            driver.find_element_by_id("com.android.calculator2:id/op_"+i[1]).click()

    #driver.press_keycode(66)
    driver.find_element_by_id("com.android.calculator2:id/eq").click()
    jg = driver.find_element_by_id("com.android.calculator2:id/result").text
    sleep(3)
    if jg == i[3]:
        print("测试通过")
    else:
        print("测试失败")

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
#关闭APP
driver.quit()

