import unittest

from src.api.ChatGPT import ChatGPT
from src.bot.Bot import Bot
from dotenv import load_dotenv

load_dotenv()

class TestChatGPT(unittest.TestCase):
  gpt: ChatGPT = ChatGPT()
  
  def test_authorization(self):
    response: dict = self.gpt.chat('This is a test message.')

    self.assertEqual(
      response['status'],
      200,
      'Should return a 200 status code when making a request to ChatGPT API',
    )

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestChatGPT))

  return suite
