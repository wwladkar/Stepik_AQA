import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

time.sleep(1)

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # открываем страницу первого товара
    browser.get("https://www.wildberries.ru/catalog/47414704/detail.aspx?size=91870267")
    time.sleep(5)

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, "button.btn-main")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://www.wildberries.ru/catalog/37878051/detail.aspx?size=77815312")
    time.sleep(5)

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, "button.btn-main")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://www.wildberries.ru/lk/basket")
    time.sleep(5)

    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, ".list-item__good")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла