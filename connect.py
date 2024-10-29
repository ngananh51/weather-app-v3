import sys
from PyQt6 import QtWidgets
from app import Ui_MainWindow  # Import giao diện từ app.py
from api import get_weather_data  # Import hàm lấy API từ api.py

class WeatherApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.API_KEY = '92c553dbdce3e66246fefaad9c9460e5'

        # Kết nối với hộp chọn toạ độ khi người dùng thay đổi thành phố
        self.comboBox_toa_do.currentIndexChanged.connect(self.update_weather_info)

        # Kết nối các menu item Reset và Exit
        self.actionReset.triggered.connect(self.reset_app)
        self.actionExit.triggered.connect(self.close_app)

    def update_weather_info(self):
        city = self.comboBox_toa_do.currentText()   # Lấy tên thành phố mà người dùng chọn
        weather_data = get_weather_data(city, self.API_KEY)    # Gọi API lấy dữ liệu thời tiết của thành phố

        # Kiểm tra xem API có trả về dữ liệu thành công không
        if weather_data:
            # Cập nhật dữ liệu vào các trường trong giao diện
            self.lineEdit_location.setText(weather_data["city"])
            self.lineEdit_temperature.setText(f"{weather_data['temperature']}")
            self.lineEdit_wind_power.setText(f"{weather_data['wind_speed']}")
            self.lineEdit_wind_direction.setText(f"{weather_data['wind_deg']}")
            self.lineEdit_atmospheric_pressure.setText(f"{weather_data['pressure']}")
            self.lineEdit_humidity.setText(f"{weather_data['humidity']}")
            self.lineEdit_vision.setText(f"{weather_data['visibility']}")
            self.lineEdit_cloud_ratio.setText(f"{weather_data['clouds']}")
            self.lineEdit_nation.setText(weather_data["country"])
            lat, lon = weather_data["coordinates"]
            self.lineEdit_coordinates.setText(f"{lat}, {lon}")
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

    def reset_app(self):    # Đặt lại tất cả các ô hiển thị về trạng thái ban đầu
        self.lineEdit_location.clear()
        self.lineEdit_temperature.clear()
        self.lineEdit_wind_power.clear()
        self.lineEdit_wind_direction.clear()
        self.lineEdit_atmospheric_pressure.clear()
        self.lineEdit_humidity.clear()
        self.lineEdit_vision.clear()
        self.lineEdit_cloud_ratio.clear()
        self.lineEdit_nation.clear()
        self.lineEdit_coordinates.clear()
        self.comboBox_toa_do.setCurrentIndex(0)  # Đặt lại về vị trí đầu tiên trong danh sách hộp Toạ độ

    def close_app(self):    # Đóng ứng dụng
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = WeatherApp()
    main_window.show()
    sys.exit(app.exec())