import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

### Задача 2.3.4
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/alert_accept.html"
# browser = webdriver.Chrome()
# browser.get(link)
# browser.find_element(By.TAG_NAME, "button").click()
# browser.switch_to.alert.accept()
# value = int(browser.find_element(By.ID, "input_value").text)
# answer = calc(value)
# browser.find_element(By.ID,'answer').send_keys(answer)
# browser.find_element(By.XPATH,"//button").click()
# print(browser.switch_to.alert.text)

### Задача 2.3.6
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.TAG_NAME, "button").click()
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)
value = int(browser.find_element(By.ID, "input_value").text)
answer = calc(value)
browser.find_element(By.ID,'answer').send_keys(answer)
browser.find_element(By.XPATH,"//button").click()
print(browser.switch_to.alert.text)