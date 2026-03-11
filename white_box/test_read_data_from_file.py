import unittest
from unittest.mock import patch
from mockup_exercises import read_data_from_file

class TestReadDataFromFile(unittest.TestCase):

    @patch('builtins.open')
    def test_read_data_from_file_exitoso(self, mock_open):
        archivo_falso = mock_open.return_value.__enter__.return_value
        archivo_falso.read.return_value = "hola esto es un archivo"

        result = read_data_from_file("hola.py")

        self.assertEqual(result, "hola esto es un archivo")
        mock_open.assert_called_once_with("hola.py", encoding="utf-8")

    @patch('builtins.open')
    def test_read_data_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            read_data_from_file("archivo_fantasma.txt")
        
        mock_open.assert_called_once()