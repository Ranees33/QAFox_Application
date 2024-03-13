from selenium.webdriver.common.by import By

from configProperties.configinfo import Testdata
from pageObjects.basePage import BasePage


class LoginPage(BasePage):
    Click_MyAccount_To_Login = (By.XPATH, "//span[text()='My Account']")
    Click_Login = (By.LINK_TEXT, "Login")
    Enter_Email = (By.ID, "input-email")
    Enter_Password = (By.ID, "input-password")
    Click_Login_Btn = (By.XPATH, "//input[@class='btn btn-primary']")
    Click_MyAccount_To_Logout = (By.XPATH, "//span[text()='My Account']")
    Click_Logout = (By.XPATH, "//div[@id='top-links']/ul[1]/li[2]/ul[1]/li[5]/a[1]")
    Get_Account_Logout_Text = (By.XPATH, "//div[@class='col-sm-9']//h1[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.App_Url)

    def do_click_myaccount_to_login(self):
        self.do_click(self.Click_MyAccount_To_Login)

    def do_click_login(self):
        self.do_click(self.Click_Login)

    def do_enter_email(self, text):
        self.do_send_keys(self.Enter_Email, text)

    def do_enter_password(self, text):
        self.do_send_keys(self.Enter_Password, text)

    def do_click_login_btn(self):
        self.do_click(self.Click_Login_Btn)

    def do_click_myaccount_to_logout(self):
        self.do_click(self.Click_MyAccount_To_Logout)

    def do_click_logout(self):
        self.do_click(self.Click_Logout)

    def get_account_logout_text(self):
        return self.get_element_text(self.Get_Account_Logout_Text)

    def get_logout_page_title(self):
        return self.get_page_title(self.driver.title)



