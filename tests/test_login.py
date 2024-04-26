import logging
import time

import pytest

from pageObjects.loginPage import LoginPage
from utilities.logger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.regression
# @pytest.mark.skip(reason="Need to run the checkout page test case separately")
class TestLogin:
    logger = LogGen.log_gen()

    def test_login(self):
        logging.info("Program execution started")
        to_login = LoginPage(self.driver)
        to_login.do_click_myaccount_to_login()
        to_login.do_click_login()
        to_login.do_enter_email("tonyboniee@gmail.com")
        to_login.do_enter_password("tonyboniee")
        to_login.do_click_login_btn()
        to_login.do_click_myaccount_to_logout()
        to_login.do_click_logout()
        time.sleep(5)
        # Using assertion to verifying the text!
        actual_Text = to_login.get_account_logout_text()
        expected_Text = "Account Logout"
        assert actual_Text == expected_Text, f"Expected: {expected_Text}, Actual: {actual_Text}"
        # Using assertion to verifying the page title!
        actual_Title = to_login.get_logout_page_title()
        assert actual_Title is not None and "Account Logout" in actual_Title
        print("Assertion Test Passed")
        to_login.do_click_continue_btn()
        print("The Webpage Url after continue the Logout: ", to_login.get_page_url_after_continue_logout())
        logging.info("Program execution ended")
