import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_basket_enable(browser):
    browser.get(link)
    time.sleep(30)
    BASKET_ENABLE = browser.find_element(By.XPATH, "//button[contains(@class, 'add-to-basket')]")
    assert BASKET_ENABLE,"Кнопка 'Добавить в корзину' отсутствует на сайте"