import unittest
from unittest.mock import patch
from mockup_exercises import fetch_data_from_api
import json
from unittest.mock import Mock

class Test_fetch_data_from_api(unittest.TestCase):
    @patch('mockup_exercises.request.get')
    def test_fetch_data_from_api(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {"id": 1, "name": "test"})
        result = fetch_data_from_api("http://example.com/api")
        self.assertEqual(result, {"id": 1, "name": "test"})
        mock_get.assert_called_once_with("http://example.com/api")