# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Chi(object):
    def setupUi(self, Chi):
        Chi.setObjectName("Chi")
        Chi.resize(1044, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Downloads/logo-09e4a95d.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Chi.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=Chi)
        self.centralwidget.setObjectName("centralwidget")
        self.reminders_display = QtWidgets.QColumnView(parent=self.centralwidget)
        self.reminders_display.setGeometry(QtCore.QRect(10, 10, 521, 381))
        self.reminders_display.setObjectName("reminders_display")
        self.gpt_input = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gpt_input.setGeometry(QtCore.QRect(620, 400, 371, 41))
        self.gpt_input.setTitle("")
        self.gpt_input.setObjectName("gpt_input")
        self.gpt_input_label = QtWidgets.QLabel(parent=self.gpt_input)
        self.gpt_input_label.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.gpt_input_label.setObjectName("gpt_input_label")
        self.gpt_input_box = QtWidgets.QLineEdit(parent=self.gpt_input)
        self.gpt_input_box.setGeometry(QtCore.QRect(70, 10, 241, 21))
        self.gpt_input_box.setObjectName("gpt_input_box")
        self.gpt_send_button = QtWidgets.QPushButton(parent=self.gpt_input)
        self.gpt_send_button.setGeometry(QtCore.QRect(320, 10, 41, 24))
        self.gpt_send_button.setObjectName("gpt_send_button")
        self.middle_divider = QtWidgets.QFrame(parent=self.centralwidget)
        self.middle_divider.setGeometry(QtCore.QRect(530, 10, 20, 431))
        self.middle_divider.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.middle_divider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.middle_divider.setObjectName("middle_divider")
        self.gpt_display_input_divider = QtWidgets.QFrame(parent=self.centralwidget)
        self.gpt_display_input_divider.setGeometry(QtCore.QRect(550, 370, 461, 31))
        self.gpt_display_input_divider.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gpt_display_input_divider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.gpt_display_input_divider.setObjectName("gpt_display_input_divider")
        self.gpt_weather_reminder = QtWidgets.QFrame(parent=self.centralwidget)
        self.gpt_weather_reminder.setGeometry(QtCore.QRect(550, 113, 481, 20))
        self.gpt_weather_reminder.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gpt_weather_reminder.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.gpt_weather_reminder.setObjectName("gpt_weather_reminder")
        self.time_weather_divider = QtWidgets.QFrame(parent=self.centralwidget)
        self.time_weather_divider.setGeometry(QtCore.QRect(780, 20, 31, 91))
        self.time_weather_divider.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.time_weather_divider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.time_weather_divider.setObjectName("time_weather_divider")
        self.gpt_text_display = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.gpt_text_display.setGeometry(QtCore.QRect(550, 130, 491, 251))
        self.gpt_text_display.setObjectName("gpt_text_display")
        self.hours_lcd = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.hours_lcd.setGeometry(QtCore.QRect(590, 20, 71, 81))
        self.hours_lcd.setDigitCount(2)
        self.hours_lcd.setProperty("value", 12.0)
        self.hours_lcd.setObjectName("hours_lcd")
        self.minutes_lcd = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.minutes_lcd.setGeometry(QtCore.QRect(680, 20, 71, 81))
        self.minutes_lcd.setDigitCount(2)
        self.minutes_lcd.setProperty("value", 45.0)
        self.minutes_lcd.setObjectName("minutes_lcd")
        self.weather_text_display = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.weather_text_display.setGeometry(QtCore.QRect(810, 30, 211, 81))
        self.weather_text_display.setObjectName("weather_text_display")
        self.create_reminder_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_reminder_button.setGeometry(QtCore.QRect(180, 400, 141, 41))
        self.create_reminder_button.setObjectName("create_reminder_button")
        Chi.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chi)
        QtCore.QMetaObject.connectSlotsByName(Chi)

    def retranslateUi(self, Chi):
        _translate = QtCore.QCoreApplication.translate
        Chi.setWindowTitle(_translate("Chi", "Chi Reminders"))
        self.gpt_input_label.setText(_translate("Chi", "ChatGPT:"))
        self.gpt_send_button.setText(_translate("Chi", "Send"))
        self.gpt_text_display.setHtml(_translate("Chi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">GPT: Hello</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">User: No</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">GPT: Yes</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">User: No</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">GPT: No</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">User: Yes</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">User: Damn it.</span></p></body></html>"))
        self.weather_text_display.setHtml(_translate("Chi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">Conditions: Sunny</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">Temp: 19 C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:12pt;\">City: San Fransisco, CA</span></p></body></html>"))
        self.create_reminder_button.setText(_translate("Chi", "Create Reminder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Chi = QtWidgets.QMainWindow()
    ui = Ui_Chi()
    ui.setupUi(Chi)
    Chi.show()
    sys.exit(app.exec())
