#! python3
import unittest
import sys


def testInputString():
    print(sys.argv)
    # self.assertEqual(True, False)  # add assertion here

class MyTestCase(unittest.TestCase):
    pass


if __name__ == '__main__':
    # unittest.main()
    testInputString()