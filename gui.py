from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(620, 110, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(544, 110, 81, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(660, 170, 281, 51))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 190, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 250, 141, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(660, 240, 281, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 389, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(120, 100, 389, 24))
        self.lineEdit_1.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 310, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 200, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 50, 191, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.pressed.connect(self.open_path)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 50, 191, 28))
        self.pushButton_4.setText('Путь сохранения таблицы')
        self.pushButton_4.pressed.connect(self.save_path)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IT График"))
        self.label_2.setText(_translate("MainWindow", "Сотрудник"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Даты"))
        self.label_3.setText(_translate("MainWindow", "Хочет отдыхать"))
        self.label_4.setText(_translate("MainWindow", "Приоритетные смены"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Названия смен"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Путь"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Путь Сохранения"))
        self.label.setText(_translate("MainWindow", "Путь к таблице"))
        self.pushButton.setText(_translate("MainWindow", "Добавить информацию"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать график"))
        self.pushButton_3.setText(_translate("MainWindow", "Открыть таблицу"))

    def open_path(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.lineEdit.setText(str(filename))

    def save_path(self):
        filename = QFileDialog.getSaveFileName(self, 'Save file', '', '*.xslx')[0]
        self.lineEdit_1.setText(str(filename))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
