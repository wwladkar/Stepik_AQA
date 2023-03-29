import time
import math
import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # открыть страницу
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)  # искать каждый элемент в течение 5 секунд
    browser.get(link)

    # дождаться, когда цена дома уменьшится до $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    # нажать на кнопку
    button = browser.find_element(By.ID, "book")
    button.click()

    # пройти капчу для робота и получить число-ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

    # вывод в консоль кода ответа
    alert = browser.switch_to.alert
    alert_text = alert.text
    text_answer = alert_text.split(': ')[-1]
    print(text_answer)

    # копировать код ответа в буфер обмена и принять alert
    pyperclip.copy(text_answer)
    alert.accept()

finally:
    # время для визуальной оценки результата
    time.sleep(5)

    # закрыть браузер после всех манипуляций
    browser.quit()
