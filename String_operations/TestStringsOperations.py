import unittest
from StringsOperations import StringsOperations


# Test cases to test StringsOperations methods
# You always create  a child class derived from unittest.TestCase
class TestStringsOperations(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.newlines_in_strings = StringsOperations()

    # Each test method starts with the keyword test_
    def test_newlines_in_strings(self):
        self.assertEqual(self.newlines_in_strings.strings_operations("ni"), "ninini!")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
