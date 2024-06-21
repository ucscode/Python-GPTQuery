## How to use

```python
from packages.vision import Vision
from packages.gpt_chat import GPTChat
from PIL import Image

chat = GPTChat()

# set initial system message
chat.set_system_context('You are a helpful assistant')

# start conversation
chat.add_assistant('How can I help you today')

chat.add_user('Well I need you to check an image for me')

chat.add_assistance('Please upload the image for inspection and state your requirement')

chat.add_user([
    'I would like you to tell me what is in the following image',
    Image.open('image.png', 'r'),
])

# initialize vision

vision = Vision()

response = vision.query_gpt(chat, max_token=300)

response.choices[0].message.content
```