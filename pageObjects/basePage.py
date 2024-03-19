# from tkinter import Image
# from PIL import Image

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This is the parent class of all Pages """
""" It contains all the generic methods and utilities for all the Pages """


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_displayed(self, by_locators):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locators))
        return bool(element)

    def get_page_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def get_current_url(self, current_url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(current_url))
        return self.driver.current_url

    def select_dropdown(self, by_locator, value):
        element = Select(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)))
        return element.select_by_value(value)

    def move_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(source_locator))
        target_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(target_locator))
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        # webpage_Image = Image.open(filename)
        # webpage_Image.show()

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)




