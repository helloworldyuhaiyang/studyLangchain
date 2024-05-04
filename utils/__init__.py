from .constant import api_key
from .constant import openai_model
from .constant import openai_chat_model
from .constant import openai_embedding
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
