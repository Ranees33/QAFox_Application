from selenium.webdriver.common.by import By

from configProperties.configinfo import Testdata
from pageObjects.basePage import BasePage


class CheckoutPage(BasePage):
    ClickTabletsInMenu = (By.LINK_TEXT, "Tablets")
    ClickAddtocartBtnOnProduct = (By.XPATH, "//div[@class='button-group']//button[1]")
    ClickRightsideCartBtn = (By.ID, "cart-total")
    ClickCheckoutLink = (By.XPATH, "//strong[text()='Checkout']")
    ClickCartQntyBox = (By.XPATH, "//input[@class='form-control']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.App_Url)

    def do_click_tablet_menu(self):
        self.do_click(self.ClickTabletsInMenu)

    def do_click_product_addtocart_btn(self):
        self.do_click(self.ClickAddtocartBtnOnProduct)

    def do_click_rightside_itemcart_btn(self):
        self.do_click(self.ClickRightsideCartBtn)

    def do_click_checkout_link(self):
        self.do_click(self.ClickCheckoutLink)

    def do_click_cart_quantity_box(self):
        self.do_click(self.ClickCartQntyBox)

    def do_clear_textbox(self):
        self.clear_textbox(self.ClickCartQntyBox)

    def do_enter_quantity_value(self, EnterQtyValue):
        self.do_send_keys(self.ClickCartQntyBox, EnterQtyValue)

    def takes_screenshot(self):
        self.take_screenshot("Quantity_nos.png")



