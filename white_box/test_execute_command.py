import unittest
"""
Test suite for the execute_command function.
This module contains unit tests for the execute_command function from the mockup_exercises module.
It uses mocking to verify that the function correctly calls subprocess.run with the expected parameters
and properly handles exceptions when commands fail.
Classes:
    Test_execute_command: Test class containing test cases for execute_command function.
Test Cases:
    test_execute_command: Verifies that:
        - execute_command returns the expected output ('command output')
        - subprocess.run is called exactly once with the correct parameters (command, shell=True, capture_output=True, text=True)
        - execute_command properly raises an Exception when subprocess.run fails
"""
from white_box.mockup_exercises import execute_command
from unittest.mock import patch

class Test_execute_command(unittest.TestCase):
    @patch('mockup_exercises.execute_command.subprocess.run') 
    def test_execute_command(self, mock):
        output = execute_command('ls')
        self.assertEqual(output, 'command output')
        mock.assert_called_once_with('ls', shell=True, capture_output=True, text=True)
        mock.reset_mock()
        mock.side_effect = Exception('Command failed')
        with self.assertRaises(Exception):
            execute_command('invalid_command')