# chrome_setup.py
from selenium import webdriver

def setup_chrome_driver():
    """
    Setup Chrome WebDriver.
    
    Returns:
    WebDriver: Instance of Selenium WebDriver for Chrome.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver
