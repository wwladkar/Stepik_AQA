import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    time.sleep(1)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    summ = x + y
    print(summ)
    value = str(summ)

    # выбрать элемент из выпадающего списка со значением value
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(value)

    # нажать кнопку
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрыть браузер после всех манипуляций
    browser.quit()
