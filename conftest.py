import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")  # декоратор фикстуры с областью видимости "function"
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")  # декоратор фикстуры с областью видимости "function"
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit driver..")
    driver.quit()



