import pytest
from selenium import webdriver
from configProperties.configinfo import Testdata
from utilities.logger import logging, LogGen

logger = LogGen.log_gen()


@pytest.fixture()
def setup_and_teardown(request):
    logging.info("Setting up WebDriver...")
    # global driver
    driver = webdriver.Chrome()
    browser = Testdata.Browser
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
        print("Launching firefox browser...")
    else:
        print("Provide a valid Browser name")
    driver.maximize_window()
    driver.get(Testdata.App_Url)
    request.cls.driver = driver
    yield
    logging.info("Quitting WebDriver...")
    driver.quit()
