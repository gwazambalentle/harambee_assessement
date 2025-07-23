from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    CATEGORY_MENU = (By.ID, "react-burger-menu-btn")
    SELECT_ITEMS = (By.ID, "inventory_sidebar_link")
    PRODUCT_TITLE = (By.ID, "item_4_title_link")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

    def browser_category(self):
        self.click(self.CATEGORY_MENU)
        self.click(self.SELECT_ITEMS)

    def select_product(self):
        self.click(self.PRODUCT_TITLE)

    def is_product_displayed(self):
        return self.is_displayed(self.BACK_TO_PRODUCTS)
    