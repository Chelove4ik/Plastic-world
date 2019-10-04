
def main():
    from table import table
    from gui import UI_MainWindow
    from Pyqt6 import QtCore, QtGui, QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




