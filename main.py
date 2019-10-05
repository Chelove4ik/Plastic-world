from gui import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
from my_parser import parser
from generation_table import generation_table
PATH = ''


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 180, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 81, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 230, 281, 51))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 141, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 300, 281, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 389, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 100, 389, 24))
        self.lineEdit_1.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(17, 370, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 57, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.downloading)


        self.label_downloading = QtWidgets.QLabel(self.centralwidget)
        self.label_downloading.setGeometry(QtCore.QRect(20, 140, 151, 71))
        self.label_downloading.setObjectName("label")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 48, 191, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.pressed.connect(self.open_path)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 98, 191, 28))
        self.pushButton_4.setText('Путь сохранения таблицы')
        self.pushButton_4.pressed.connect(self.save_path)
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Путь к исходной таблице"))
        self.lineEdit_1.setPlaceholderText(_translate("MainWindow", "Путь сохранения таблицы"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Добавить информацию"))
        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton_2.setText(_translate("MainWindow", "Создать график"))
        self.pushButton_3.setText(_translate("MainWindow", "Открыть таблицу"))

    def open_path(self):
        global PATH
        filename = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.lineEdit.setText(str(filename))
        PATH = str(filename)

    def save_path(self):
        filename = QFileDialog.getSaveFileName(self, 'Save file', '', '*.xslx')[0]
        self.lineEdit_1.setText(str(filename))

    def downloading(self):
        self.label_downloading.setText("Загрузка...")
        self.label_downloading.resize(self.label_downloading.sizeHint())
        table = parser(PATH)
        tables = [generation_table(table, table.shape[0], 30, 31, 25, table.columns[8].weekday()) for i in range(1000)]


def main():
    from Table import Table
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ##
    #  Код, пожалуйста
    ##
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
