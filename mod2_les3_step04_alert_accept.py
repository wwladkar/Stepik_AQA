import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

time.sleep(1)


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:

    # выводим в консоль ответ
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[-1])

    # закрываем браузер после всех манипуляций
    browser.quit()
