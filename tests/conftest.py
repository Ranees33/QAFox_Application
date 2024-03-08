import pytest
from selenium import webdriver
from configProperties.configinfo import Testdata


@pytest.fixture()
def setup_and_teardown(request):
    # global driver
    driver = webdriver.Chrome()
    browser = Testdata.Browser
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid Browser name")
    driver.maximize_window()
    driver.get(Testdata.App_Url)
    request.cls.driver = driver
    yield
    driver.quit()
