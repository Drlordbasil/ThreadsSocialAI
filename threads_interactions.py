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

def post_content(driver, title, content):
    """
    Post new content on Threads.net.
    
    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    title (str): Title of the post.
    content (str): Content of the post.
    """
    driver.get('https://www.threads.net/new-post')
    driver.find_element(By.ID, 'title').send_keys(title)
    driver.find_element(By.ID, 'content').send_keys(content)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

def reply_to_comment(driver, post_url, comment_id, reply_content):
    """
    Reply to a comment on a post.
    
    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    post_url (str): URL of the post.
    comment_id (str): ID of the comment to reply to.
    reply_content (str): Content of the reply.
    """
    driver.get(f'{post_url}#comment-{comment_id}')
    driver.find_element(By.CSS_SELECTOR, f'button[reply-to="{comment_id}"]').click()
    driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Write a reply..."]').send_keys(reply_content)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

def update_profile(driver, bio):
    """
    Update profile bio on Threads.net.
    
    Parameters:
    driver (WebDriver): Selenium WebDriver instance.
    bio (str): New bio text.
    """
    driver.get('https://www.threads.net/profile/edit')
    driver.find_element(By.ID, 'bio').clear()
    driver.find_element(By.ID, 'bio').send_keys(bio)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
