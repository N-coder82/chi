from PyQt6 import QtWidgets, QtCore
import sys
from ui import Ui_Chi
from remindersdialog import Ui_RemindersDialog
import controller


def print_dict(dct):
    return_string = ""
    for name, item in dct.items():
        return_string = return_string + f"{str(name)}: {str(item)}<br>"
    return return_string


class RemindersPopup(QtWidgets.QMainWindow, Ui_RemindersDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_button.clicked.connect(self.on_create_button_clicked)

    def on_create_button_clicked(self):
        # Get all data from all inputs and process into a single write request in controller
        date_selected = self.date_box.text()
        time_selected = self.time_box.text()
        raw_time = time_selected.split(" ")[0]
        h, m = raw_time.split(":")
        time_selected = h + "." + m
        priority_selected = self.priority_dropdown.currentText()
        place_selected = self.place_input_box.text()
        title_selected = self.title_input_box.text()
        desc_selected = self.desc_input_box.text()
        day_repeat_selected = self.day_repeat_input_box.text()
        year_repeat_selected = self.year_repeat_input_box.text()
        repeat_bool = self.repeat_checkbox.isChecked()
        flagged_bool = self.flagged_checkbox.isChecked()
        summary_dict = {
            "date": date_selected,
            "time": time_selected,
            "priority index": priority_selected,
            "place": place_selected,
            "title": title_selected,
            "desc": desc_selected,
            "day repeating?": repeat_bool,
            "day repeat": day_repeat_selected,
            "year repeat": year_repeat_selected,
            "flagged?": flagged_bool,
        }
        self.summary_display_box.setHtml(f"<h3>{print_dict(summary_dict)}</h3>")
        controller.write(
            "reminders.chi",
            title_selected,
            desc_selected,
            date_selected,
            time_selected,
            repeat_bool,
            day_repeat_selected,
            year_repeat_selected,
            place_selected,
            priority_selected,
            flagged_bool,
        )


class MainWindow(QtWidgets.QMainWindow, Ui_Chi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reminderspopup = None
        self.gpt_send_button.clicked.connect(self.on_gpt_send_clicked)
        self.create_reminder_button.clicked.connect(
            self.on_create_reminder_button_clicked
        )
        city, temp, condition = controller.weather_data("10001")
        self.weather_text_display.setHtml(
            f"<h3>City: {city}<br>Temp: {temp}<br>Conditions: {condition}</h3>"
        )
        currentreminders = ""
        linecount = 0
        with open("reminders.chi", "r") as file:
            data = file.readlines()
            for line in data:
                linecount += 1
            linecount = linecount - 2
        i = 0
        for i in range(linecount):
            current_reminders_dict = controller.read("reminders.chi", str(i + 1))
            currentreminders += print_dict(current_reminders_dict)
            currentreminders += "<br>=======================================<br>"

        self.reminders_display.setHtml(currentreminders)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.show()

    def update_time(self):
        current_time = QtCore.QTime.currentTime()
        minutes = current_time.toString("mm")
        hours = current_time.toString("hh")
        self.hours_lcd.setProperty("value", hours)
        self.minutes_lcd.setProperty("value", minutes)

    def on_gpt_send_clicked(self):
        # Add your code here to respond to the button click
        chatgptQues = self.gpt_input_box.text()
        GPTanswer = controller.chatbot(chatgptQues)
        self.gpt_text_display.setHtml(f"<h3>{GPTanswer}</h3>")

    def on_create_reminder_button_clicked(self):
        if self.reminderspopup is None:
            self.reminderspopup = RemindersPopup()
        self.reminderspopup.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
