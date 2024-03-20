import pytest

from pageObjects.checkoutPage import CheckoutPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestCheckout:
    def test_checkout_quantity_value_adding(self):
        checkout_quantity_adding = CheckoutPage(self.driver)
        checkout_quantity_adding.do_click_tablet_menu()
        checkout_quantity_adding.do_click_product_addtocart_btn()
        checkout_quantity_adding.do_click_rightside_itemcart_btn()
        checkout_quantity_adding.do_click_checkout_link()
        checkout_quantity_adding.do_click_cart_quantity_box()
        checkout_quantity_adding.do_clear_textbox()
        checkout_quantity_adding.do_enter_quantity_value("2")
        checkout_quantity_adding.takes_screenshot()
        print("Successfully quantity '2' nos has been added")

