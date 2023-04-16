import pyperclip
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_class_name(browser, class_name):
    try:
        browser.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        return False
    return True


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

text_answer = ""


@pytest.mark.parametrize("link", links)
def test_stepik_auth(browser, link):
    browser.implicitly_wait(5)
    link = "{}".format(link)
    browser.get(link)
    button_enter = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    button_enter.click()
    email_send = browser.find_element(By.ID, "id_login_email")
    email_send.send_keys("your_login_email_for_Stepik")
    password_send = browser.find_element(By.ID, "id_login_password")
    password_send.send_keys("your_login_password_for_Stepik")
    button_inlet = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button_inlet.click()
    WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "div.light-tabs")))
    answer = math.log(int(time.time()))

    if check_exists_by_class_name(browser, "again-btn"):
        button_again = browser.find_element(By.CLASS_NAME, "again-btn")
        button_again.click()
        if check_exists_by_class_name(browser, "modal-popup__container"):
            button_popup = browser.find_element(By.CSS_SELECTOR, ".ember-view.modal-popup__footer > "
                                                                 "button:nth-of-type(1)")
            button_popup.click()

    text_area = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")
    text_area.clear()
    text_area.send_keys(answer)
    button_submit = browser.find_element(By.CLASS_NAME, "submit-submission")
    button_submit.click()
    feedback = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    text_feedback = feedback.text
    print('text_feedback: "' + text_feedback + '".')
    global text_answer  # задание глобальной переменной
    if text_feedback != "Correct!":
        text_answer = text_answer + text_feedback
    print('text_answer: "' + text_answer + '".')
    pyperclip.copy(text_answer)  # поместить текст ответа в буфер обмена
    assert text_feedback == "Correct!", 'text feedback is not "Correct!"'
