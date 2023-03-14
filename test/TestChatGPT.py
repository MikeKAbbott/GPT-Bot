import unittest

from dotenv import load_dotenv
from src.api.ChatGPT import ChatGPT

load_dotenv()

class TestChatGPT(unittest.TestCase):

  gpt: ChatGPT = ChatGPT()
  
  def test_authorization(self):
    response: dict = self.gpt.chat('This is a test message.')

    self.assertEqual(
      msg = 'Should return a 200 status code when making a request to ChatGPT API',
      first = response['status'],
      second = 200,
    )

  def test_add_user_message(self):
    self.gpt.reset()
    response: dict = self.gpt.chat('This is a test message.')

    self.assertIn(
      msg = 'Should check that a users message is in the messages list',
      member = {'role': 'user', 'content': 'This is a test message.'},
      container = self.gpt.messages,
    )
  
  
  def test_reset(self):
    self.gpt.reset()

    self.assertEqual(
      msg = 'Should return an array of chats base message',
      first = self.gpt.messages,
      second = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    )

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestChatGPT))

  return suite
