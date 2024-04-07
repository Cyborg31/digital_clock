import requests

def get_weather(api_key, city):
    """Fetches weather data for a specified city using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()
        
        # Extracting the data we need
        main_data = data['main']
        return main_data
    else:
        print("Error in the HTTP request")
