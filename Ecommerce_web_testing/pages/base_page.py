from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exception import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def alert_popout(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def enter_text(self, locator, text):
        return self.wait.until(EC.Visible_and_clickable(locator)).send_keys(text)
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def is_displayed(self, locator,timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException:
            return False
        