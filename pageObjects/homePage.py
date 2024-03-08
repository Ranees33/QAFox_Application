from selenium.webdriver.common.by import By
from configProperties.configinfo import Testdata
from pageObjects.basePage import BasePage


class HomePage(BasePage):
    ClickTabletsInMenu = (By.LINK_TEXT, "Tablets")
    ClickAddtocartBtnOnProduct = (By.XPATH, "//div[@class='button-group']//button[1]")
    ClickRightsideCartBtn = (By.ID, "cart-total")
    ClickViewCartBtn = (By.XPATH, "//strong[text()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.App_Url)

    def do_click_tablet(self):
        self.do_click(self.ClickTabletsInMenu)

    def do_click_product_cart_btn(self):
        self.do_click(self.ClickAddtocartBtnOnProduct)

    def do_click_top_totalcart_btn(self):
        self.do_click(self.ClickRightsideCartBtn)

    def do_click_view_cart_btn(self):
        self.do_click(self.ClickViewCartBtn)
