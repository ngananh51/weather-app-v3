import sys
from PyQt6 import QtWidgets
from app import Ui_MainWindow  # Import giao diện từ app.py
from api import get_weather_data  # Import hàm lấy API từ api.py

class WeatherApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.API_KEY = '92c553dbdce3e66246fefaad9c9460e5'

        # Kết nối sự kiện thay đổi thành phố trong comboBox với hàm cập nhật thời tiết
        self.comboBox_toa_do.currentIndexChanged.connect(self.update_weather_info)

    def update_weather_info(self):
        # Lấy tên thành phố mà người dùng chọn
        city = self.comboBox_toa_do.currentText()

        # Gọi API lấy dữ liệu thời tiết của thành phố
        weather_data = get_weather_data(city, self.API_KEY)

        # Kiểm tra xem API có trả về dữ liệu thành công không
        if weather_data:
            # Cập nhật dữ liệu vào các trường trong giao diện
            self.lineEdit_location.setText(weather_data["city"])
            self.lineEdit_temperature.setText(f"{weather_data['temperature']} °C")
            self.lineEdit_wind_power.setText(f"{weather_data['wind_speed']} m/s")
            self.lineEdit_wind_direction.setText(f"{weather_data['wind_deg']}°")
            self.lineEdit_atmospheric_pressure.setText(f"{weather_data['pressure']} hPa")
            self.lineEdit_humidity.setText(f"{weather_data['humidity']}%")
            self.lineEdit_vision.setText(f"{weather_data['visibility']} km")
            self.lineEdit_cloud_ratio.setText(f"{weather_data['clouds']}%")
            self.lineEdit_nation.setText(weather_data["country"])  # Hiển thị mã quốc gia
            lat, lon = weather_data["coordinates"]
            self.lineEdit_coordinates.setText(f"{lat}, {lon}")  # Hiển thị toạ độ
        else:
            # Hiển thị thông báo lỗi nếu không lấy được dữ liệu
            self.lineEdit_location.setText("Error")
            self.lineEdit_temperature.setText("N/A")
            self.lineEdit_wind_power.setText("N/A")
            self.lineEdit_wind_direction.setText("N/A")
            self.lineEdit_atmospheric_pressure.setText("N/A")
            self.lineEdit_humidity.setText("N/A")
            self.lineEdit_vision.setText("N/A")
            self.lineEdit_cloud_ratio.setText("N/A")
            self.lineEdit_nation.setText("N/A")
            self.lineEdit_coordinates.setText("N/A")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = WeatherApp()
    main_window.show()
    sys.exit(app.exec())
