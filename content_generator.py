# content_generator.py

from gpt4all_setup import setup_gpt4all

model = setup_gpt4all("orca-mini-3b.ggmlv3.q4_0.bin")

def generate_post_title_and_content():
    """
    Generate a post title and content using GPT-4.
    
    Returns:
    tuple: Generated title and content.
    """
    title = model.generate("Generate a catchy post title about AI advancements", max_tokens=10)
    content = model.generate("Write a detailed post about recent advancements in AI", max_tokens=200)
    return title, content

def generate_reply(comment_text):
    """
    Generate a reply to a given comment using GPT-4.
    
    Parameters:
    comment_text (str): Text of the comment to reply to.
    
    Returns:
    str: Generated reply.
    """
    reply = model.generate(f"Reply to: {comment_text}", max_tokens=50)
    return reply
