from gui import *

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
