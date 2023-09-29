# Update bot.py

from content_generator import generate_post_title_and_content, generate_reply
from threads_interactions import post_content, reply_to_comment, login  
from config import Config
from logger_setup import setup_logger
from chrome_setup import setup_chrome_driver 
logger = setup_logger('InfluencerBot')


def main():
    """
    Main function to orchestrate the influencer bot activities.
    """
    driver = setup_chrome_driver()
    login(driver, Config.THREADS_NET_USERNAME, Config.THREADS_NET_PASSWORD)

    logger.info('Bot started')

    # Post new content
    title, content = generate_post_title_and_content()
    post_content(driver, title, content)
    
    # Assume we have a function to get comments and their ids
    comments = get_comments(driver, 'post_url_here')
    for comment_id, comment_text in comments:
        reply_text = generate_reply(comment_text)
        reply_to_comment(driver, 'post_url_here', comment_id, reply_text)
    logger.info('Bot finished')


if __name__ == "__main__":
    main()
