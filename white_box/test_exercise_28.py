import unittest
from unittest.mock import patch, MagicMock
from white_box.class_exercises import exercise_28

class TestExercise28(unittest.TestCase):
    
    @patch('white_box.class_exercises.requests.get')
    def test_successful_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'test'}
        mock_get.return_value = mock_response
        
        result = exercise_28('http://api.test.com')
        
        mock_get.assert_called_once_with('http://api.test.com')
        self.assertEqual(result, {'data': 'test'})
    
    @patch('white_box.class_exercises.requests.get')
    def test_api_call_404(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = exercise_28('http://api.test.com')
        
        self.assertIsNone(result)
    
    @patch('white_box.class_exercises.requests.get')
    def test_api_call_500(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        result = exercise_28('http://api.test.com')
        
        self.assertIsNone(result)
    
    @patch('white_box.class_exercises.requests.get')
    def test_api_call_exception(self, mock_get):
        mock_get.side_effect = Exception('Connection error')
        
        result = exercise_28('http://api.test.com')
        
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
    