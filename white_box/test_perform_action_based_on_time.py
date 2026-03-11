import unittest
from unittest.mock import patch
from mockup_exercises import perform_action_based_on_time

class Test_perform_action_based_on_time(unittest.TestCase):

    @patch('mockup_exercises.time.time')
    def test_action_a(self, mock_time):
        mock_time.return_value = 5
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch('mockup_exercises.time.time')
    def test_action_b(self, mock_time):
        mock_time.return_value = 15
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")

    @patch('mockup_exercises.time.time')
    def test_action_b_boundary(self, mock_time):
        mock_time.return_value = 10
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        

    @patch('mockup_exercises.time.time')
    def test_action_a_boundary(self, mock_time):
        mock_time.return_value = 9
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")