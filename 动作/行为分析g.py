import sys

from PyQt5.QtGui import QCursor

sys.path.append('../ui/')
sys.path.append('../类/')
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QLineEdit, QComboBox, QLabel
from test.test import *
from 行为分析 import Ui_Frame
from PyQt5 import QtWidgets
from CProcedure import proModeling, showall
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu
from functools import partial


class actForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(actForm, self).__init__()
        self.setupUi(self)
        self.names = []
        # 创建一个对象，存储多个模型函数
        self.models = proModeling()

        # 手工建模
        self.pushButton_4.clicked.connect(self.Preview1)
        self.pushButton_3.clicked.connect(self.add1)
        self.listWidget_4.itemClicked.connect(self.QLWclicked1)
        self.listWidget_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_4.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_4))
        # 视频建模
        self.pushButton_2.clicked.connect(self.Preview2)
        self.pushButton_5.clicked.connect(self.add2)
        self.listWidget_6.itemClicked.connect(self.QLWclicked2)
        self.listWidget_6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_6.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_6))
        # 生成式
        self.listWidget_5.itemClicked.connect(self.QLWclicked3)
        self.listWidget_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_5.customContextMenuRequested.connect(lambda: self.rightMenuShow(self.listWidget_5))

        # 手工建模条件 - 1
        self.mmcondition = []
        self.mmcountc = 1
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
        # self.inif(self.gridLayout_19, self.mmresult, self.mmcountr, '结果')
        # 增

        # 删


    # 获取手工建模的条件和结果
    def get1(self):
        condition = []
        condition.append(self.lineEdit.text())
        temp = []
        temp.append(self.comboBox_3.currentText())
        temp.append(self.comboBox_7.currentText())
        temp.append(self.lineEdit_3.text())
        condition.append(temp)
        temp = []
        temp.append(self.comboBox_9.currentText())
        temp.append(self.comboBox_10.currentText())
        temp.append(self.lineEdit_8.text())
        condition.append(temp)

        result = []
        temp = []
        temp.append(self.comboBox_4.currentText())
        temp.append(self.comboBox_11.currentText())
        temp.append(self.lineEdit_9.text())
        result.append(temp)
        temp = []
        temp.append(self.comboBox_5.currentText())
        temp.append(self.comboBox_12.currentText())
        temp.append(self.lineEdit_4.text())
        result.append(temp)
        temp = []
        temp.append(self.comboBox_6.currentText())
        temp.append(self.comboBox_13.currentText())
        temp.append(self.lineEdit_5.text())
        result.append(temp)
        return condition, result

    def Preview1(self):
        # print(self.get1())
        condition, result = self.get1()
        if condition[0] not in self.names:
            self.textBrowser_4.setText(self.models.makeModel(condition, result))
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("已有该函数名"))

    # 获取视频建模的条件和结果
    def get2(self):
        condition = []
        condition.append(self.lineEdit_2.text())
        try:
            condition.append(float(self.lineEdit_6.text()))
        except Exception as e:
            QMessageBox.information(self, "Information",
                                    self.tr("时间格式不正确"))
        temp = []
        temp.append(self.comboBox_21.currentText())
        temp.append(self.comboBox_23.currentText())
        temp.append(self.lineEdit_11.text())
        condition.append(temp)
        temp = []
        temp.append(self.comboBox_20.currentText())
        temp.append(self.comboBox_24.currentText())
        temp.append(self.lineEdit_10.text())
        condition.append(temp)

        result = []
        temp = []
        temp.append(self.comboBox_17.currentText())
        temp.append(self.comboBox_16.currentText())
        temp.append(self.lineEdit_13.text())
        result.append(temp)
        temp = []
        temp.append(self.comboBox_18.currentText())
        temp.append(self.comboBox_15.currentText())
        temp.append(self.lineEdit_7.text())
        result.append(temp)
        temp = []
        temp.append(self.comboBox_19.currentText())
        temp.append(self.comboBox_22.currentText())
        temp.append(self.lineEdit_12.text())
        result.append(temp)
        return condition, result

    def Preview2(self):
        # print(self.get2())
        condition, result = self.get2()
        if condition[0] not in self.names:
            # self.names.append(condition[0])
            condition.pop(1)
            self.MODELSTRING=self.models.makeModel(condition, result)
            self.textBrowser_5.setText(self.MODELSTRING)
            create_file2("d://test.lisp",self.MODELSTRING)

        else:
            QMessageBox.information(self, "Information",
                                    self.tr("已有该函数名"))

    def add1(self):
        condition, result = self.get1()
        if condition[0] not in self.models.name and condition[0] != '':
            self.models.moremodel(condition, result)
            self.listWidget_4.addItem(condition[0])
            self.listWidget_5.addItem(condition[0])
            self.listWidget_6.addItem(condition[0])
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("添加未成功"))

    def add2(self):
        condition, result = self.get2()
        if condition[0] not in self.models.name and condition[0] != '':
            self.models.moremodel(condition, result)
            self.listWidget_4.addItem(condition[0])
            self.listWidget_5.addItem(condition[0])
            self.listWidget_6.addItem(condition[0])
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("添加未成功"))

    def delmodel(self, name):
        num = self.models.name.index(name)
        self.models.time.pop(num)
        self.models.name.pop(num)
        self.models.condition.pop(num)
        self.models.result.pop(num)
        self.models.model.pop(num)
        self.models.len -= 1

    # def add(self, verticalLayout1, verticalLayout2, verticalLayout3):
    #     comboBox1 = QtWidgets.QComboBox(self.groupBox)
    #     comboBox2 = QtWidgets.QComboBox(self.groupBox)
    #     lineEdit = QtWidgets.QLineEdit(self.groupBox)
    #     # 增加控件的名称
    #     # self.comboBox_13.setObjectName("comboBox_13")
    #     verticalLayout1.addWidget(comboBox1)
    #     verticalLayout2.addWidget(comboBox2)
    #     verticalLayout3.addWidget(lineEdit)
    #
    # def delete(self, verticalLayout1, verticalLayout2, verticalLayout3):
    #     pass

    def QLWclicked1(self, item):
        # print(item.text())
        try:
            # print(self.models.name.index(item.text()))
            self.textBrowser_4.setText(self.models.model[self.models.name.index(item.text())])
        except Exception as e:
            print(e)

    def QLWclicked2(self, item):
        try:
            self.textBrowser_5.setText(self.models.model[self.models.name.index(item.text())])
        except Exception as e:
            print(e)

    def QLWclicked3(self, item):
        try:
            self.textBrowser.setText(self.models.model[self.models.name.index(item.text())])
        except Exception as e:
            print(e)

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
        self.delmodel(name)
        self.listWidget_4.takeItem(num)
        self.listWidget_6.takeItem(num)
        self.listWidget_5.takeItem(num)

    def onActionClear(self, qlw):
        pass

    def delmodel(self, name):
        num = self.models.name.index(name)
        self.models.time.pop(num)
        self.models.name.pop(num)
        self.models.condition.pop(num)
        self.models.result.pop(num)
        self.models.model.pop(num)
        self.models.len -= 1

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

    # def closeEvent(self, event):
    #     title = self.names[0] + '.txt'
    #     print(title)
    #     try:
    #         f = open(title, 'w')
    #         for i in self.models.model:
    #             f.write(i)
    #         f.close()
    #     except Exception as e:
    #         print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = actForm()
    window.show()
    sys.exit(app.exec_())
