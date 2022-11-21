#!/usr/bin/python3
import unittest

from If_else import if_else
from Loop import loop

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        x = 10
        y = 5
        result_1 = if_else(x,y)

        n = 5
        result_2 = loop(n)

        self.assertEqual(result_1, 15)
        self.assertEqual(result_2, 15)

if __name__ == '__main__':
    unittest.main()