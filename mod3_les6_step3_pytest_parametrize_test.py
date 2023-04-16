import pytest
from selenium.webdriver.common.by import By

languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский",  marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]


@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(browser, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

