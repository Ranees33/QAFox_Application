import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.addtocartPage import AddToCartPage
from pageObjects.basePage import BasePage
from utilities.logger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
# @pytest.mark.skip(reason="Need to run the register test case separately")
# @pytest.mark.run(order=2)
class TestProductScreeshot:
    logger = LogGen.log_gen()

    def test_addtocart_product_screenshot(self):
        logging.info("Program execution started")

        # Below is the method has been implemented before create the page Object:
        # self.driver.find_element(By.LINK_TEXT, "Tablets").click()
        # self.driver.find_element(By.XPATH, "//div[@class='button-group']//button[1]").click()
        # time.sleep(5)
        # self.driver.find_element(By.ID, "cart-total").click()
        # self.driver.find_element(By.XPATH, "//strong[text()='View Cart']").click()
        # time.sleep(5)
        # self.driver.save_screenshot("Tablet.png")
        # tabImage = Image.open("Tablet.png")
        # tabImage.show()

        # Below is the method has been implemented after the Page Objects:
        check_tablet_product_on_cart = AddToCartPage(self.driver)
        check_tablet_product_on_cart.do_click_tablet()
        check_tablet_product_on_cart.do_click_product_cart_btn()
        check_tablet_product_on_cart.do_click_top_totalcart_btn()
        check_tablet_product_on_cart.do_click_view_cart_btn()
        check_tablet_product_on_cart.takes_screenshot()
        logging.info("Program execution ended")

