from openai import OpenAI
from typing import Union
from PIL import Image
from packages.gpt_chat import GPTChat
import base64
from io import BytesIO

class Vision():

    __gpt_models = [
        'gpt-4o', # [text, image] @ 128K content length
        'gpt-4-turbo', # [text, image] @ 128K content length
    ]

    __model = 'gpt-4o'
    
    def __init__(self, openai_api_key: str):
        self.set_model(self.__gpt_models[0])
        self.client = OpenAI(api_key=openai_api_key)

    def set_model(self, model: str) -> None:
        # set gpt model to use
        if model.lower() not in self.__gpt_models:
            raise Exception('The specified model does not have vision capability')
        self.__model = model
        
    def query_gpt(self, chat: GPTChat, max_tokens: int = 300):
        return self.client.chat.completions.create(
            model=self.__model,
            messages=chat.get_content(),
            max_tokens=max_tokens
        )