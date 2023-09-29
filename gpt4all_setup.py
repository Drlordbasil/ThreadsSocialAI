# gpt4all_setup.py
from gpt4all import GPT4All

def setup_gpt4all(model_path):
    """
    Setup GPT4All model.
    
    Parameters:
    model_path (str): Path to the GPT-4 model file.
    
    Returns:
    GPT4All: Instance of the GPT4All model.
    """
    model = GPT4All(model_path)
    return model
