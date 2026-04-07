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
            def test_custom_delimiter_semicolon(self):
                self.assertEqual(self.calculator.add("//;\n1;3"), 4)

            def test_custom_delimiter_pipe(self):
                self.assertEqual(self.calculator.add("//|\n1|2|3"), 6)

            def test_custom_delimiter_multiple_characters(self):
                self.assertEqual(self.calculator.add("//sep\n2sep5"), 7)

            def test_invalid_mixed_delimiters_raises_error(self):
                with self.assertRaisesRegex(
                    ValueError,
                    r"I expected .* but .* found at position 3",
                ):
                    self.calculator.add("//|\n1|2,3")

                        def test_negative_numbers_raises_error(self):
                            with self.assertRaisesRegex(ValueError, r"Negative number\(s\) not allowed: -2"):
                                self.calculator.add("1,-2")

                        def test_multiple_negative_numbers_raises_error(self):
                            with self.assertRaisesRegex(ValueError, r"Negative number\(s\) not allowed: -4,-9"):
                                self.calculator.add("2,-4,-9")

                                    def test_multiple_errors_returns_all_messages(self):
                                        with self.assertRaisesRegex(
                                            ValueError,
                                            r"Negative number\(s\) not allowed: -3\n'' expected but .* found at position 3",
                                        ):
                                            self.calculator.add("//\n1|2,-3")

                                                def test_numbers_bigger_than_1000_are_ignored(self):
                                                    self.assertEqual(self.calculator.add("2,1001"), 2)