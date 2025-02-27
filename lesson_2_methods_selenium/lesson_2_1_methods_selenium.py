from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

### Задача 2.1.5
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "https://suninjuly.github.io/math.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# value = int(browser.find_element(By.ID, "input_value").text)
# answer = calc(value)
# browser.find_element(By.ID,'answer').send_keys(answer)
# browser.find_element(By.ID, "robotCheckbox").click()
# browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()
# browser.find_element(By.XPATH,"//button").click()
# print(browser.switch_to.alert.text)


### Задача 2.1.7
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

value = int(browser.find_element(By.ID, "treasure").get_attribute("valuex"))
answer = calc(value)
browser.find_element(By.ID,'answer').send_keys(answer)
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.XPATH,"//button").click()
print(browser.switch_to.alert.text)