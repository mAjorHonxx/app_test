#-*- codeing = utf-8 -*-
#@Time : 2020/8/15 11:27\
#@Author : YJY
#@File : 测试代码.py
#@Software : PyCharm


import pandas
data = pandas.read_excel("E:/calc.xls",sheet_name=0,names=['s1','op','s2','s3'],dtype={'s1':str,'op':str,'s2':str,'s3':str},header=None)
data = data.values.tolist()
print(data)