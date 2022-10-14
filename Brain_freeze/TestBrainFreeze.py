import unittest
from BrainFreeze import BrainFreeze


# Test cases to test BrainFreeze methods
# You always create  a child class derived from unittest.TestCase
class TestBrainFreeze(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.brainfreeze = BrainFreeze()

    # Each test method starts with the keyword test_
    def test_multiplication_operator(self):
        self.assertEqual(self.brainfreeze.multiplication_operator(68, 2), 136)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
