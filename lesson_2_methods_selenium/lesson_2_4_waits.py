import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# link = "http://suninjuly.github.io/cats.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# browser.find_element(By.ID, "button")



# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

### Задача 2.4.8
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'), "$100"))
browser.find_element(By.ID, "book").click()
value = int(browser.find_element(By.ID, "input_value").text)
answer = calc(value)
browser.find_element(By.ID,'answer').send_keys(answer)
browser.find_element(By.ID,"solve").click()
print(browser.switch_to.alert.text)
