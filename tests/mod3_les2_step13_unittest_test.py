import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestReg(unittest.TestCase):

    def test_registration1(self):

        try:
            options = Options()
            options.add_argument("start-maximized")
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Ivanov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("ivan@gmail.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg=None)

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration2(self):

        try:
            options = Options()
            options.add_argument("start-maximized")
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Ivanov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("ivan@gmail.com")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg=None)

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
