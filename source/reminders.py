from PyQt6 import QtWidgets, QtCore
import sys
from remindersdialog import Ui_MainWindow
#import controller
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        #self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
    def on_pushButton_clicked(self):
        # Get all data from all inputs and process into a single write request in controller
        pass
 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())