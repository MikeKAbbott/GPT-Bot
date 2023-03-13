import unittest
import TestChatGPT
import TestUtils

from unittest import TestSuite

TEST_MODULES: list = [
  TestChatGPT,
  TestUtils,
]

def suite():
  suite: TestSuite = unittest.TestSuite()

  for module in TEST_MODULES:
    suite.addTest(module.suite())

  return suite

if __name__ == '__main__':
  unittest.main(
    defaultTest='suite',
    verbosity = 2,
  )
