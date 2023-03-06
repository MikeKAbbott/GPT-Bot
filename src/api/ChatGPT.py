import openai
import os

from dotenv import load_dotenv
from openai.openai_object import OpenAIObject
from utils.Sanitize import sanitize

class ChatGPT:

  __model: str = 'gpt-3.5-turbo'

  __messages: list = [{
    'role': 'system',
    'content': 'You are a helpful assistant.',
  }]

  def __init__(self):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

  def add_message(self, role: str, message: str) -> None:
    self.__messages.append({
      'role': role,
      'content': sanitize(message),      
    })
  
  def chat(self, user_message: str) -> str:
    try:
      self.add_message('user', user_message)

      response: OpenAIObject = openai.ChatCompletion.create(
        model = self.__model,
        messages = self.__messages
      )

      gpt_message: str = sanitize(response.get('choices')[0].message.content)
      self.add_message('assistant', gpt_message)

      return gpt_message

    except Exception as e:
      print(e)
      return 'Sorry, something when wrong. Could you repeat that?'

  def clear_messages(self) -> None:
    self.__messages = [{
      'role': 'system',
      'content': 'You are a helpful assistant.',
    }]
