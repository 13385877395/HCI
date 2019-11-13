import sys

from PyQt5.QtWidgets import QApplication

sys.path.append('../ui/')

from 认知建模 import Ui_Frame
from PyQt5 import QtWidgets

class conForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(conForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = conForm()
    window.show()
    sys.exit(app.exec_())