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