import unittest

from src.bot.Bot import Bot
from dotenv import load_dotenv

load_dotenv()

class TestBot(unittest.TestCase):

  bot: Bot = Bot()

  def test_is_running():
    pass

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestBot))

  return suite
