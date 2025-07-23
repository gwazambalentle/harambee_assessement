import os
from datetime import datetime

def take_screenshot(driver, test_name):
    """
    Takes a screenshot of the current browser window.
    
    :param driver: The Selenium WebDriver instance.
    :param test_name: The name of the test for which the screenshot is taken.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"screenshots/{name}_{timestamp}.png"
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    
    #save the screenshot
    driver.save_screenshot(screenshot_path)

    #print the path to the screenshot
    print(f"Screenshot saved to {screenshot_path}")

def handle_error(test_name, driver, e):
    print(f"[Error] {test_name}: failed: {e}")
    take_screenshot(driver, test_name)