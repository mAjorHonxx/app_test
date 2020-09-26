#-*- codeing = utf-8 -*-
#@Time : 2020/9/21 21:57\
#@Author : YJY
#@File : test_fixture_yield.py
#@Software : PyCharm


import pytest

# 作用域：module是在模块之前执行，  模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield    # yield  相当于加入了 teardown操作

    print("执行teardown")
    print("最后关闭浏览器")

def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__ == '__main__':
    pytest.main()