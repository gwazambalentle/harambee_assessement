from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    SUCCESS_MSG = (By.ID, "successfully_registered")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def is_registration_successful(self):
        return self.is_displayed(self.SUCCESS_MSG)