import requests

# API key từ OpenWeatherMap
API_KEY = '92c553dbdce3e66246fefaad9c9460e5'

def get_weather_data(city_name, api_key):
    """Lấy dữ liệu thời tiết từ OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Đơn vị nhiệt độ: Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None
