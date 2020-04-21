import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from com.ran.bobo.main.Calculator import Ui_MainWindow
from com.ran.bobo.base import gol_var


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        gol_var._init()
        gol_var.set_value('result', '0')
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
