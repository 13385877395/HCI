import sys

from PyQt5.QtGui import QCursor

sys.path.append('../ui/')
sys.path.append('../类/')
from PyQt5.QtWidgets import QApplication, QMessageBox
from test.test import *
from 行为分析 import Ui_Frame
from PyQt5 import QtWidgets
from CProcedure import proModeling, showall
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu


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

        # 增
        self.pushButton.clicked.connect(
            lambda: self.add( self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3 ) )
        self.pushButton_12.clicked.connect(
            lambda: self.add( self.verticalLayout_4, self.verticalLayout_5, self.verticalLayout_6 ) )
        self.pushButton_14.clicked.connect(
            lambda: self.add( self.verticalLayout_9, self.verticalLayout_10, self.verticalLayout_11 ) )
        self.pushButton_15.clicked.connect(
            lambda: self.add( self.verticalLayout_12, self.verticalLayout_13, self.verticalLayout_14 ) )
        # 删
        self.pushButton_8.clicked.connect(
            lambda: self.delete( self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3 ) )
        self.pushButton_11.clicked.connect(
            lambda: self.delete( self.verticalLayout_4, self.verticalLayout_5, self.verticalLayout_6 ) )
        self.pushButton_13.clicked.connect(
            lambda: self.delete( self.verticalLayout_9, self.verticalLayout_10, self.verticalLayout_11 ) )
        self.pushButton_16.clicked.connect(
            lambda: self.delete( self.verticalLayout_12, self.verticalLayout_13, self.verticalLayout_14 ) )

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
        num = self.models.name.index( name )
        self.models.time.pop( num )
        self.models.name.pop( num )
        self.models.condition.pop( num )
        self.models.result.pop( num )
        self.models.model.pop( num )
        self.models.len -= 1

    def add(self, verticalLayout1, verticalLayout2, verticalLayout3):
        comboBox1 = QtWidgets.QComboBox( self.groupBox )
        comboBox2 = QtWidgets.QComboBox( self.groupBox )
        lineEdit = QtWidgets.QLineEdit( self.groupBox )
        # 增加控件的名称
        # self.comboBox_13.setObjectName("comboBox_13")
        verticalLayout1.addWidget( comboBox1 )
        verticalLayout2.addWidget( comboBox2 )
        verticalLayout3.addWidget( lineEdit )
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
