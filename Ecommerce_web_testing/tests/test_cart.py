import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utility.helpers import handle_error
from utility.helpers import take_screenshot
from utility.config_loader import load_env_config
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_to_cart(driver, request):
    env = request.config.getoption("--env")
    config = load_env_config(env)    
    try:
        driver.get(f"{config['base_url']}/login")
        login_data = config["user"]["valid"]
        LoginPage(driver).login(login_data['username'], login_data['password'])
        take_screenshot(driver, "logged_in_screenshot")
        product_Page = ProductPage(driver)
        product_Page.browser_category()
        product_Page.select_product()
        take_screenshot(driver, "product_selected_screenshot")
        cart_page = CartPage(driver)
        cart_page.add_to_cart()
        cart_page.open_cart
        take_screenshot(driver, "cart_page_screenshot")
        assert cart_page.is_product_in_cart(), "Product was not added to the cart"
    except Exception as e:
        handle_error(test_add_to_cart, driver, e)
        raise