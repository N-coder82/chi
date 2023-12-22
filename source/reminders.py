from ctypes.wintypes import PLCID
from PyQt6 import QtWidgets, QtCore
import sys
from remindersdialog import Ui_MainWindow
import controller
def print_dict(dct):
    return_string = ""
    for name, item in dct.items():
        return_string = return_string + f"{name}: {item}<br>"
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
        place_selected = self.place_input_box.text()
        title_selected = self.title_input_box.text()
        desc_selected = self.desc_input_box.text()
        day_repeat_selected = self.day_repeat_input_box.text()
        year_repeat_selected = self.year_repeat_input_box.text()
        repeat_bool = self.repeat_checkbox.isChecked()
        flagged_bool = self.flagged_checkbox.isChecked()
        debug_dict = {
            "date": date_selected, 
            "time": time_selected,
            "priority index": priority_selected, 
            "place": place_selected,
            "title": title_selected,
            "desc": desc_selected,
            "day repeating?": repeat_bool,
            "day repeat": day_repeat_selected,
            "year repeat": year_repeat_selected,
            "flagged?": flagged_bool
        }
        self.summary_display_box.setHtml(f"<h3>{print_dict(debug_dict)}</h3>")
        print("displayed")
 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())