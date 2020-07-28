from unittest import TestCase
import unittest
from check_pwd import check_pwd


class TestCase(TestCase):

    def testLengthRequirement(self):
        self.assertFalse(check_pwd("aB1#"))

    def test_Lower_case(self):
        self.assertFalse(check_pwd("AB%2CD(3"))

    def test_Upper_case(self):
        self.assertFalse(check_pwd("ab@4cd$5ef)6gh^7"))

    def test_Digit(self):
        self.assertFalse(check_pwd("iEI~jFJ`kGK&lHL_"))

    def test_Special_Character(self):
        self.assertFalse(check_pwd("Mm8qNn9QOo0rPp1R"))
        

if __name__ == '__main__':
    unittest.main()