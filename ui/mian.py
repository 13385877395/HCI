# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mian.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.sideBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBar.sizePolicy().hasHeightForWidth())
        self.sideBar.setSizePolicy(sizePolicy)
        self.sideBar.setMinimumSize(QtCore.QSize(105, 0))
        self.sideBar.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(181, 181, 181, 255))")
        self.sideBar.setObjectName("sideBar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sideBar)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.sideBar)
        self.widget.setMinimumSize(QtCore.QSize(0, 1))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 1))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 4, 0, 1, 1)
        self.toolButton_1 = QtWidgets.QToolButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_1.sizePolicy().hasHeightForWidth())
        self.toolButton_1.setSizePolicy(sizePolicy)
        self.toolButton_1.setMinimumSize(QtCore.QSize(105, 90))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1.setIcon(icon)
        self.toolButton_1.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_1.setCheckable(True)
        self.toolButton_1.setChecked(False)
        self.toolButton_1.setAutoExclusive(True)
        self.toolButton_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_1.setObjectName("toolButton_1")
        self.gridLayout_2.addWidget(self.toolButton_1, 1, 0, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setMinimumSize(QtCore.QSize(105, 90))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/button-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_5.setCheckable(True)
        self.toolButton_5.setAutoExclusive(True)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_2.addWidget(self.toolButton_5, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 7, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QtCore.QSize(105, 90))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/button-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setAutoExclusive(True)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_2.addWidget(self.toolButton_3, 3, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setMinimumSize(QtCore.QSize(105, 90))
        self.toolButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/resources/button-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setAutoExclusive(True)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_2.addWidget(self.toolButton_4, 5, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.sideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(105, 90))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/resources/button-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(False)
        self.toolButton_2.setAutoExclusive(True)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_2.addWidget(self.toolButton_2, 2, 0, 1, 1)
        self.toolButton_5.raise_()
        self.toolButton_2.raise_()
        self.widget.raise_()
        self.toolButton_1.raise_()
        self.toolButton_3.raise_()
        self.toolButton_4.raise_()
        self.gridLayout_3.addWidget(self.sideBar, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sideBar.setProperty("class", _translate("MainWindow", "SideBar"))
        self.widget.setProperty("class", _translate("MainWindow", "Separator"))
        self.toolButton_1.setText(_translate("MainWindow", "知识与参数"))
        self.toolButton_5.setText(_translate("MainWindow", "绩效评价"))
        self.toolButton_3.setText(_translate("MainWindow", "认知建模"))
        self.toolButton_4.setText(_translate("MainWindow", "行为仿真"))
        self.toolButton_2.setText(_translate("MainWindow", "行为分析"))
import resources_rc
