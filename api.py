import requests

# Hàm lấy dữ liệu thời tiết từ OpenWeatherMap API
def get_weather_data(city_name, api_key):
   """Lấy dữ liệu thời tiết từ OpenWeatherMap API."""
   base_url = "http://api.openweathermap.org/data/2.5/weather"
   params = {
       'q': city_name,
       'appid': api_key,
       'units': 'metric'  # Đơn vị nhiệt độ: Celsius
   }

   response = requests.get(base_url, params=params)
   if response.status_code == 200:
       data = response.json()
       return {
           "city": data["name"],
           "nation": data["sys"]["nation"],
           "temperature": data["main"]["temp"],
           "wind_speed": data["wind"]["speed"],
           "wind_deg": data["wind"]["deg"],
           "pressure": data["main"]["pressure"],
           "humidity": data["main"]["humidity"],
           "clouds": data["clouds"]["all"],
           "visibility": data["visibility"] / 1000,  # Convert visibility from meters to km
           "coordinates": (data["coord"]["lat"], data["coord"]["long"])
       }
   else:
       return None
