import requests
from datetime import datetime, timezone

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    """
    Converts temperature from Kelvin to Celsius.
    
    Parameters:
        kelvin (float): Temperature in Kelvin.
    
    Returns:
        float: Temperature in Celsius.
    """
    return kelvin - 273.15

# Function to validate the selected time
def validate_time(selected_time, valid_times):
    """
    Validates if the selected time is within the valid times provided by OpenWeatherMap API.
    
    Parameters:
        selected_time (str): The time selected by the user.
        valid_times (list): A list of valid times in 'HH:MM' format.
    
    Returns:
        bool: True if the selected time is valid, False otherwise.
    """
    # Check if the time entered by the user is in the valid times list
    return selected_time in valid_times

# Function to fetch 5-day forecast data from OpenWeatherMap API
def get_5_day_forecast(city_name, api_key, selected_time):
    """
    Fetch 5-day weather forecast for a specific city and display weather for the selected time.
    
    Parameters:
        city_name (str): Name of the city.
        api_key (str): API key for OpenWeatherMap.
        selected_time (str): Time of day to fetch the forecast (e.g., '12:00').
    """
    try:
        # Construct the URL to make the API request for the 5-day forecast
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # If the request is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response from the API
            data = response.json()
            
            # Display the city name and the selected time for which the forecast is shown
            print(f"\n5-Day Weather Forecast for {data['city']['name']} at {selected_time}:\n")
            
            # Iterate over the list of forecasts, which contain data at 3-hour intervals
            for forecast in data['list']:
                # Convert the timestamp (in UNIX format) to a readable date and time
                timestamp = forecast['dt']
                date_time = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                time_only = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%H:%M:%S')
                
                # Filter forecasts that match the selected time
                if time_only.startswith(selected_time):
                    # Extract temperature, weather description, humidity, and wind speed
                    temp_kelvin = forecast['main']['temp']
                    temp_celsius = kelvin_to_celsius(temp_kelvin)
                    weather_description = forecast['weather'][0]['description']
                    humidity = forecast['main']['humidity']
                    wind_speed = forecast['wind']['speed']
                    
                    # Print the weather details for the matching forecast
                    print(f"Date & Time: {date_time}")
                    print(f"Temperature: {temp_celsius:.2f}°C")
                    print(f"Weather: {weather_description.capitalize()}")
                    print(f"Humidity: {humidity}%")
                    print(f"Wind Speed: {wind_speed} m/s")
                    print("-" * 40)
        
        # Handle the case where the city is not found (404 error)
        elif response.status_code == 404:
            print(f"\nError: City '{city_name}' not found. Please check the name and try again.")
        
        # Handle the case where the API key is invalid (401 error)
        elif response.status_code == 401:
            print("\nError: Invalid API key. Please check your API key and try again.")
        
        # Handle other HTTP errors
        else:
            print(f"\nError: Unable to fetch data (HTTP {response.status_code}). Please try again later.")
    
    # Handle connection errors (e.g., no internet)
    except requests.exceptions.ConnectionError:
        print("\nError: Network problem. Please check your internet connection and try again.")
    
    # Handle request timeout errors
    except requests.exceptions.Timeout:
        print("\nError: The request timed out. Please try again later.")
    
    # Handle any other request-related errors
    except requests.exceptions.RequestException as e:
        print(f"\nError: {e}")

# Function to fetch current weather data from OpenWeatherMap API
def get_current_weather(city_name, api_key):
    """
    Fetch current weather data for a specific city and display the details.
    
    Parameters:
        city_name (str): Name of the city.
        api_key (str): API key for OpenWeatherMap.
    """
    try:
        # Construct the URL to make the API request for the current weather
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # If the request is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response from the API
            data = response.json()
            
            # Extract relevant weather information
            city = data['name']
            temp_kelvin = data['main']['temp']
            temp_celsius = kelvin_to_celsius(temp_kelvin)
            weather_description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Print the current weather details
            print(f"\nCurrent Weather in {city}:")
            print(f"Temperature: {temp_celsius:.2f}°C")
            print(f"Weather: {weather_description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print("-" * 40)
        
        # Handle the case where the city is not found (404 error)
        elif response.status_code == 404:
            print(f"\nError: City '{city_name}' not found. Please check the name and try again.")
        
        # Handle the case where the API key is invalid (401 error)
        elif response.status_code == 401:
            print("\nError: Invalid API key. Please check your API key and try again.")
        
        # Handle other HTTP errors
        else:
            print(f"\nError: Unable to fetch data (HTTP {response.status_code}). Please try again later.")
    
    # Handle connection errors (e.g., no internet)
    except requests.exceptions.ConnectionError:
        print("\nError: Network problem. Please check your internet connection and try again.")
    
    # Handle request timeout errors
    except requests.exceptions.Timeout:
        print("\nError: The request timed out. Please try again later.")
    
    # Handle any other request-related errors
    except requests.exceptions.RequestException as e:
        print(f"\nError: {e}")

# Main program logic
if __name__ == "__main__":
    """
    Main program entry point. It prompts the user for city names, API key, 
    and whether they want current weather or a 5-day forecast. Then it 
    calls the appropriate function to fetch and display the weather data.
    """
    # Ask the user to input city names (comma-separated list)
    city_names = input("Enter the names of cities (separated by commas): ").split(',')
    
    # Ask the user to input their OpenWeatherMap API key
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    # Ask the user to select either the current weather or a 5-day forecast
    weather_choice = input("Would you like the 'current' weather or '5-day' forecast? (Enter 'current' or '5-day'): ").strip().lower()
    
    # If the user provides invalid input, default to 'current' weather
    if weather_choice not in ['current', '5-day']:
        print("\nInvalid input or no input provided. Defaulting to 'current' weather.")
        weather_choice = 'current'
    
    # Remove any extra spaces from the city names entered by the user
    city_names = [city.strip() for city in city_names]
    
    # Define the valid times for the 5-day forecast (3-hour intervals)
    valid_times = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    
    # If the user selects the 5-day forecast, prompt them to select a time
    selected_time = None
    if weather_choice == '5-day':
        while True:
            # Prompt the user to select a valid time for the forecast
            selected_time = input(f"Enter the time for the forecast (valid times: {', '.join(valid_times)}): ").strip()
            
            # Validate the selected time using the validate_time function
            if validate_time(selected_time, valid_times):
                break
            else:
                print(f"\nInvalid time entered. Please choose a valid time from {', '.join(valid_times)}.")
    
    # Loop through each city and fetch the appropriate weather data
    for city_name in city_names:
        print(f"\nFetching weather data for {city_name}...")
        if weather_choice == 'current':
            # Fetch and display current weather data
            get_current_weather(city_name, api_key)
        elif weather_choice == '5-day':
            # Fetch and display 5-day forecast for the selected time
            get_5_day_forecast(city_name, api_key, selected_time)