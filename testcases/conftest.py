import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        print("launching chrome")
        driver = webdriver.Chrome()
    elif browser =="firefox":
        print("launching firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge")
        driver = webdriver.Edge()
    else:
        print("opening headless")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)

    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    return driver



