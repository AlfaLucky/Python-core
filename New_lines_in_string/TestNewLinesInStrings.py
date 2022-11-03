import unittest
from NewLinesInStrings import NewLinesInStrings


# Test cases to test NewLinesInStrings methods
# You always create  a child class derived from unittest.TestCase
class TestNewLinesInStrings(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.newlines_in_strings = NewLinesInStrings()

    # Each test method starts with the keyword test_
    def test_newlines_in_strings(self):
        self.assertEqual(self.newlines_in_strings.newlines_in_strings("A\nB\nC\nD"), "A\nB\nC\nD")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
