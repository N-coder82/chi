from PyQt6 import QtWidgets, QtCore
import sys
from remindersdialog import Ui_MainWindow
import controller
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_button.clicked.connect(self.on_create_button_clicked)
    def on_create_button_clicked(self):
        # Get all data from all inputs and process into a single write request in controller
        date_selected = self.date_box.date()
        time_selected = self.time_box.time()
        priority_selected = self.priority_dropdown.currentIndex()
        print(f"Date: {date_selected} Time: {time_selected}")
        print(priority_selected)
 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())