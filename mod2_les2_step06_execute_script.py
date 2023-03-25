import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
