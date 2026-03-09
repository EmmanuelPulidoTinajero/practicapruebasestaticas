import unittest



from unittest.mock import patch, mock_open
from white_box.class_exercises import exercise_27

class TestExercise27(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_read_file_success(self, mock_file):
        result = exercise_27('test.txt')
        mock_file.assert_called_once_with('test.txt', 'r')
        self.assertEqual(result, ['line1', 'line2', 'line3'])
    
    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_file_not_found(self, mock_file):
        result = exercise_27('nonexistent.txt')
        self.assertEqual(result, [])
    
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_empty_file(self, mock_file):
        result = exercise_27('empty.txt')
        self.assertEqual(result, [])
    
    @patch('builtins.open', new_callable=mock_open, read_data='single line')
    def test_single_line(self, mock_file):
        result = exercise_27('single.txt')
        self.assertEqual(result, ['single line'])

if __name__ == '__main__':
    unittest.main()