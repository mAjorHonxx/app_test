#-*- codeing = utf-8 -*-
#@Time : 2020/9/21 21:46\
#@Author : YJY
#@File : test_fixture.py
#@Software : PyCharm


import pytest

@pytest.fixture()
def login():
    print("这是个登录方法")

def test_case1(login):
    print("test_case1，需要登录")
    pass

def test_case2():
    print("test_case2，不需要登录")
    pass

def test_case3(login):
    print("test_case3，需要登录")
    pass

if __name__ == '__main__':
    pytest.main()