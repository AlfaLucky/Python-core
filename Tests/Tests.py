import unittest
from BrainFreeze import BrainFreeze
from HowManyMiles import HowManyMiles
from ICode import ICode
from MultipleVariables import MultipleVariables
from NewLinesInStrings import NewLinesInStrings
from StringsOperations import StringsOperations
from Variables import Variables


# Test cases to test methods
# You always create  a child class derived from unittest.TestCase
class TestPythonCore(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.brain_freeze = BrainFreeze()
        self.how_many_miles = HowManyMiles()
        self.i_code = ICode()
        self.multiple_variables = MultipleVariables()
        self.newlines_in_strings = NewLinesInStrings()
        self.strings_operations = StringsOperations()
        self.variables = Variables()

    def test_multiplication_operator(self):
        self.assertEqual(self.brain_freeze.multiplication_operator(68, 2), 136)

    def test_division_operator(self):
        self.assertEqual(self.how_many_miles.division_operator(1000, 1.6), 624)

    def test_i_code(self):
        self.assertEqual(self.i_code.string_operator("I'm a programmer"), "I'm a programmer")

    def test_multiple_variables(self):
        self.assertEqual(self.multiple_variables.multiple_variables("ni", '3'), "ninini")

    def test_newlines_in_strings(self):
        self.assertEqual(self.newlines_in_strings.newlines_in_strings("A\nB\nC\nD"), "A\nB\nC\nD")

    def test_strings_operations(self):
        self.assertEqual(self.strings_operations.strings_operations("ni"), "ninini!")

    def test_variables(self):
        self.assertEqual(self.variables.Variables(7, 3), 343)

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
