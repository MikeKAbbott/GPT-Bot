import openai
import os

from dotenv import load_dotenv
from openai.openai_object import OpenAIObject
from src.utils.Sanitize import sanitize

class ChatGPT:
  _base_messages: list = [{
    'role': 'system',
    'content': 'You are a helpful assistant.',
  }]

  _model: str = 'gpt-3.5-turbo'

  def __init__(self):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    self._messages = self._base_messages

  def _add_message(self, role: str, message: str) -> None:
    self._messages.append({
      'role': role,
      'content': sanitize(message),      
    })

  def chat(self, user_message: str) -> str:
    try:
      self._add_message('user', user_message)

      response: OpenAIObject = openai.ChatCompletion.create(
        model = self._model,
        messages = self._messages
      )

      gpt_message: str = sanitize(response.get('choices')[0].message.content)
      self._add_message('assistant', gpt_message)

      return { 
        'content': gpt_message,
        'status': 200,
      }

    except Exception as e:
      print(e)
      return {
        'content': 'Sorry, something when wrong. Could you repeat that?',
        'status': 404,
      }

  def clear_messages(self) -> None:
    self._messages = self._base_messages
