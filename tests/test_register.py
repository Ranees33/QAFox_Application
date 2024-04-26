import logging
import time

import pytest

from pageObjects.registerPage import RegisterPage
from utilities.logger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
# @pytest.mark.skip(reason="Need to run the login test case separately")
class TestRegister:
    logger = LogGen.log_gen()

    def test_register(self):
        logging.info("Program execution started")
        to_create_an_account = RegisterPage(self.driver)
        to_create_an_account.do_click_myaccount()
        to_create_an_account.do_click_register()
        to_create_an_account.do_enter_firstname("Tony")
        to_create_an_account.do_enter_lastname("Boniee")
        to_create_an_account.do_enter_email("tonyboniee@gmail.com")
        to_create_an_account.do_enter_phone_number("0123456789")
        to_create_an_account.do_enter_password("tonyboniee")
        to_create_an_account.do_enter_password_for_confirm("tonyboniee")
        to_create_an_account.do_select_privacy()
        to_create_an_account.do_click_submit_btn()
        # to_create_an_account.do_click_continue_btn()
        # to_create_an_account.get_account_created_success_url()
        time.sleep(5)
        # Using assertion to verifying the text!
        actual_Text = to_create_an_account.get_email_already_registrd_text()
        expected_Text = "Warning: E-Mail Address is already registered!"
        assert actual_Text == expected_Text, f"Expected: {expected_Text}, Actual: {actual_Text}"
        print("This Email Address Already Registered Text is : " +
              to_create_an_account.get_email_already_registrd_text())
        logging.info("Program execution ended")



