
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def build_browser():
    with allure.step("build web driver"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
    with allure.step("cleanup web driver"):
        driver.close()

@allure.feature("baidu feature")
@allure.link("https://www.baidu.com", name="Baidu1")
@pytest.mark.parametrize('search_string',['selenium','deepseek','滕王阁序'])
def test_open_browser(build_browser, search_string):
    driver = build_browser
    with allure.step("Opening browser"):
        driver.get("https://www.baidu.com")
        time.sleep(1)
    with allure.step("Check if browser is opened"):
        assert "百度一下，你就知道" in driver.title
    with allure.step("go to search box"):
        web_element = driver.find_element(By.ID, "kw")
    with allure.step("type in search box"):
        web_element.send_keys(search_string)
        time.sleep(1)
    with allure.step("click search button"):
        driver.find_element(By.ID, "su").click()
        time.sleep(3)
    with allure.step("take a screenshot"):
        driver.get_screenshot_as_file("screenshot.png")
        time.sleep(1)
    with allure.step("attach the screenshot"):
        allure.attach.file("screenshot.png", name="baidu", attachment_type=allure.attachment_type.PNG)

