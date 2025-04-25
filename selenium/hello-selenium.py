from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get('http://www.baidu.com')
driver.maximize_window()
# sleep(1)
# driver.find_element(By.ID, "kw").send_keys("selenium")
# driver.find_element(By.ID, 'su').click()
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "kw"))).send_keys('deepseek')
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "su"))).click()
sleep(5)
print(driver.window_handles)

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "DeepSeek | 深度求索"))).click()
print(driver.window_handles)
print(driver.current_window_handle)
sleep(5)
count=len(driver.window_handles)
new_window = driver.window_handles[count-1]
driver.switch_to.window(new_window)
print(driver.window_handles)
print(driver.current_window_handle)
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cursor-pointer > .text-xl"))).click()
driver.save_screenshot('test.png')
print(driver.window_handles)
print(driver.current_window_handle)
sleep(5)
driver.close()
