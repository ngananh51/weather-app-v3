# Form implementation generated from reading ui file 'giaodienchinh.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 535)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 110, 69, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_toa_do = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_toa_do.setGeometry(QtCore.QRect(170, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_toa_do.setFont(font)
        self.comboBox_toa_do.setObjectName("comboBox_toa_do")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.setItemText(0, "")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.comboBox_toa_do.addItem("")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 160, 311, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_location = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_location.setGeometry(QtCore.QRect(130, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_location.setFont(font)
        self.lineEdit_location.setText("")
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.lineEdit_nation = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_nation.setGeometry(QtCore.QRect(130, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_nation.setFont(font)
        self.lineEdit_nation.setText("")
        self.lineEdit_nation.setObjectName("lineEdit_nation")
        self.lineEdit_coordinates = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_coordinates.setGeometry(QtCore.QRect(130, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_coordinates.setFont(font)
        self.lineEdit_coordinates.setText("")
        self.lineEdit_coordinates.setObjectName("lineEdit_coordinates")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_wind_power = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_wind_power.setGeometry(QtCore.QRect(630, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_wind_power.setFont(font)
        self.lineEdit_wind_power.setText("")
        self.lineEdit_wind_power.setObjectName("lineEdit_wind_power")
        self.lineEdit_temperature = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_temperature.setGeometry(QtCore.QRect(630, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_temperature.setFont(font)
        self.lineEdit_temperature.setText("")
        self.lineEdit_temperature.setObjectName("lineEdit_temperature")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_humidity = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_humidity.setGeometry(QtCore.QRect(630, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_humidity.setFont(font)
        self.lineEdit_humidity.setText("")
        self.lineEdit_humidity.setObjectName("lineEdit_humidity")
        self.lineEdit_atmospheric_pressure = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_atmospheric_pressure.setGeometry(QtCore.QRect(630, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_atmospheric_pressure.setFont(font)
        self.lineEdit_atmospheric_pressure.setText("")
        self.lineEdit_atmospheric_pressure.setObjectName("lineEdit_atmospheric_pressure")
        self.lineEdit_wind_direction = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_wind_direction.setGeometry(QtCore.QRect(630, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_wind_direction.setFont(font)
        self.lineEdit_wind_direction.setText("")
        self.lineEdit_wind_direction.setObjectName("lineEdit_wind_direction")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_vision = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_vision.setGeometry(QtCore.QRect(630, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_vision.setFont(font)
        self.lineEdit_vision.setText("")
        self.lineEdit_vision.setObjectName("lineEdit_vision")
        self.lineEdit_cloud_ratio = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_cloud_ratio.setGeometry(QtCore.QRect(630, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_cloud_ratio.setFont(font)
        self.lineEdit_cloud_ratio.setText("")
        self.lineEdit_cloud_ratio.setObjectName("lineEdit_cloud_ratio")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(770, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(770, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(770, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(770, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(770, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(770, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInfo = QtWidgets.QMenu(parent=self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtGui.QAction(parent=MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionProduct = QtGui.QAction(parent=MainWindow)
        self.actionProduct.setObjectName("actionProduct")
        self.actionAuthor = QtGui.QAction(parent=MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionProduct)
        self.menuInfo.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tọa độ:"))
        self.comboBox_toa_do.setItemText(1, _translate("MainWindow", "Hanoi"))
        self.comboBox_toa_do.setItemText(2, _translate("MainWindow", "Tokyo"))
        self.comboBox_toa_do.setItemText(3, _translate("MainWindow", "Berlin"))
        self.comboBox_toa_do.setItemText(4, _translate("MainWindow", "London"))
        self.comboBox_toa_do.setItemText(5, _translate("MainWindow", "Paris"))
        self.comboBox_toa_do.setItemText(6, _translate("MainWindow", "Ottawa"))
        self.comboBox_toa_do.setItemText(7, _translate("MainWindow", "Seoul"))
        self.comboBox_toa_do.setItemText(8, _translate("MainWindow", "Washington, D.C."))
        self.comboBox_toa_do.setItemText(9, _translate("MainWindow", "Bắc Kinh"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin địa điểm:"))
        self.label_2.setText(_translate("MainWindow", "Địa điểm:"))
        self.label_3.setText(_translate("MainWindow", "Quốc gia:"))
        self.label_4.setText(_translate("MainWindow", "Tọa độ:"))
        self.label_5.setText(_translate("MainWindow", "Thời tiết hôm nay:"))
        self.label_6.setText(_translate("MainWindow", "Nhiệt độ:"))
        self.label_8.setText(_translate("MainWindow", "Hướng gió:"))
        self.label_9.setText(_translate("MainWindow", "Sức gió:"))
        self.label_10.setText(_translate("MainWindow", "Áp suất khí quyển:"))
        self.label_11.setText(_translate("MainWindow", "Độ ẩm:"))
        self.label_12.setText(_translate("MainWindow", "Tầm nhìn:"))
        self.label_13.setText(_translate("MainWindow", "Tỉ lệ mây:"))
        self.label_14.setText(_translate("MainWindow", "m/s"))
        self.label_15.setText(_translate("MainWindow", "độ C"))
        self.label_16.setText(_translate("MainWindow", "%"))
        self.label_17.setText(_translate("MainWindow", "%"))
        self.label_18.setText(_translate("MainWindow", "%"))
        self.label_19.setText(_translate("MainWindow", "km"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionProduct.setText(_translate("MainWindow", "Product"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
