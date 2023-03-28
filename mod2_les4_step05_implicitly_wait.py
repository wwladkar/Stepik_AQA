import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

time.sleep(1)


link = "http://suninjuly.github.io/wait1.html"

try:
    # открыть страницу
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)  # искать каждый элемент в течение 5 секунд
    browser.get(link)

    # нажать на кнопку
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # время для визуальной оценки результата
    time.sleep(5)

    # закрыть браузер после всех манипуляций
    browser.quit()
