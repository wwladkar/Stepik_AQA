import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/wait2.html"

try:
    # открыть страницу
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    # проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    # нажать на кнопку
    button.click()

    # прочитать сообщение
    message = browser.find_element(By.ID, "verify_message")

    # текст сообщения содержит "successful"
    assert "successful" in message.text

finally:
    # время для визуальной оценки результата
    time.sleep(5)

    # закрыть браузер после всех манипуляций
    browser.quit()
