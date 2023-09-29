# threads_interactions.py
from selenium.webdriver.common.by import By

def login(driver, username, password):
    """
    Login to Threads.net.
    
    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    username (str): Username for Threads.net.
    password (str): Password for Threads.net.
    """
    driver.get('https://www.threads.net/login')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
