import sys

from PyQt5.QtGui import QCursor

sys.path.append('../ui/')
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QLineEdit, QComboBox, QLabel, QListWidgetItem
from test.test import *
from 行为分析 import Ui_Frame
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu
from functools import partial


class actForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(actForm, self).__init__()
        self.setupUi(self)
        # 创建一个对象，存储多个模型函数
        self.models = {}
        self.tempModel = {}

        # 手工建模
        self.pushButton_4.clicked.connect(lambda: self.Preview(self.mmcondition, self.mmresult, self.lineEdit, self.textBrowser_4))
        self.pushButton_3.clicked.connect(self.add)
        self.listWidget_4.itemClicked.connect(lambda: self.QLWclicked(self.listWidget_4.currentItem(), self.textBrowser_4))
        self.listWidget_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_4.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_4))
        # self.pushButton_9.clicked.connect(self.print)
        # 视频建模
        self.pushButton_2.clicked.connect(lambda: self.Preview(self.vacondition, self.varesult, self.lineEdit_2, self.textBrowser_5))
        self.pushButton_5.clicked.connect(self.add)
        self.listWidget_6.itemClicked.connect(
            lambda: self.QLWclicked(self.listWidget_6.currentItem(), self.textBrowser_5))
        self.listWidget_6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_6.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_6))
        # 生成式
        self.listWidget_5.itemClicked.connect(lambda: self.QLWclicked(self.listWidget_5.currentItem(), self.textEdit))
        self.listWidget_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_5.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_5))

        # 手工建模条件 - 1
        self.mmcondition = []
        self.mmcountc = 1       # 行数
        # 手工建模结果 - 2
        self.mmresult = []
        self.mmcountr = 1
        # 视频分析条件 - 3
        self.vacondition = []
        self.vacountc = 1
        # 视频分析结果 -4
        self.varesult = []
        self.vacountr = 1
        # 条件结果初始化
        self.inif(self.gridLayout_18, self.mmcondition, 1)
        self.inif(self.gridLayout_19, self.mmresult, 2)
        self.inif(self.gridLayout_11, self.vacondition, 3)
        self.inif(self.gridLayout_14, self.varesult, 4)

    # 预览按钮
    def Preview(self, condition, result, name, textBrowser):
        combobox = QComboBox()
        lineEdit = QLineEdit()
        con = [name.text()]
        re = []
        for i in condition:
            temp = []
            for j in i:
                if type(j) == type(combobox):
                    temp.append(j.currentText())
                elif type(j) == type(lineEdit):
                    temp.append(j.text())
            con.append(temp)
        for i in result:
            temp = []
            for j in i:
                if type(j) == type(combobox):
                    temp.append(j.currentText())
                elif type(j) == type(lineEdit):
                    temp.append(j.text())
            re.append(temp)
        self.tempModel = {name.text(): self.modeling(con, re)}
        textBrowser.setText(self.tempModel[name.text()])

    # 模型生成
    def modeling(self, condition, result):
        model = '(p '
        model += condition[0] + '\n'
        model += '\t=' + condition[1][0] + '>' + "\n"
        model += "\t\t" + condition[1][1] + "\t\t" + condition[1][2] + "\n"
        for con in condition[2:]:
            if con[1] == 'goal' or con[1] == 'retrieval':
                model += '\t' + con[0] + con[1] + '>\n'
                model += '\t\t' + con[2] + '\t\t' + con[3]
            else:
                model += "\t\t" + con[1] + "\t\t" + con[2] + con[3] + "\n"
        model += '==>\n'
        model += '\t=' + result[0][0] + '>\n'
        model += '\t\t'+ result[0][1] + '\t\t' + result[0][2] + '\n'
        for re in result[1:]:
            if re[1] == 'goal' or re[1] == 'retrieval':
                model += '\t' + re[0] + re[1] + '>\n'
                model += '\t\t' + re[2] + '\t\t' + re[3] + '\n'
            else:
                model += "\t\t" + re[1] + "\t\t" + re[2] + re[3] + "\n"
        model += ')'
        return model

    # 增加按钮
    def add(self):
        if list(self.tempModel.keys())[0] not in list(self.models.keys()):
            self.models.update(self.tempModel)
            self.listWidget_4.addItem(list(self.tempModel.keys())[0])
            self.listWidget_5.addItem(list(self.tempModel.keys())[0])
            self.listWidget_6.addItem(list(self.tempModel.keys())[0])
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("添加未成功"))

    # 知识列表点击功能
    def QLWclicked(self, item, textBrowser):
        print(item.text())
        textBrowser.setText(self.models[item.text()])

    # 右键弹出菜单
    def rightMenuShow(self, qlw):
        try:
            self.contextMenu = QMenu()
            self.delete = self.contextMenu.addAction(u'删除')
            self.clear = self.contextMenu.addAction(u'清除')
            self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
            self.delete.triggered.connect(lambda: self.onActionDelete(qlw))
            self.clear.triggered.connect(lambda: self.onActionClear(qlw))
            self.contextMenu.show()
        except Exception as e:
            print(e)

    # 删除
    def onActionDelete(self, qlw):
        num = qlw.currentRow()
        name = qlw.currentItem().text()
        self.models.pop(name)
        self.listWidget_4.takeItem(num)
        self.listWidget_6.takeItem(num)
        self.listWidget_5.takeItem(num)

    def onActionClear(self, qlw):
        pass

    # 条件结果初始化
    def inif(self, gridLayout, list, num):
        if num == 1 or num == 3:
            Lab = QLabel('条件')
        elif num == 2 or num == 4:
            Lab = QLabel('结果')
        L = []
        box1 = QComboBox()
        box1.setMaximumWidth(100)
        box2 = QComboBox()
        box2.setMaximumWidth(100)
        Edit = QLineEdit()
        Edit.setMaximumWidth(100)
        L.append(box1)
        L.append(box2)
        L.append(Edit)
        self.cash(L)
        list.append(L)
        gridLayout.addWidget(Lab, 0, 0)
        gridLayout.addWidget(box1, 0, 3)
        gridLayout.addWidget(box2, 0, 4)
        gridLayout.addWidget(Edit, 0, 5)
        self.buttonStatePlus(gridLayout, list, num)
        self.buttonStatePlus(gridLayout, list, num)

    # 加号
    def buttonStatePlus(self, gridLayout, list, num):
        L = []
        plus = QPushButton('+')
        plus.setMaximumWidth(30)
        minus = QPushButton('-')
        minus.setMaximumWidth(30)
        box1 = QComboBox()
        box1.setMaximumWidth(100)
        box2 = QComboBox()
        box2.setMaximumWidth(100)
        box3 = QComboBox()
        box3.setMaximumWidth(100)
        Edit = QLineEdit()
        Edit.setMaximumWidth(100)
        L.append(plus)
        L.append(minus)
        L.append(box1)
        L.append(box2)
        L.append(box3)
        L.append(Edit)
        self.cash(L)
        list.append(L)
        if num == 1:
            gridLayout.addWidget(plus, self.mmcountc, 0)
            gridLayout.addWidget(minus, self.mmcountc, 1)
            gridLayout.addWidget(box1, self.mmcountc, 2)
            gridLayout.addWidget(box2, self.mmcountc, 3)
            gridLayout.addWidget(box3, self.mmcountc, 4)
            gridLayout.addWidget(Edit, self.mmcountc, 5)
            plus.clicked.connect(lambda: self.buttonStatePlus(gridLayout, list, 1))
            count = self.mmcountc
            self.mmcountc = self.mmcountc + 1
            minus.clicked.connect(lambda: self.buttonStateMinus(list, count, 1))

        elif num == 2:
            gridLayout.addWidget(plus, self.mmcountr, 0)
            gridLayout.addWidget(minus, self.mmcountr, 1)
            gridLayout.addWidget(box1, self.mmcountr, 2)
            gridLayout.addWidget(box2, self.mmcountr, 3)
            gridLayout.addWidget(box3, self.mmcountr, 4)
            gridLayout.addWidget(Edit, self.mmcountr, 5)
            plus.clicked.connect(lambda: self.buttonStatePlus(gridLayout, list, 2))
            count = self.mmcountr
            self.mmcountr = self.mmcountr + 1
            minus.clicked.connect(lambda: self.buttonStateMinus(list, count, 2))

        elif num == 3:
            gridLayout.addWidget(plus, self.vacountc, 0)
            gridLayout.addWidget(minus, self.vacountc, 1)
            gridLayout.addWidget(box1, self.vacountc, 2)
            gridLayout.addWidget(box2, self.vacountc, 3)
            gridLayout.addWidget(box3, self.vacountc, 4)
            gridLayout.addWidget(Edit, self.vacountc, 5)
            plus.clicked.connect(lambda: self.buttonStatePlus(gridLayout, list, 3))
            count = self.vacountc
            self.vacountc = self.vacountc + 1
            minus.clicked.connect(lambda: self.buttonStateMinus(list, count, 3))

        elif num == 4:
            gridLayout.addWidget(plus, self.vacountr, 0)
            gridLayout.addWidget(minus, self.vacountr, 1)
            gridLayout.addWidget(box1, self.vacountr, 2)
            gridLayout.addWidget(box2, self.vacountr, 3)
            gridLayout.addWidget(box3, self.vacountr, 4)
            gridLayout.addWidget(Edit, self.vacountr, 5)
            plus.clicked.connect(lambda: self.buttonStatePlus(gridLayout, list, 4))
            count = self.vacountr
            self.vacountr = self.vacountr + 1
            minus.clicked.connect(lambda: self.buttonStateMinus(list, count, 4))

    # 减号
    def buttonStateMinus(self, list, count, num):
        L = list[count]
        if count > 2:
            plus = L[0]
            minus = L[1]
            box1 = L[2]
            box2 = L[3]
            box3 = L[4]
            Edit = L[5]
            plus.deleteLater()
            minus.deleteLater()
            box1.deleteLater()
            box2.deleteLater()
            box3.deleteLater()
            Edit.deleteLater()
            list.remove(L)
            if num == 1:
                self.mmcountc = self.mmcountc - 1
                for n in range(count, self.mmcountc):
                    list[n][1].clicked.disconnect()
                    list[n][1].clicked.connect(partial(self.buttonStateMinus, list, n, 1))
            elif num == 2:
                self.mmcountr = self.mmcountr - 1
                for n in range(count, self.mmcountr):
                    list[n][1].clicked.disconnect()
                    list[n][1].clicked.connect(partial(self.buttonStateMinus, list, n, 2))
            elif num == 3:
                self.vacountc = self.vacountc - 1
                for n in range(count, self.vacountc):
                    list[n][1].clicked.disconnect()
                    list[n][1].clicked.connect(partial(self.buttonStateMinus, list, n, 3))
            elif num == 4:
                self.vacountr = self.vacountr - 1
                for n in range(count, self.vacountr):
                    list[n][1].clicked.disconnect()
                    list[n][1].clicked.connect(partial(self.buttonStateMinus, list, n, 4))

    #缓冲器赋值
    def cash(self, comboboxs):
        symbol = ['', '=', '+', '-', '?']
        list1 = ['', 'goal', 'retrieval']
        list2 = ['', 'isa', '=']
        if len(comboboxs) == 3:
            comboboxs[0].addItems(list1)
            comboboxs[1].addItems(list2)
        elif len(comboboxs) == 6:
            comboboxs[2].addItems(symbol)
            comboboxs[3].addItems(list1)
            comboboxs[4].addItems(list2)

    # 模型函数测试
    # def print(self):
    #     for i in self.models:
    #         print(self.models[i])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = actForm()
    window.show()
    sys.exit(app.exec_())
