import unittest

from dotenv import load_dotenv
from src.utils.IsEmptyString import is_empty_string
from src.utils.Sanitize import sanitize
from unittest import TestSuite

load_dotenv()

class TestUtils(unittest.TestCase):

  def test_is_empty_string(self):
    populated_string: str = 'Test String'
    empty_string: str = ''
    none_string = None

    self.assertEqual(
      msg = 'Should return a False when the string is not empty',
      first = is_empty_string(populated_string),
      second = False,
    )

    self.assertEqual(
      msg = 'Should return a True when the string is empty',
      first = is_empty_string(empty_string),
      second = True,
    )

    self.assertEqual(
      msg = 'Should return a True when the string is none',
      first = is_empty_string(none_string),
      second = True,
    )

  def test_santize(self):
    test_string = ' Test Str\ning '

    self.assertEqual(
      msg = 'Should return a string with removed white spaces and new lines',
      first = sanitize(test_string),
      second = 'Test String',
    )

def suite() -> TestSuite:
  suite: TestSuite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestUtils))

  return suite

