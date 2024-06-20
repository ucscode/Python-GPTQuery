from typing import Union, List
from PIL import Image
from packages.extractor import Extractor

class GPTChat:

    __formation = []

    def __init__(self):
        self.set_image_detail('auto')

    def get_content(self):
        return self.__formation
    
    def set_system_context(self, message: str):
        context = {
            'role': 'system', 
            'content': message
        }
        index = self.__has_initial_context()
        if index is False:
            self.__formation.insert(0, context)
        else:
            self.__formation[index] = context
    
    def __has_initial_context(self) -> Union[int, None]:
        for key, value in enumerate(self.__formation):
            if value['role'] == 'system':
                return key
        return False
    
    def set_image_detail(self, quality: str):
        if not quality in ['auto', 'high', 'low']:
            raise Exception('Invalid image quality type')
        self.__image_detail = quality

    def add_assistant(self, message):
        self.__formation.append({
            "role": "assistant",
            "content": message,
        })
        return self

    def add_user(self, content: Union[str, Image.Image, List[Union[str, Image.Image]]]):
        if not isinstance(content, list):
            content = [content]

        linear_content = []

        for value in content:
            if isinstance(value, list):
                for image in value:
                    linear_content.append(image)
            else:
                linear_content.append(value)

        self.__formation.append({
            "role": "user",
            "content": list(map(lambda value: self.__build_user_content(value), linear_content))
        })
        return self
    
    def __build_user_content(self, value: Union[str, Image.Image]):
        if isinstance(value, str):
            return {
                'type': 'text',
                'text': value
            }
        else:
            base64_image = Extractor().image_to_base64(value)
            return {
                'type': 'image_url',
                'image_url': {
                    'url': f"data:image/png;base64,{base64_image}",
                    'detail': self.__image_detail
                }
            }