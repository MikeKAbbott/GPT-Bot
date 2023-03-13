import unittest

from unittest import TestSuite
from src.utils.IsEmptyString import is_empty_string
from src.utils.Sanitize import sanitize
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

def suite() -> TestSuite:
  suite: TestSuite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestUtils))

  return suite

