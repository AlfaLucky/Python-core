import unittest
from ICode import ICode


# Test cases to test ICode methods
# You always create  a child class derived from unittest.TestCase
class TestICode(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.icode = ICode()

    # Each test method starts with the keyword test_
    def test_multiplication_operator(self):
        self.assertEqual(self.icode.string_operator("I'm a programmer"), "I'm a programmer")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
