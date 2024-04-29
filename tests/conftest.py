import pytest
from selenium import webdriver
from configProperties.configinfo import Testdata
from utilities.logger import logging, LogGen

logger = LogGen.log_gen()


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    logging.info("Setting up WebDriver...")
    # driver = webdriver.Firefox()
    browser = Testdata.Browser
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
        logging.info("Chrome Browser Launching...")
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
        print("Launching firefox browser...")
        logging.info("Firefox Browser Launching...")
    else:
        print("Provide a valid Browser name")
    driver.maximize_window()
    driver.get(Testdata.App_Url)
    request.cls.driver = driver
    yield
    logging.info("Quitting WebDriver...")
    driver.quit()
