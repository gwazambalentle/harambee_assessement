import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from utility.helpers import handle_error
from utility.config_loader import load_env_config
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_browse_product(driver, request):
    env = request.config.getoption("--env")
    config = load_env_config(env)    
    try:
        driver.get(f"{config['base_url']}/login")
        login_data = config["user"]["valid"]
        LoginPage(driver).login(login_data['username'], login_data['password'])
        product_Page = ProductPage(driver)
        product_Page.browser_category()
        product_Page.select_product()
        
        assert product_Page.is_product_displayed(), "Product details not displayed"
    except Exception as e:
        handle_error(test_browse_product, driver, e)
        raise