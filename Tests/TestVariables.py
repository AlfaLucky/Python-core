import unittest
from Variables import Variables


# Test cases to test variables methods
# You always create  a child class derived from unittest.TestCase
class TestVariables(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.variables = Variables()

    # Each test method starts with the keyword test_
    def test_variables(self):
        self.assertEqual(self.variables.Variables(7, 3), 343)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
