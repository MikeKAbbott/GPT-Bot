import openai
import os

from openai.openai_object import OpenAIObject
from dotenv import load_dotenv
from utils.Sanitize import sanitize

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatGPT:
  
  __model: str = 'gpt-3.5-turbo'
  
  __messages: list = [{
      'role': 'system',
      'content': 'You are a helpful assistant.',
    }]

  def __init__(self):
    pass

  @classmethod
  def add_message(self, role: str, message: str) -> None:
    self.__messages.append({
      'role': role,
      'content': sanitize(message),      
    })
  
  @classmethod
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
  
  @classmethod
  def clear_messages(self) -> None:
    self.__messages = [{
      'role': 'system',
      'content': 'You are a helpful assistant.',
    }]