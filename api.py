'''
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


def display_weather_data(city_name):
    """Hiển thị dữ liệu thời tiết đã xử lý."""
    weather_data = get_weather_data(city_name)

    if weather_data:
        print(f"Thời tiết tại {weather_data['city']}:")
        print(f"Nhiệt độ: {weather_data['temperature']}°C")
        print(f"Mô tả: {weather_data['description']}")
        print(f"Độ ẩm: {weather_data['humidity']}%")
        print(f"Tốc độ gió: {weather_data['wind_speed']} m/s")
    else:
        print(f"Không thể lấy dữ liệu thời tiết cho {city_name}.")


#giao diện thử
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo giao diện
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Nhập thành phố
        self.city_label = QLabel('Enter City:')
        self.city_input = QLineEdit()

        # Hiển thị thông tin thời tiết
        self.result_label = QLabel('Weather Info will appear here')

        # Nút để lấy thông tin thời tiết
        self.search_button = QPushButton('Get Weather')
        self.search_button.clicked.connect(self.show_weather)

        # Thêm các widget vào layout
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def show_weather(self):
        city = self.city_input.text()
        api_key = '92c553dbdce3e66246fefaad9c9460e5'  # Thay bằng API key của bạn

        weather_data = get_weather_data(city, api_key)
        if weather_data:
            temp = weather_data['temperature']
            description = weather_data['description']
            weather_info = f"Temperature: {temp}°C\nDescription: {description}"
        else:
            weather_info = "City not found!"

        self.result_label.setText(weather_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
'''

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
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None


# Thử giao diện ứng dụng bằng PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo giao diện
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Nhãn và ô nhập tên thành phố
        self.city_label = QLabel('Nhập tên thành phố:')
        self.city_input = QLineEdit()

        # Nhãn để hiển thị kết quả thời tiết
        self.result_label = QLabel('Thông tin thời tiết sẽ xuất hiện tại đây')

        # Nút để lấy thông tin thời tiết
        self.search_button = QPushButton('Xem thời tiết')
        self.search_button.clicked.connect(self.show_weather)

        # Thêm các widget vào layout
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)

        # Cài đặt layout cho ứng dụng
        self.setLayout(layout)

    def show_weather(self):
        """Lấy và hiển thị thông tin thời tiết."""
        city = self.city_input.text()  # Lấy tên thành phố từ người dùng
        api_key = '92c553dbdce3e66246fefaad9c9460e5'

        weather_data = get_weather_data(city, api_key)  # Lấy dữ liệu thời tiết
        if weather_data:
            # Định dạng dữ liệu thời tiết để hiển thị
            temp = weather_data['temperature']
            description = weather_data['description']
            humidity = weather_data['humidity']
            wind_speed = weather_data['wind_speed']
            weather_info = (f"Thời tiết tại {weather_data['city']}:\n"
                            f"Nhiệt độ: {temp}°C\n"
                            f"Mô tả: {description}\n"
                            f"Độ ẩm: {humidity}%\n"
                            f"Tốc độ gió: {wind_speed} m/s")
        else:
            weather_info = "Không tìm thấy thành phố!"

        self.result_label.setText(weather_info)  # Hiển thị kết quả lên giao diện


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()  # Tạo ứng dụng thời tiết
    window.show()  # Hiển thị cửa sổ ứng dụng
    sys.exit(app.exec())
