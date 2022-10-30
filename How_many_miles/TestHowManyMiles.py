import unittest
from HowManyMiles import HowManyMiles


# Test cases to test HowManyMiles methods
# You always create  a child class derived from unittest.TestCase
class TestHowManyMiles(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.howmanymiles = HowManyMiles()

    # Each test method starts with the keyword test_
    def test_division_operator(self):
        self.assertEqual(self.howmanymiles.division_operator(1000, 1.6), 624)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
