from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_container")
    CART_ITEM= (By.CLASS_NAME, "cart_item_label")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
    def open_cart(self):
        self.click(self.CART_ICON)

    def is_product_in_cart(self):
        return self.is_displayed(self.CART_ITEM)
 


    