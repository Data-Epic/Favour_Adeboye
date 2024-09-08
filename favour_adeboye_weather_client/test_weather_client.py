import unittest
from unittest.mock import patch
from weather_client import kelvin_to_celsius, validate_time, get_current_weather, get_5_day_forecast

class TestWeatherClient(unittest.TestCase):
    
    def test_kelvin_to_celsius(self):
        """Test kelvin_to_celsius function for accurate conversions."""
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0.0)
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85)
    
    def test_validate_time(self):
        """Test validate_time function with valid and invalid times."""
        valid_times = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
        
        # Test valid times
        self.assertTrue(validate_time('00:00', valid_times))
        self.assertTrue(validate_time('12:00', valid_times))
        
        # Test invalid times
        self.assertFalse(validate_time('02:00', valid_times))
        self.assertFalse(validate_time('22:00', valid_times))
    
    @patch('weather_client.requests.get')
    def test_get_current_weather(self, mock_get):
        """Test get_current_weather with mocked API response."""
        # Mock API response with sample JSON data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'name': 'London',
            'main': {
                'temp': 293.15,  # 20°C
                'humidity': 60
            },
            'weather': [{
                'description': 'clear sky'
            }],
            'wind': {
                'speed': 5.5
             }
        }
       
        # Test get_current_weather with a valid city name
        get_current_weather('London', 'valid_api_key')
        mock_get.assert_called_once_with('http://api.openweathermap.org/data/2.5/weather?q=London&appid=valid_api_key')
    
    @patch('weather_client.requests.get')
    def test_get_current_weather_invalid_city(self, mock_get):
        """Test get_current_weather when the city is invalid (404 error)."""
        mock_get.return_value.status_code = 404
        
        # Test get_current_weather with an invalid city name
        with self.assertLogs(level='ERROR') as log:
            get_current_weather('InvalidCity', 'valid_api_key')
            self.assertIn("Error: City 'InvalidCity' not found", log.output[0])
    
    @patch('weather_client.requests.get')
    def test_get_5_day_forecast(self, mock_get):
        """Test get_5_day_forecast with mocked API response."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'name': 'London',
            'main': {
                'temp': 293.15,  # 20°C
                'humidity': 60
            },
            'weather': [{
                'description': 'clear sky'
            }],
            'wind': {
                'speed': 5.5
            }
        }
        
        # Test get_5_day_forecast with a valid time
        get_5_day_forecast('Paris', 'valid_api_key', '12:00')
        mock_get.assert_called_once_with('http://api.openweathermap.org/data/2.5/forecast?q=Paris&appid=valid_api_key')
    
    @patch('weather_client.requests.get')
    def test_get_5_day_forecast_invalid_city(self, mock_get):
        """Test get_5_day_forecast when the city is invalid (404 error)."""
        mock_get.return_value.status_code = 404
    
        # Test get_5_day_forcast with an invalid city name
        with self.assertLogs(level='ERROR') as log:
            get_5_day_forecast('InvalidCity', 'valid_api_key', '12:00')
            self.assertIn("Error: City 'InvalidCity' not found", log.output[0])

if __name__ == '__main__':
    unittest.main()