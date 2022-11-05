import unittest
from MultipleVariables import MultipleVariables


# Test cases to test Multiple Variables methods
# You always create  a child class derived from unittest.TestCase
class TestMultipleVariables(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.multiple_variables = MultipleVariables()

    # Each test method starts with the keyword test_
    def test_multiple_variables(self):
        self.assertEqual(self.multiple_variables.multiple_variables("ni", '3'), "ninini")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
