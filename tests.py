from unittest import TestCase
import unittest
from check_pwd import check_pwd


class TestCase(TestCase):

    def testLengthRequirement(self):
        self.assertFalse(check_pwd("cD24#"),)

    def test_Lower_case(self):
        self.assertFalse(check_pwd("CD%2AC(5"))

    def test_Upper_case(self):
        self.assertFalse(check_pwd("cd@5abv$ef)qh^2"))

    def test_Digit(self):
        self.assertFalse(check_pwd("Cdsf~jFJ`szK&2sL_"))

    def test_Special_Character(self):
        self.assertFalse(check_pwd("nN825Qn9QQo2rQp1H"))

if __name__ == '__main__':
    unittest.main()
