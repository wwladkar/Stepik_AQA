import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

time.sleep(1)

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла