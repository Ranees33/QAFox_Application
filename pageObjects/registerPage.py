from selenium.webdriver.common.by import By

from configProperties.configinfo import Testdata
from pageObjects.basePage import BasePage


class RegisterPage(BasePage):
    Click_MyAccount = (By.XPATH, "//span[text()='My Account']")
    Click_Register = (By.LINK_TEXT, "Register")
    Enter_Firstname = (By.ID, "input-firstname")
    Enter_Lastname = (By.ID, "input-lastname")
    Enter_Email = (By.ID, "input-email")
    Enter_Phonenumber = (By.ID, "input-telephone")
    Enter_Password = (By.ID, "input-password")
    Enter_Password_Confirm = (By.ID, "input-confirm")
    Select_Privacypolicy = (By.NAME, "agree")
    Click_Submit_Btn = (By.XPATH, "//input[@type='submit']")
    Click_Continue_Btn = (By.LINK_TEXT, "Continue")
    Get_Email_AlreadyReg_Text = (By.XPATH, "//*[@id='account-register']/div[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.App_Url)

    def do_click_myaccount(self):
        self.do_click(self.Click_MyAccount)

    def do_click_register(self):
        self.do_click(self.Click_Register)

    def do_enter_firstname(self, text):
        self.do_send_keys(self.Enter_Firstname, text)

    def do_enter_lastname(self, text):
        self.do_send_keys(self.Enter_Lastname, text)

    def do_enter_email(self, text):
        self.do_send_keys(self.Enter_Email, text)

    def do_enter_phone_number(self, text):
        self.do_send_keys(self.Enter_Phonenumber, text)

    def do_enter_password(self, text):
        self.do_send_keys(self.Enter_Password, text)

    def do_enter_password_for_confirm(self, text):
        self.do_send_keys(self.Enter_Password_Confirm, text)

    def do_select_privacy(self):
        self.do_click(self.Select_Privacypolicy)

    def do_click_submit_btn(self):
        self.do_click(self.Click_Submit_Btn)

    # def do_click_continue_btn(self):
    #     self.do_click(self.Click_Continue_Btn)
    #
    # def get_account_created_success_url(self):
    #     account_creation_URL = self.get_current_url(self)
    #     print("The Url for created a new account is : " + account_creation_URL)

    def get_email_already_registrd_text(self):
        return self.get_element_text(self.Get_Email_AlreadyReg_Text)




