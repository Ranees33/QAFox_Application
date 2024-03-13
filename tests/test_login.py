import time

import pytest

from pageObjects.loginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login(self):
        to_login = LoginPage(self.driver)
        to_login.do_click_myaccount_to_login()
        to_login.do_click_login()
        to_login.do_enter_email("tonyboniee@gmail.com")
        to_login.do_enter_password("tonyboniee")
        to_login.do_click_login_btn()
        to_login.do_click_myaccount_to_logout()
        to_login.do_click_logout()
        time.sleep(10)
        actual_Text = to_login.get_account_logout_text()
        expected_Text = "Account Logut"
        # Using assertion to verifying the text!
        assert actual_Text == expected_Text, f"Expected: {expected_Text}, Actual: {actual_Text}"
        actual_Title = to_login.get_logout_page_title()
        # Using assertion to verifying the page title!
        assert actual_Title is not None and "Account Logout" in actual_Title
        print("Assertion Test Passed")
