# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '知识与参数.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(960, 780)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(900, 780))
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Frame)
        self.tabWidget.setObjectName("tabWidget")
        self.system = QtWidgets.QWidget()
        self.system.setObjectName("system")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.system)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sys_add = QtWidgets.QPushButton(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_add.sizePolicy().hasHeightForWidth())
        self.sys_add.setSizePolicy(sizePolicy)
        self.sys_add.setObjectName("sys_add")
        self.gridLayout_4.addWidget(self.sys_add, 1, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sys_lable_model = QtWidgets.QLabel(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_lable_model.sizePolicy().hasHeightForWidth())
        self.sys_lable_model.setSizePolicy(sizePolicy)
        self.sys_lable_model.setObjectName("sys_lable_model")
        self.verticalLayout.addWidget(self.sys_lable_model)
        self.sys_textBrowser = QtWidgets.QTextBrowser(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_textBrowser.sizePolicy().hasHeightForWidth())
        self.sys_textBrowser.setSizePolicy(sizePolicy)
        self.sys_textBrowser.setObjectName("sys_textBrowser")
        self.verticalLayout.addWidget(self.sys_textBrowser)
        self.gridLayout_4.addLayout(self.verticalLayout, 7, 0, 2, 6)
        self.sys_comboBox_name = QtWidgets.QComboBox(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_comboBox_name.sizePolicy().hasHeightForWidth())
        self.sys_comboBox_name.setSizePolicy(sizePolicy)
        self.sys_comboBox_name.setObjectName("sys_comboBox_name")
        self.sys_comboBox_name.addItem("")
        self.sys_comboBox_name.addItem("")
        self.sys_comboBox_name.addItem("")
        self.gridLayout_4.addWidget(self.sys_comboBox_name, 0, 1, 1, 1)
        self.sys_lineEdit_value = QtWidgets.QLineEdit(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_lineEdit_value.sizePolicy().hasHeightForWidth())
        self.sys_lineEdit_value.setSizePolicy(sizePolicy)
        self.sys_lineEdit_value.setObjectName("sys_lineEdit_value")
        self.gridLayout_4.addWidget(self.sys_lineEdit_value, 0, 3, 1, 1)
        self.sys_lable_value = QtWidgets.QLabel(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_lable_value.sizePolicy().hasHeightForWidth())
        self.sys_lable_value.setSizePolicy(sizePolicy)
        self.sys_lable_value.setObjectName("sys_lable_value")
        self.gridLayout_4.addWidget(self.sys_lable_value, 0, 2, 1, 1)
        self.sys_lable_name = QtWidgets.QLabel(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_lable_name.sizePolicy().hasHeightForWidth())
        self.sys_lable_name.setSizePolicy(sizePolicy)
        self.sys_lable_name.setObjectName("sys_lable_name")
        self.gridLayout_4.addWidget(self.sys_lable_name, 0, 0, 1, 1)
        self.sys_all = QtWidgets.QListWidget(self.system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sys_all.sizePolicy().hasHeightForWidth())
        self.sys_all.setSizePolicy(sizePolicy)
        self.sys_all.setObjectName("sys_all")
        self.gridLayout_4.addWidget(self.sys_all, 0, 4, 4, 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.system, icon, "")
        self.model = QtWidgets.QWidget()
        self.model.setObjectName("model")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.model)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.model_lineEdit_default = QtWidgets.QLineEdit(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_lineEdit_default.sizePolicy().hasHeightForWidth())
        self.model_lineEdit_default.setSizePolicy(sizePolicy)
        self.model_lineEdit_default.setObjectName("model_lineEdit_default")
        self.gridLayout_5.addWidget(self.model_lineEdit_default, 1, 3, 1, 1)
        self.model_comboBox_type = QtWidgets.QComboBox(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_comboBox_type.sizePolicy().hasHeightForWidth())
        self.model_comboBox_type.setSizePolicy(sizePolicy)
        self.model_comboBox_type.setObjectName("model_comboBox_type")
        self.model_comboBox_type.addItem("")
        self.model_comboBox_type.addItem("")
        self.model_comboBox_type.addItem("")
        self.gridLayout_5.addWidget(self.model_comboBox_type, 0, 3, 1, 1)
        self.model_name = QtWidgets.QLabel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_name.sizePolicy().hasHeightForWidth())
        self.model_name.setSizePolicy(sizePolicy)
        self.model_name.setObjectName("model_name")
        self.gridLayout_5.addWidget(self.model_name, 0, 0, 1, 1)
        self.model_label_default = QtWidgets.QLabel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label_default.sizePolicy().hasHeightForWidth())
        self.model_label_default.setSizePolicy(sizePolicy)
        self.model_label_default.setObjectName("model_label_default")
        self.gridLayout_5.addWidget(self.model_label_default, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.model_label_model = QtWidgets.QLabel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label_model.sizePolicy().hasHeightForWidth())
        self.model_label_model.setSizePolicy(sizePolicy)
        self.model_label_model.setObjectName("model_label_model")
        self.verticalLayout_2.addWidget(self.model_label_model)
        self.model_textBrowser = QtWidgets.QTextBrowser(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_textBrowser.sizePolicy().hasHeightForWidth())
        self.model_textBrowser.setSizePolicy(sizePolicy)
        self.model_textBrowser.setObjectName("model_textBrowser")
        self.verticalLayout_2.addWidget(self.model_textBrowser)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 13, 0, 1, 6)
        self.model_label_type = QtWidgets.QLabel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label_type.sizePolicy().hasHeightForWidth())
        self.model_label_type.setSizePolicy(sizePolicy)
        self.model_label_type.setObjectName("model_label_type")
        self.gridLayout_5.addWidget(self.model_label_type, 0, 2, 1, 1)
        self.model_lineEdit_name = QtWidgets.QLineEdit(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_lineEdit_name.sizePolicy().hasHeightForWidth())
        self.model_lineEdit_name.setSizePolicy(sizePolicy)
        self.model_lineEdit_name.setObjectName("model_lineEdit_name")
        self.gridLayout_5.addWidget(self.model_lineEdit_name, 0, 1, 1, 1)
        self.model_add = QtWidgets.QPushButton(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_add.sizePolicy().hasHeightForWidth())
        self.model_add.setSizePolicy(sizePolicy)
        self.model_add.setObjectName("model_add")
        self.gridLayout_5.addWidget(self.model_add, 2, 3, 1, 1)
        self.model_all = QtWidgets.QListWidget(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_all.sizePolicy().hasHeightForWidth())
        self.model_all.setSizePolicy(sizePolicy)
        self.model_all.setObjectName("model_all")
        self.gridLayout_5.addWidget(self.model_all, 0, 4, 4, 2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/button-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.model, icon1, "")
        self.state = QtWidgets.QWidget()
        self.state.setObjectName("state")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.state)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 3)
        self.state_plus = QtWidgets.QPushButton(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_plus.sizePolicy().hasHeightForWidth())
        self.state_plus.setSizePolicy(sizePolicy)
        self.state_plus.setMaximumSize(QtCore.QSize(30, 16777215))
        self.state_plus.setSizeIncrement(QtCore.QSize(20, 0))
        self.state_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.state_plus.setObjectName("state_plus")
        self.gridLayout_3.addWidget(self.state_plus, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 5, 0, 1, 1)
        self.state_lineEdit_name = QtWidgets.QLineEdit(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_lineEdit_name.sizePolicy().hasHeightForWidth())
        self.state_lineEdit_name.setSizePolicy(sizePolicy)
        self.state_lineEdit_name.setText("")
        self.state_lineEdit_name.setObjectName("state_lineEdit_name")
        self.gridLayout_3.addWidget(self.state_lineEdit_name, 5, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.state_textBrowser = QtWidgets.QTextBrowser(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_textBrowser.sizePolicy().hasHeightForWidth())
        self.state_textBrowser.setSizePolicy(sizePolicy)
        self.state_textBrowser.setObjectName("state_textBrowser")
        self.verticalLayout_7.addWidget(self.state_textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 13, 0, 1, 12)
        self.state_lineEdit_classname = QtWidgets.QLineEdit(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_lineEdit_classname.sizePolicy().hasHeightForWidth())
        self.state_lineEdit_classname.setSizePolicy(sizePolicy)
        self.state_lineEdit_classname.setText("")
        self.state_lineEdit_classname.setObjectName("state_lineEdit_classname")
        self.gridLayout_3.addWidget(self.state_lineEdit_classname, 1, 2, 1, 1)
        self.state_minus = QtWidgets.QPushButton(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_minus.sizePolicy().hasHeightForWidth())
        self.state_minus.setSizePolicy(sizePolicy)
        self.state_minus.setMaximumSize(QtCore.QSize(30, 16777215))
        self.state_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.state_minus.setObjectName("state_minus")
        self.gridLayout_3.addWidget(self.state_minus, 8, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_slot1 = QtWidgets.QLabel(self.state)
        self.label_slot1.setObjectName("label_slot1")
        self.horizontalLayout.addWidget(self.label_slot1)
        self.comboBox_1 = QtWidgets.QComboBox(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setObjectName("comboBox_1")
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_slot2 = QtWidgets.QLabel(self.state)
        self.label_slot2.setObjectName("label_slot2")
        self.horizontalLayout_2.addWidget(self.label_slot2)
        self.comboBox_2 = QtWidgets.QComboBox(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_value1 = QtWidgets.QLabel(self.state)
        self.label_value1.setObjectName("label_value1")
        self.horizontalLayout_3.addWidget(self.label_value1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_3.addWidget(self.lineEdit_1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_value2 = QtWidgets.QLabel(self.state)
        self.label_value2.setObjectName("label_value2")
        self.horizontalLayout_4.addWidget(self.label_value2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 8, 2, 1, 3)
        self.label_18 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 5, 3, 1, 1)
        self.state_comboBox_Class = QtWidgets.QComboBox(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_comboBox_Class.sizePolicy().hasHeightForWidth())
        self.state_comboBox_Class.setSizePolicy(sizePolicy)
        self.state_comboBox_Class.setObjectName("state_comboBox_Class")
        self.gridLayout_3.addWidget(self.state_comboBox_Class, 5, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 3, 1, 1)
        self.state_comboBox_kge = QtWidgets.QComboBox(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_comboBox_kge.sizePolicy().hasHeightForWidth())
        self.state_comboBox_kge.setSizePolicy(sizePolicy)
        self.state_comboBox_kge.setObjectName("state_comboBox_kge")
        self.gridLayout_3.addWidget(self.state_comboBox_kge, 1, 4, 1, 1)
        self.state_add_class = QtWidgets.QPushButton(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_add_class.sizePolicy().hasHeightForWidth())
        self.state_add_class.setSizePolicy(sizePolicy)
        self.state_add_class.setObjectName("state_add_class")
        self.gridLayout_3.addWidget(self.state_add_class, 2, 4, 1, 1)
        self.state_all = QtWidgets.QListWidget(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_all.sizePolicy().hasHeightForWidth())
        self.state_all.setSizePolicy(sizePolicy)
        self.state_all.setObjectName("state_all")
        self.gridLayout_3.addWidget(self.state_all, 8, 6, 1, 6)
        self.state_all_class = QtWidgets.QListWidget(self.state)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_all_class.sizePolicy().hasHeightForWidth())
        self.state_all_class.setSizePolicy(sizePolicy)
        self.state_all_class.setObjectName("state_all_class")
        self.gridLayout_3.addWidget(self.state_all_class, 1, 6, 5, 6)
        self.checkBox = QtWidgets.QCheckBox(self.state)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 12, 2, 1, 1)
        self.state_add = QtWidgets.QPushButton(self.state)
        self.state_add.setObjectName("state_add")
        self.gridLayout_3.addWidget(self.state_add, 12, 4, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/button-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.state, icon2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.sys_lineEdit_value, self.model_lineEdit_name)
        Frame.setTabOrder(self.model_lineEdit_name, self.model_lineEdit_default)
        Frame.setTabOrder(self.model_lineEdit_default, self.state_lineEdit_classname)
        Frame.setTabOrder(self.state_lineEdit_classname, self.state_lineEdit_name)
        Frame.setTabOrder(self.state_lineEdit_name, self.lineEdit_1)
        Frame.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        Frame.setTabOrder(self.lineEdit_2, self.state_textBrowser)
        Frame.setTabOrder(self.state_textBrowser, self.model_comboBox_type)
        Frame.setTabOrder(self.model_comboBox_type, self.sys_comboBox_name)
        Frame.setTabOrder(self.sys_comboBox_name, self.model_add)
        Frame.setTabOrder(self.model_add, self.sys_textBrowser)
        Frame.setTabOrder(self.sys_textBrowser, self.state_plus)
        Frame.setTabOrder(self.state_plus, self.state_all)
        Frame.setTabOrder(self.state_all, self.sys_all)
        Frame.setTabOrder(self.sys_all, self.tabWidget)
        Frame.setTabOrder(self.tabWidget, self.state_minus)
        Frame.setTabOrder(self.state_minus, self.comboBox_1)
        Frame.setTabOrder(self.comboBox_1, self.comboBox_2)
        Frame.setTabOrder(self.comboBox_2, self.model_all)
        Frame.setTabOrder(self.model_all, self.model_textBrowser)
        Frame.setTabOrder(self.model_textBrowser, self.state_comboBox_Class)
        Frame.setTabOrder(self.state_comboBox_Class, self.state_comboBox_kge)
        Frame.setTabOrder(self.state_comboBox_kge, self.state_add_class)
        Frame.setTabOrder(self.state_add_class, self.sys_add)
        Frame.setTabOrder(self.sys_add, self.state_all_class)
        Frame.setTabOrder(self.state_all_class, self.checkBox)
        Frame.setTabOrder(self.checkBox, self.state_add)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.sys_add.setText(_translate("Frame", "增加"))
        self.sys_lable_model.setText(_translate("Frame", "模型预览"))
        self.sys_textBrowser.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sys_comboBox_name.setItemText(0, _translate("Frame", "esc"))
        self.sys_comboBox_name.setItemText(1, _translate("Frame", "if"))
        self.sys_comboBox_name.setItemText(2, _translate("Frame", "trace-detail"))
        self.sys_lable_value.setText(_translate("Frame", "参数值"))
        self.sys_lable_name.setText(_translate("Frame", "参数名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.system), _translate("Frame", "系统参数"))
        self.model_comboBox_type.setItemText(0, _translate("Frame", "整数"))
        self.model_comboBox_type.setItemText(1, _translate("Frame", "浮点数"))
        self.model_comboBox_type.setItemText(2, _translate("Frame", "字符串"))
        self.model_name.setText(_translate("Frame", "参数名"))
        self.model_label_default.setText(_translate("Frame", "缺省值"))
        self.model_label_model.setText(_translate("Frame", "模型参数预览"))
        self.model_textBrowser.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.model_label_type.setText(_translate("Frame", "参数类型"))
        self.model_add.setText(_translate("Frame", "增加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.model), _translate("Frame", "模型参数"))
        self.label_7.setText(_translate("Frame", "陈述知识类定义"))
        self.state_plus.setText(_translate("Frame", "+"))
        self.label_10.setText(_translate("Frame", "陈述知识定义"))
        self.label_12.setText(_translate("Frame", "知识类名称"))
        self.label_17.setText(_translate("Frame", "知识名"))
        self.label_6.setText(_translate("Frame", "陈述知识预览"))
        self.state_textBrowser.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.state_minus.setText(_translate("Frame", "-"))
        self.label_slot1.setText(_translate("Frame", "槽"))
        self.label_slot2.setText(_translate("Frame", "槽"))
        self.label_value1.setText(_translate("Frame", "值"))
        self.label_value2.setText(_translate("Frame", "值"))
        self.label_18.setText(_translate("Frame", "知识类"))
        self.label_9.setText(_translate("Frame", "知识槽"))
        self.state_add_class.setText(_translate("Frame", "增加"))
        self.checkBox.setText(_translate("Frame", "初始知识"))
        self.state_add.setText(_translate("Frame", "增加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.state), _translate("Frame", "陈述知识"))
import resources_rc
