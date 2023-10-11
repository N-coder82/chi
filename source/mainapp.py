from PyQt6 import QtWidgets, uic
import sys
from compiledui import Ui_Chi
import shell
class MainWindow(QtWidgets.QMainWindow, Ui_Chi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        city, temp, condition = shell.weather_data("94404")
        self.textBrowser_2.setHtml(f"<h3>City: {city}<br>Temp: {temp}<br>Conditions: {condition}</h3>")
    def on_pushButton_clicked(self):
        # Add your code here to respond to the button click
        chatgptQues = self.lineEdit.text()
        GPTanswer = shell.chatbot(chatgptQues)
        self.textBrowser.setHtml(f"<h3>{GPTanswer}</h3>")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())