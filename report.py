#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 16:36\
#@Author : YJY
#@File : report.py
#@Software : PyCharm

import unittest
import time
import HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover("F:/软件测试/app_test",pattern="unit*.py")
suite.addTests(tests)

now = time.strftime("%Y%m%d %H%M%S",time.localtime())

reportFile = "./" + now + "_result.html"

fp = open(reportFile,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'App测试报告',description=u'Calc and Baidu')
runner.run(suite)
fp.close()
