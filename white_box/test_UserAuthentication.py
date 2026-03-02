import unittest
from class_exercises import UserAuthentication
class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.myUserAuthentication = UserAuthentication()
        self.assertEqual(self.myUserAuthentication.state, "Logged Out")

    def test_login_Logged_Out(self):
        self.myUserAuthentication.state = "Logged Out"
        self.assertEqual(self.myUserAuthentication.login(), "Login successful")
        self.assertEqual(self.myUserAuthentication.state, "Logged In")

    def test_login_not_Logged_Out(self):
        self.myUserAuthentication.state = "Logged In"
        self.assertEqual(self.myUserAuthentication.login(), "Invalid operation in current state")

    def test_logout(self):
        self.myUserAuthentication.state = "Logged In"
        self.myUserAuthentication.logout()
        self.assertEqual(self.myUserAuthentication.state, "Logged Out")