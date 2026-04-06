import unittest
from stringcalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_that_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_new_lines_as_separators(self):
        self.assertEqual(self.calculator.add("1\n2\n3"), 6)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)

    def test_separator_at_end_raises_error(self):
        with self.assertRaises(ValueError):
            self.calculator.add("1,2,")
