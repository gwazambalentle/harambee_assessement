from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON= (By.ID, "login-button")
    MAIN_MENU = (By.ID, "inventory_container")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_successfully_login_in(self):
        return self.is_displayed(self.MAIN_MENU)