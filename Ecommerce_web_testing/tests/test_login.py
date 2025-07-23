import pytest
from pages.login_page import LoginPage
from utility.helpers import handle_error
from utility.config_loader import load_env_config
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_user_login(driver, request):
    env = request.config.getoption("--env")
    config = load_env_config(env)    
    try:
        driver.get(f"{config['base_url']}/login")
        login_data = config["user"]["valid"]
        login_page = LoginPage(driver)
        login_page.login(login_data['username'], login_data['password'])
        assert login_page.is_successfully_login_in(), "User was not able to log in successfully"
    except Exception as e:
        handle_error(test_user_login, driver, e)
        raise