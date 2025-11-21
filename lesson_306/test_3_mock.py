import unittest
from unittest.mock import patch, Mock
from for_mocking import APIClient

class TestAPIClient(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):

        # Створюємо макет відповіді API-ендпоінта
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'example_data'}
        # Встановлюємо макет для функції get() з бібліотеки
        mock_get.return_value = mock_response
        # Тестуємо метод get_data() з класу APIClient
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()
        # Перевіряємо, чи метод get() був викликаний з очік
        mock_get.assert_called_once_with('https://api.example.com/data')
        # Перевіряємо результат
        self.assertEqual(result, {'data': 'example_data'})
    
    
    @patch('requests.get')
    def test_get_data_fail(self, mock_get):

        # Створюємо макет відповіді API-ендпоінта
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "{'data': 'example_data'}"
        # Встановлюємо макет для функції get() з бібліотеки
        mock_get.return_value = mock_response
        # Тестуємо метод get_data() з класу APIClient
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()
        # Перевіряємо, чи метод get() був викликаний з очік
        mock_get.assert_called_once_with('https://api.example.com/data')
        # Перевіряємо результат
        self.assertEqual(result, "{'data': 'example_data'}", 
                         msg="Expect str with data"
        )

unittest.main(verbosity=2)
