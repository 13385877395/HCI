# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '行为分析.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# sys.path.append('样式/')
# sys.path.append('../样式/')

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1000, 799)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 430, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 70, 91, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 70, 113, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 71, 21))
        self.label_10.setObjectName("label_10")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_4.setGeometry(QtCore.QRect(470, 490, 411, 231))
        self.listWidget_4.setObjectName("listWidget_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 360, 111, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 320, 91, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 680, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_12.setObjectName("label_12")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 360, 91, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 390, 111, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_6.setGeometry(QtCore.QRect(110, 390, 91, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_7.setGeometry(QtCore.QRect(220, 70, 91, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_8.setGeometry(QtCore.QRect(70, 110, 31, 21))
        self.comboBox_8.setObjectName("comboBox_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 110, 113, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(110, 110, 91, 21))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(220, 110, 91, 21))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(470, 80, 411, 331))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 320, 113, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(220, 320, 91, 21))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_12.setGeometry(QtCore.QRect(220, 360, 91, 21))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_13.setGeometry(QtCore.QRect(220, 390, 91, 21))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 430, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 441, 631))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 21, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 70, 21, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 350, 21, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 350, 21, 21))
        self.pushButton_12.setObjectName("pushButton_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 40, 431, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 470, 421, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(90, 10, 72, 15))
        self.label.setObjectName("label")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.pushButton_3.raise_()
        self.comboBox_3.raise_()
        self.lineEdit_3.raise_()
        self.label_10.raise_()
        self.listWidget_4.raise_()
        self.lineEdit_4.raise_()
        self.comboBox_4.raise_()
        self.pushButton_4.raise_()
        self.label_12.raise_()
        self.comboBox_5.raise_()
        self.lineEdit_5.raise_()
        self.comboBox_6.raise_()
        self.comboBox_7.raise_()
        self.comboBox_8.raise_()
        self.lineEdit_8.raise_()
        self.comboBox_9.raise_()
        self.comboBox_10.raise_()
        self.textBrowser_4.raise_()
        self.lineEdit_9.raise_()
        self.comboBox_11.raise_()
        self.comboBox_12.raise_()
        self.comboBox_13.raise_()
        self.pushButton_9.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/button-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(450, 30, 41, 21))
        self.label_5.setObjectName("label_5")
        self.mdiArea = QtWidgets.QMdiArea(self.tab_4)
        self.mdiArea.setGeometry(QtCore.QRect(40, 20, 381, 231))
        self.mdiArea.setObjectName("mdiArea")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(80, 260, 321, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 30, 113, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(40, 290, 91, 21))
        self.label_24.setObjectName("label_24")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 690, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(40, 311, 381, 371))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_14.setGeometry(QtCore.QRect(500, 110, 31, 21))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_15.setGeometry(QtCore.QRect(650, 300, 91, 21))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_16 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_16.setGeometry(QtCore.QRect(650, 270, 91, 21))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_17 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_17.setGeometry(QtCore.QRect(540, 270, 91, 21))
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_18 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_18.setGeometry(QtCore.QRect(540, 300, 91, 21))
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(450, 270, 71, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(760, 300, 111, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(760, 110, 113, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(760, 70, 113, 20))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.comboBox_19 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_19.setGeometry(QtCore.QRect(540, 330, 91, 21))
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(450, 70, 71, 21))
        self.label_13.setObjectName("label_13")
        self.comboBox_20 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_20.setGeometry(QtCore.QRect(540, 110, 91, 21))
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_21 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_21.setGeometry(QtCore.QRect(540, 70, 91, 21))
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(760, 330, 111, 20))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.comboBox_22 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_22.setGeometry(QtCore.QRect(650, 330, 91, 21))
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.comboBox_23 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_23.setGeometry(QtCore.QRect(650, 70, 91, 21))
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(760, 270, 113, 20))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.comboBox_24 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_24.setGeometry(QtCore.QRect(650, 110, 91, 21))
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_24.addItem("")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(480, 430, 91, 21))
        self.label_27.setObjectName("label_27")
        self.listWidget_6 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_6.setGeometry(QtCore.QRect(480, 461, 411, 251))
        self.listWidget_6.setObjectName("listWidget_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 690, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_13.setGeometry(QtCore.QRect(470, 110, 21, 21))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(440, 110, 21, 21))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_15.setGeometry(QtCore.QRect(460, 330, 21, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_16.setGeometry(QtCore.QRect(490, 330, 21, 21))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(660, 30, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(760, 30, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/button-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon1, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 660, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_5 = QtWidgets.QListWidget(self.widget)
        self.listWidget_5.setGeometry(QtCore.QRect(410, 70, 401, 561))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(410, 40, 91, 21))
        self.label_25.setObjectName("label_25")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(30, 40, 131, 21))
        self.label_16.setObjectName("label_16")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 660, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 70, 361, 561))
        self.textBrowser.setObjectName("textBrowser")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.widget, icon2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_3.setText(_translate("Frame", "增加"))
        self.comboBox_3.setItemText(0, _translate("Frame", "goal"))
        self.label_10.setText(_translate("Frame", "结果"))
        self.comboBox_4.setItemText(0, _translate("Frame", "goal"))
        self.comboBox_4.setItemText(1, _translate("Frame", "count-order"))
        self.pushButton_4.setText(_translate("Frame", "预览"))
        self.label_12.setText(_translate("Frame", "条件"))
        self.comboBox_5.setItemText(0, _translate("Frame", "retrieve"))
        self.comboBox_6.setItemText(0, _translate("Frame", "first"))
        self.comboBox_7.setItemText(0, _translate("Frame", "IS"))
        self.comboBox_7.setItemText(1, _translate("Frame", "="))
        self.comboBox_7.setItemText(2, _translate("Frame", ">"))
        self.comboBox_7.setItemText(3, _translate("Frame", "<"))
        self.comboBox_7.setItemText(4, _translate("Frame", ">="))
        self.comboBox_7.setItemText(5, _translate("Frame", "<="))
        self.comboBox_9.setItemText(0, _translate("Frame", "start"))
        self.comboBox_10.setItemText(0, _translate("Frame", "="))
        self.textBrowser_4.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox_11.setItemText(0, _translate("Frame", "count"))
        self.comboBox_11.setItemText(1, _translate("Frame", "="))
        self.comboBox_11.setItemText(2, _translate("Frame", ">"))
        self.comboBox_11.setItemText(3, _translate("Frame", "<"))
        self.comboBox_11.setItemText(4, _translate("Frame", ">="))
        self.comboBox_11.setItemText(5, _translate("Frame", "<="))
        self.comboBox_12.setItemText(0, _translate("Frame", "IS"))
        self.comboBox_12.setItemText(1, _translate("Frame", "="))
        self.comboBox_12.setItemText(2, _translate("Frame", ">"))
        self.comboBox_12.setItemText(3, _translate("Frame", "<"))
        self.comboBox_12.setItemText(4, _translate("Frame", ">="))
        self.comboBox_12.setItemText(5, _translate("Frame", "<="))
        self.comboBox_13.setItemText(0, _translate("Frame", "="))
        self.pushButton_9.setText(_translate("Frame", "格式检查"))
        self.groupBox.setTitle(_translate("Frame", "过程知识类定义"))
        self.pushButton.setText(_translate("Frame", "+"))
        self.pushButton_8.setText(_translate("Frame", "-"))
        self.pushButton_11.setText(_translate("Frame", "-"))
        self.pushButton_12.setText(_translate("Frame", "+"))
        self.groupBox_2.setTitle(_translate("Frame", "预览结果"))
        self.groupBox_3.setTitle(_translate("Frame", "过程知识列表"))
        self.label.setText(_translate("Frame", "函数名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Frame", "手工建模"))
        self.pushButton_2.setText(_translate("Frame", "预览"))
        self.label_5.setText(_translate("Frame", "时间"))
        self.label_9.setText(_translate("Frame", "播放   暂停  停止 快进 快退   时间定位"))
        self.label_24.setText(_translate("Frame", "过程知识预览"))
        self.pushButton_5.setText(_translate("Frame", "增加"))
        self.textBrowser_5.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox_15.setItemText(0, _translate("Frame", "IS"))
        self.comboBox_15.setItemText(1, _translate("Frame", "="))
        self.comboBox_15.setItemText(2, _translate("Frame", ">"))
        self.comboBox_15.setItemText(3, _translate("Frame", "<"))
        self.comboBox_15.setItemText(4, _translate("Frame", ">="))
        self.comboBox_15.setItemText(5, _translate("Frame", "<="))
        self.comboBox_16.setItemText(0, _translate("Frame", "count"))
        self.comboBox_16.setItemText(1, _translate("Frame", "="))
        self.comboBox_16.setItemText(2, _translate("Frame", ">"))
        self.comboBox_16.setItemText(3, _translate("Frame", "<"))
        self.comboBox_16.setItemText(4, _translate("Frame", ">="))
        self.comboBox_16.setItemText(5, _translate("Frame", "<="))
        self.comboBox_17.setItemText(0, _translate("Frame", "goal"))
        self.comboBox_17.setItemText(1, _translate("Frame", "count-order"))
        self.comboBox_18.setItemText(0, _translate("Frame", "retrieve"))
        self.label_11.setText(_translate("Frame", "结果"))
        self.comboBox_19.setItemText(0, _translate("Frame", "first"))
        self.label_13.setText(_translate("Frame", "条件"))
        self.comboBox_20.setItemText(0, _translate("Frame", "start"))
        self.comboBox_21.setItemText(0, _translate("Frame", "goal"))
        self.comboBox_22.setItemText(0, _translate("Frame", "="))
        self.comboBox_23.setItemText(0, _translate("Frame", "IS"))
        self.comboBox_23.setItemText(1, _translate("Frame", "="))
        self.comboBox_23.setItemText(2, _translate("Frame", ">"))
        self.comboBox_23.setItemText(3, _translate("Frame", "<"))
        self.comboBox_23.setItemText(4, _translate("Frame", ">="))
        self.comboBox_23.setItemText(5, _translate("Frame", "<="))
        self.comboBox_24.setItemText(0, _translate("Frame", "="))
        self.label_27.setText(_translate("Frame", "过程知识列表"))
        self.pushButton_10.setText(_translate("Frame", "格式检查"))
        self.pushButton_13.setText(_translate("Frame", "-"))
        self.pushButton_14.setText(_translate("Frame", "+"))
        self.pushButton_15.setText(_translate("Frame", "+"))
        self.pushButton_16.setText(_translate("Frame", "-"))
        self.label_2.setText(_translate("Frame", "函数名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Frame", "视频分析"))
        self.pushButton_6.setText(_translate("Frame", "格式检查"))
        self.label_25.setText(_translate("Frame", "过程知识列表"))
        self.label_16.setText(_translate("Frame", "ACT-R生成式"))
        self.pushButton_7.setText(_translate("Frame", "增加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Frame", "ACT-R生成式"))
import resources_rc
