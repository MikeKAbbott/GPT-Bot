import discord
import unittest

from unittest import TestSuite
from src.utils.IsEmptyString import is_empty_string
from src.utils.Sanitize import sanitize
from src.utils.CreateDiscordEmbed import DiscordEmbed
from dotenv import load_dotenv

load_dotenv()

class TestUtils(unittest.TestCase):

  def test_is_empty_string(self):
    populated_string: str = 'Test String'
    empty_string: str = ''
    none_string = None

    self.assertEqual(
      is_empty_string(populated_string),
      False,
      'Should return a False when the string is not empty',
    )

    self.assertEqual(
      is_empty_string(empty_string),
      True,
      'Should return a True when the string is empty',
    )

    self.assertEqual(
      is_empty_string(none_string),
      True,
      'Should return a True when the string is none',
    )

  def test_santize(self):
    test_string = ' Test Str\ning '

    self.assertEqual(
      sanitize(test_string),
      'Test String',
      'Should return a string with removed white spaces and new lines',
    )
  def test_create_embed(self):
    test_embed: DiscordEmbed = DiscordEmbed(
      description = '@TestUser',
    )

    test_content: list = [
      {
      'title': 'User Message',
      'content': 'This is a test user message'
      },
      {
      'title': 'ChatGPT Response',
      'content': 'This is a test ChatGPT response'
      },
    ]
    
    self.assertEqual(
      test_embed.embed.description,
      '@TestUser',
      'Should return the test embeds description',
    )
    
    for index, content in enumerate(test_content):
      test_embed.add_content(
        content['title'],
        content['content'],
      )
      
      self.assertEqual(
        test_embed.embed.fields[index].name,
        content['title'],
        'Should return the fields name'
      )
      
      self.assertEqual(
        test_embed.embed.fields[index].value,
        content['content'],
        'Should return the fields content value'
      )

def suite() -> TestSuite:
  suite: TestSuite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestUtils))

  return suite

