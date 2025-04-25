import time
"""

"""
from selenium import webdriver
import pytest
url= "https://www.baidu.com"

@pytest.fixture(scope="class")
def open_url():
    # 前置
    print("----- open_url----")
    driver = webdriver.Chrome()
    driver.get(url) #url为链接地址
    yield driver    #yield之前代码是前置，之后的代码就是后置。
    # 后置
    print("----- quit_url----")
    driver.quit()

@pytest.fixture(scope="function")
def refresh_url(open_url):
    print("----- start refresh_url----")
    yield
    print("----- end refresh_url----")
    open_url.refresh()

@pytest.mark.usefixtures("open_url")
class TestLogin:

    def test_login(self):

        print("login done")

    # def test_logout(self,open_url):
    #     print("logout done")

    def test_refresh(self, refresh_url):
        print("refresh done")


