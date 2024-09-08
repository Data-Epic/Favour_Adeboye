# Weather Data API Client

This Python application fetches and displays weather information for one or more cities using the **OpenWeatherMap** API. It allows users to select between the **current weather** or the **5-day weather forecast** at specific times.

## Features
- Fetch **current weather** for a list of cities.
- Fetch **5-day weather forecasts** with time selection for specified cities.
- Handles common errors (e.g., invalid city names, invalid API keys, network issues).
- Validates user input for forecast time (e.g., `00:00`, `03:00`, `12:00`, etc.).

## Prerequisites

1. **Python**: Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
2. **Requests Library**: This script uses the `requests` library to interact with the OpenWeatherMap API. Install it using the following command:
   ```bash
   pip install requests
   ```

## How to Obtain an OpenWeatherMap API Key

To use this script, you need an API key from OpenWeatherMap. Follow these steps to obtain your free API key:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/api).
2. Sign up for a free account if you don't already have one.
3. After signing in, navigate to the **API keys** section in your account.
4. Create a new API key or copy your existing one.

Your API key is required to authenticate requests to the OpenWeatherMap API.

## How to Run the Script

1. **Clone or download this repository** to your local machine.

2. **Open a terminal (command line)** in the directory where the script is located.

3. **Run the script** using Python:
   ```bash
   python weather_client.py
   ```

4. **Enter the required inputs** when prompted:
   - Enter the names of the cities separated by commas (e.g., `London, Paris, New York`).
   - Enter your OpenWeatherMap API key.
   - Choose between displaying the `current` weather or a `5-day` forecast.
   - If you choose the 5-day forecast, you will be prompted to enter a specific time (e.g., `12:00`, `15:00`), and the weather forecast for that time will be displayed.

### Example of Running the Script

1. Running the script:
   ```bash
   python weather_client.py
   ```

2. Sample Input/Output:
   ```bash
   Enter the names of cities (separated by commas): London, Paris
   Enter your OpenWeatherMap API key: your_api_key_here
   Would you like the 'current' weather or '5-day' forecast? (Enter 'current' or '5-day'): 5-day
   Enter the time for the forecast (valid times: 00:00, 03:00, 06:00, 09:00, 12:00, 15:00, 18:00, 21:00): 12:00

   Fetching weather data for London...

   5-Day Weather Forecast for London at 12:00:

   Date & Time: 2024-09-08 12:00:00
   Temperature: 16.55°C
   Weather: Clear sky
   Humidity: 60%
   Wind Speed: 4.5 m/s
   ----------------------------------------

   Fetching weather data for Paris...

   5-Day Weather Forecast for Paris at 12:00:

   Date & Time: 2024-09-08 12:00:00
   Temperature: 18.75°C
   Weather: Few clouds
   Humidity: 62%
   Wind Speed: 3.9 m/s
   ----------------------------------------
   ```

## Error Handling

This script handles common issues like:
- **Invalid city name**: Displays an error message if the city is not found.
- **Invalid API key**: Informs the user if the API key is invalid.
- **Network issues**: Handles cases where the user has no internet connection.
- **Request timeouts**: If the request takes too long, the user is prompted to try again later.

## Troubleshooting

- **Invalid API Key**: Ensure that you entered the correct API key obtained from OpenWeatherMap.
- **City Not Found**: Double-check the spelling of the city names.
- **No Internet Connection**: Ensure you have an active internet connection when running the script.