import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    time.sleep(1)

    # проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people checked: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots checked: ", robots_checked)
    assert robots_checked is None, "Robots radio is selected by default"

    # проверяем значение атрибута disabled у кнопки Submit
    button_submit = browser.find_element(By.CLASS_NAME, "btn")
    button_disabled = button_submit.get_attribute("disabled")
    print("value of button disable:", button_disabled)
    assert button_disabled is None

    # проверяем значения разных атрибутов у кнопки Submit
    button_class = button_submit.get_attribute("class")
    button_type = button_submit.get_attribute("type")
    button_style = button_submit.get_attribute("style")
    print("Value of button class:", button_class)
    print("Value of button type:", button_type)
    print("Value of button style:", button_style)

    # проверяем значение атрибута disabled у кнопки Submit после таймаута (10c)
    time.sleep(10)
    button_disabled = button_submit.get_attribute("disabled")
    print("value of button disable after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:

    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
