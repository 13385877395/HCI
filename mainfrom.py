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
        # 参数传递
        # print(self.child2.mmconditon[0:])
        # print(len(self.child2.mmconditon))
        for bar in self.child2.mmconditon[1:]:
            for Feature in self.child1.modelFeatureList:
                bar[2].addItem(Feature[0])

    def child3Show(self):
        self.child1.close()
        self.child2.close()
        self.gridLayout.addWidget(self.child3)  # 添加子窗口
        self.child3.show()
        # 先判断lisp文件是否存在，再进行输出
        self.child3.textEdit.setText('''(clear-all)\n\n(define-model count\n''' + self.child1.SYSTEMSTRING + "\n\n" + self.child1.SYSTEMCLASSFEATURE + self.child1.SYSTEMFEATURE)
        # 参数传递
        self.child3.systemFeatureList = self.child1.systemFeatureList
        self.child3.modelFeatureList = self.child1.modelFeatureList
        self.child3.stateClassFeatureList = self.child1.stateClassFeatureList
        self.child3.stateClassFeatureList = self.child1.stateClassFeatureList
        self.child3.stateFeatureList = self.child1.stateFeatureList



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())