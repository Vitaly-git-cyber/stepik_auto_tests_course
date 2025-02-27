import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


### Задача 2.2.3
# link = "https://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# value_1 = int(browser.find_element(By.ID, "num1").text)
# value_2 = int(browser.find_element(By.ID, "num2").text)
# sum_value = value_1 + value_2
# select = Select(browser.find_element(By.ID, "dropdown"))
# [sel for sel in select.options if sel.text ==  str(sum_value)][0].click()
# browser.find_element(By.TAG_NAME, "button").click()
# time.sleep(3)
# print(browser.switch_to.alert.text)


### Задача 2.2.6
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)
# value = int(browser.find_element(By.ID, "input_value").text)
# answer = calc(value)
# browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID,'answer'))
# browser.find_element(By.ID,'answer').send_keys(answer)
# browser.find_element(By.ID, "robotCheckbox").click()
# browser.find_element(By.ID, "robotsRule").click()
# browser.find_element(By.XPATH,"//button").click()
# print(browser.switch_to.alert.text)

### Задача 2.2.8
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
for i in browser.find_elements(By.XPATH, "//div/input"):
    i.send_keys("Привет!")
browser.find_element(By.ID,"file").send_keys(file_path)
browser.find_element(By.TAG_NAME,'button').click()
time.sleep(3)
print(browser.switch_to.alert.text)