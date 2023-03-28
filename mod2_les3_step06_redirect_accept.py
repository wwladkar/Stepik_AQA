import time
import math
import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

time.sleep(1)


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    #  открыть страницу
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    time.sleep(1)

    #  нажать на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(1)

    #  переключиться на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #  пройти капчу для робота и получить число-ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

    #  вывод в консоль кода ответа
    alert = browser.switch_to.alert
    alert_text = alert.text
    text_answer = alert_text.split(': ')[-1]
    print(text_answer)

    #  копировать код ответа в буфер обмена и принять alert
    pyperclip.copy(text_answer)
    alert.accept()

finally:
    #  время для визуальной оценки результата
    time.sleep(5)

    #  закрыть браузер после всех манипуляций
    browser.quit()
