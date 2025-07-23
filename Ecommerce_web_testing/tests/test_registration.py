import pytest
from pages.registration_page import RegistrationPage
from utility.helpers import handle_error
from utility.config_loader import load_env_config
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_user_registration(driver, request):
    env = request.config.getoption("--env")
    config = load_env_config(env)    
    try:
        driver.get(f"{config['base_url']}/login")
        registration_data = config["user"]["valid"]
        RegistrationPage = RegistrationPage(driver)
        registration_data.login(registration_data['username'], registration_data['password'])
        assert RegistrationPage.is_registration_successful(), "User was not able to log in successfully"
    except Exception as e:
        handle_error(test_user_registration, driver, e)
        raise