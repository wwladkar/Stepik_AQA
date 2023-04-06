import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")  # декоратор фикстуры с областью видимости "function"
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
