import sys
sys.path.append('类/')
from PyQt5 import QtWidgets

sys.path.append("动作/")
sys.path.append("ui/")
from 知识与参数g import knowForm
from 行为分析g   import actForm
from 认知建模g   import conForm
from mian import *

class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.child1 = knowForm()  # self.child = children()生成子窗口实例self.child.
        self.toolButton_1.clicked.connect(self.child1Show)  # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中

        self.child2 = actForm()
        self.toolButton_2.clicked.connect(self.child2Show)


        self.child3 = conForm()
        self.toolButton_3.clicked.connect(self.child3Show)


    def child1Show(self):
        self.child2.close()
        self.child3.close()

        self.gridLayout.addWidget(self.child1)  # 添加子窗口
        self.child1.show()

    def child2Show(self):
        self.child1.close()
        self.child3.close()

        self.gridLayout.addWidget(self.child2)  # 添加子窗口
        self.child2.show()

    def child3Show(self):
        self.child1.close()
        self.child2.close()

        self.gridLayout.addWidget(self.child3)  # 添加子窗口
        self.child3.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())