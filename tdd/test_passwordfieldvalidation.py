import unittest
from passwordfieldvalidation import PasswordFieldValidation 

class TestPasswordFieldValidation(unittest.TestCase):
    def setUp(self):
        self.validator = PasswordFieldValidation()
        def test_password_too_short(self):
            result = self.validator.validate("short")
            self.assertFalse(result['valid'])
            self.assertIn("Password must be at least 8 characters", result['errors'])

        def test_password_valid_length(self):
            result = self.validator.validate("validpass123")
            self.assertTrue(result['valid'])
            self.assertEqual([], result['errors'])

    def test_password_missing_numbers(self):
        result = self.validator.validate("validpass1")
        self.assertFalse(result['valid'])
        self.assertIn("The password must contain at least 2 numbers", result['errors'])

    def test_password_with_two_numbers(self):
        result = self.validator.validate("validpass12")
        self.assertTrue(result['valid'])
        self.assertEqual([], result['errors'])

        def test_password_multiple_errors(self):
        result = self.validator.validate("somepassword")
        self.assertFalse(result['valid'])
        self.assertIn("Password must be at least 8 characters", result['errors'])
        self.assertIn("The password must contain at least 2 numbers", result['errors'])
        def test_password_missing_capital_letter(self):
            result = self.validator.validate("validpass12")
            self.assertFalse(result['valid'])
            self.assertIn("password must contain at least one capital letter", result['errors'])

        def test_password_with_capital_letter(self):
            result = self.validator.validate("Validpass12")
            self.assertTrue(result['valid'])
            self.assertEqual([], result['errors'])

        def test_password_missing_special_character(self):
            result = self.validator.validate("Validpass12")
            self.assertFalse(result['valid'])
            self.assertIn("password must contain at least one special character", result['errors'])

        def test_password_with_special_character(self):
            result = self.validator.validate("Validpass12!")
            self.assertTrue(result['valid'])
            self.assertEqual([], result['errors'])