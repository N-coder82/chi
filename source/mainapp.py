from PyQt6 import QtWidgets, QtCore
import sys
from ui import Ui_Chi
import controller
class MainWindow(QtWidgets.QMainWindow, Ui_Chi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gpt_send_button.clicked.connect(self.on_pushButton_clicked)
        # self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        city, temp, condition = controller.weather_data("10001")
        self.weather_text_display.setHtml(f"<h3>City: {city}<br>Temp: {temp}<br>Conditions: {condition}</h3>")
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.show()
    def update_time(self):
        current_time = QtCore.QTime.currentTime()
        minutes = current_time.toString('mm')
        hours = current_time.toString('hh')
        self.hours_lcd.setProperty("value", hours)
        self.minutes_lcd.setProperty("value", minutes)
    def on_pushButton_clicked(self):
        # Add your code here to respond to the button click
        chatgptQues = self.gpt_input_box.text()
        GPTanswer = controller.chatbot(chatgptQues)
        self.gpt_text_display.setHtml(f"<h3>{GPTanswer}</h3>")
    # def on_pushButton2_clicked(self):
    #     # Add your code here to respond to the button click
    #     pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())