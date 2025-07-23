import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for testing
    driver = webdriver.Chrome(options=options)
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against ( dev/stage/prod )")