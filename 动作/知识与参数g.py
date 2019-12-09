import sys

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication

sys.path.append('../ui/')

from ui.知识与参数 import Ui_Frame
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from test.test import *
from PyQt5.QtWidgets import QMenu
from PyQt5 import QtCore
class knowForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(knowForm, self).__init__()
        self.setupUi(self)
        # 系统参数
        self.systemFeatureDict = dict()
        self.systemFeatureList = list()
        self.sys_all.addItem('参数\t\t取值\t\t缺省值')
        self.sys_add.clicked.connect(self.butonSysAdd)

        # 系统参数右键菜单
        self.sys_all.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.sys_all.customContextMenuRequested.connect(self.rightMenuShowSYS)

        # 模型参数
        self.modelFeatureList = list()
        self.model_all.addItem('参数\t\t类型\t\t缺省值')
        self.model_add.clicked.connect(self.buttonModelAdd)

        # 模型参数右键菜单
        self.model_all.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.model_all.customContextMenuRequested.connect( self.rightMenuShowMODEL )

        # 陈述知识类参数
        self.stateCalssFeatureList = list()
        self.state_all_class.addItem('知识名\t\t知识槽\t\t...')
        self.state_add_class.clicked.connect(self.buttonStateClassAdd)

        # 陈述知识类参数右键菜单
        self.state_all_class.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.state_all_class.customContextMenuRequested.connect( self.rightMenuShowSTATACLASS )

        #陈述知识参数
        self.stateFeatureList = list()
        self.state_all.addItem('知识名\t\t知识类\t\t知识槽\t\t...')
        self.state_add.clicked.connect(self.buttonStateAdd)

        # 陈述知识参数右键菜单
        self.state_all.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.state_all.customContextMenuRequested.connect( self.rightMenuShowSTATA )

        # 陈述知识槽增减
        self.stateSolt = 2
        self.state_plus.clicked.connect(self.buttonStatePlus)
        self.state_minus.clicked.connect(self.buttonStateMinus)

    # 系统参数
    def butonSysAdd(self):
        # 获取参数
        systemName = self.sys_comboBox_name.currentText()
        systemFeature = self.sys_lineEdit_value.text()
        # 判断参数是否存在，如果存在则修改参数，如果不存在则插入参数
        if systemName not in self.systemFeatureDict:
            self.sys_all.addItem(systemName + '\t\t' + systemFeature)
        # 未改变参数
        elif self.systemFeatureDict[systemName]==systemFeature:
            pass
        # 修改参数
        else:
            # 删除
            item = self.sys_all.findItems(systemName+'\t\t'+self.systemFeatureDict[systemName],Qt.MatchExactly)[0]
            row = self.sys_all.row(item)
            self.sys_all.takeItem(row)
            self.sys_all.addItem(systemName + '\t\t' + systemFeature)
        self.systemFeatureDict[systemName] = systemFeature
        self.systemFeatureList = list(self.systemFeatureDict.items())
        # 调用函数返回预览字符串
        self.SYSTEMSTRING = getprint1(self.systemFeatureList)
        create_file1("d://test.lisp",self.SYSTEMSTRING)
        create_file2("d://test.lisp","\n")
        #在预览中加载字符串
        self.sys_textBrowser.setText(self.SYSTEMSTRING)

    # 系统参数右键菜单
    def rightMenuShowSYS(self):
        try:
            self.sys_contextMenu = QMenu()
            self.sys_delete = self.sys_contextMenu.addAction( u'删除' )
            self.sys_clear = self.sys_contextMenu.addAction( u'清除' )
            self.sys_contextMenu.popup( QCursor.pos() )  # 2菜单显示的位置
            self.sys_delete.triggered.connect(self.onActionDeleteSYS)
            self.sys_clear.triggered.connect(self.onActionClearSYS)
            self.sys_contextMenu.show()
        except Exception as e:
            print(e)

    # 系统参数右键删除
    def onActionDeleteSYS(self):
        row = self.sys_all.currentRow()
        if(row!=0):
            # 删除
            self.systemFeatureDict.pop(self.sys_all.item(row).text().split()[0])
            self.sys_all.takeItem(row)
            self.systemFeatureList = list( self.systemFeatureDict.items() )
            # 调用函数返回预览字符串
            self.SYSTEMSTRING = getprint1( self.systemFeatureList )

            # 在预览中加载字符串
            self.sys_textBrowser.setText( self.SYSTEMSTRING )

    # 系统参数右键清除
    def onActionClearSYS(self):
        self.sys_all.clear()
        self.systemFeatureDict = dict()
        self.systemFeatureList = list()
        self.sys_all.addItem( '参数\t\t取值\t\t缺省值' )

    # 模型参数
    def buttonModelAdd(self):
        # 获取参数
        modelName = self.model_lineEdit_name.text()
        modelType = self.model_comboBox_type.currentText()
        modelDefault = self.model_lineEdit_default.text()
        modelFeatureState = False
        # 判断参数是否存在，如果存在则修改参数，如果不存在则插入参数
        freeFeature = list()
        for feature in self.modelFeatureList:
            if modelName in feature:
                modelFeatureState = True
                item = self.model_all.findItems(feature[0] + '\t\t' +feature[1] + '\t\t' +feature[2], Qt.MatchExactly)[0]
                row = self.model_all.row(item)
                self.model_all.takeItem(row)
                self.model_all.addItem(modelName + '\t\t' + modelType + '\t\t' + modelDefault)
                freeFeature = feature
        if modelFeatureState:
            self.modelFeatureList.remove(freeFeature)
        else:
            self.model_all.addItem(modelName + '\t\t' + modelType + '\t\t' + modelDefault)
        self.modelFeatureList.append((modelName, modelType, modelDefault))
        self.showmodel()

    # 模型更改参数显示预览
    def showmodel(self):
        # 调用函数返回预览字符串
        self.MODELSTRING = getprint2( self.modelFeatureList )
        # 在预览中加载字符串
        self.model_textBrowser.setText( self.MODELSTRING )

        # 更改陈述知识内知识槽
        self.state_comboBox_kge.clear()
        for feature in self.modelFeatureList:
            self.state_comboBox_kge.addItem( feature[0] )
        # 更改陈述知识内槽
        self.comboBox_1.clear()
        for feature in self.modelFeatureList:
            self.comboBox_1.addItem( feature[0] )
        self.comboBox_2.clear()
        for feature in self.modelFeatureList:
            self.comboBox_2.addItem( feature[0] )
        # # 通过计数方式更改

        pass
    # 模型参数右键菜单
    def rightMenuShowMODEL(self):
        self.model_contextMenu = QMenu()
        self.model_delete = self.model_contextMenu.addAction( u'删除' )
        self.model_clear = self.model_contextMenu.addAction( u'清除' )
        self.model_contextMenu.popup( QCursor.pos() )  # 2菜单显示的位置
        self.model_delete.triggered.connect( self.onActionDeleteMODEL )
        self.model_clear.triggered.connect( self.onActionClearMODEL )
        self.model_contextMenu.show()

    # 模型参数右键删除
    def onActionDeleteMODEL(self):
        row = self.model_all.currentRow()
        if (row != 0):
            # 删除
            modelFeatureState =False
            freeFeature = None
            for feature in self.modelFeatureList:
                if self.model_all.item( row ).text().split()[0] in feature:
                    modelFeatureState = True
                    freeFeature = feature
            if modelFeatureState:
                self.modelFeatureList.remove( freeFeature )
                self.model_all.takeItem(row)
            self.showmodel()

    # 模型参数右键清除
    def onActionClearMODEL(self):
        self.model_all.clear()
        self.modelFeatureList = list()
        self.model_all.addItem('参数\t\t类型\t\t缺省值')
        self.showmodel()

    # 陈述知识类参数
    def buttonStateClassAdd(self):
        # 获取参数
        stateClssName = self.state_lineEdit_classname.text()
        stateSlot = self.state_comboBox_kge.currentText()
        StateClassFeatureState = False
        # 判断参数是否存在，如果存在则修改参数，如果不存在则插入参数
        freeFeature = list()
        for feature in self.stateCalssFeatureList:
            if stateClssName in feature:
                StateClassFeatureState = True
                item = self.state_all_class.findItems( feature[0] + '\t\t' + feature[1], Qt.MatchExactly )[0]
                row = self.state_all_class.row( item )
                self.state_all_class.takeItem( row )
                self.state_all_class.addItem( stateClssName + '\t\t' + stateSlot)
                freeFeature = feature
        if StateClassFeatureState:
            self.stateCalssFeatureList.remove(freeFeature)
        else:
            self.state_all_class.addItem( stateClssName + '\t\t' + stateSlot)
        self.stateCalssFeatureList.append((stateClssName,stateSlot))
        # 调用函数返回预览字符串

        # 在预览中加载字符串

        # 更改陈述知识内知识类
        self.state_comboBox_Class.clear()
        for feature in self.stateCalssFeatureList:
            self.state_comboBox_Class.addItem(feature[0])

    # 陈述知识类参数右键菜单
    def rightMenuShowSTATACLASS(self):
        self.state_contextMenu = QMenu()
        self.state_delete = self.state_contextMenu.addAction( u'删除' )
        self.state_clear = self.state_contextMenu.addAction( u'清除' )
        self.state_contextMenu.popup( QCursor.pos() )  # 2菜单显示的位置
        self.state_delete.triggered.connect( self.onActionDeleteSTATECLASS )
        self.state_clear.triggered.connect( self.onActionClearSTATECLASS )
        self.state_contextMenu.show()

    # 陈述知识类参数右键删除
    def onActionDeleteSTATECLASS(self):
        row = self.state_all_class.currentRow()
        if (row != 0):
            # 删除
            stateFeatureState = False
            freeFeature = None
            for feature in self.stateCalssFeatureList:
                if self.state_all_class.item( row ).text().split()[0] in feature:
                    stateFeatureState = True
                    freeFeature = feature
            if stateFeatureState:
                self.stateCalssFeatureList.remove( freeFeature )
                self.state_all_class.takeItem(row)
        # 更改陈述知识内知识类
        self.state_comboBox_Class.clear()
        for feature in self.stateCalssFeatureList:
            self.state_comboBox_Class.addItem( feature[0] )


    # 陈述知识类参数右键清除
    def onActionClearSTATECLASS(self):
        self.state_all_class.clear()
        self.stateCalssFeatureList = list()
        self.state_all_class.addItem('知识名\t\t知识槽\t\t...')
        # 更改陈述知识内知识类
        self.state_comboBox_Class.clear()
        for feature in self.stateCalssFeatureList:
            self.state_comboBox_Class.addItem( feature[0] )

    # 陈述知识参数
    def buttonStateAdd(self):
        # 获取参数
        stateName = self.state_lineEdit_name.text()
        stateClassName = self.state_comboBox_Class.currentText()

    # 陈述知识参数右键菜单
    def rightMenuShowSTATA(self):
        self.state_contextMenu = QMenu()
        self.state_delete = self.state_contextMenu.addAction( u'删除' )
        self.state_clear = self.state_contextMenu.addAction( u'清除' )
        self.state_contextMenu.popup( QCursor.pos() )  # 2菜单显示的位置
        self.state_delete.triggered.connect( self.onActionDeleteSTATE )
        self.state_clear.triggered.connect( self.onActionClearSTATE )
        self.state_contextMenu.show()

    # 陈述知识参数右键删除
    def onActionDeleteSTATE(self):
        row = self.state_all.currentRow()
        if (row != 0):
            # 删除
            stateFeatureState = False
            freeFeature = None
            for feature in self.stateFeatureList:
                if self.state_all.item( row ).text().split()[0] in feature:
                    stateFeatureState = True
                    freeFeature = feature
            if stateFeatureState:
                self.stateFeatureList.remove( freeFeature )
                self.state_all.takeItem( row )

    # 陈述知识参数右键清除
    def onActionClearSTATE(self):
        self.state_all.clear()
        self.stateFeatureList = list()
        self.state_all.addItem('知识名\t\t知识类\t\t知识槽\t\t...')

    # 陈述知识槽增减
    def buttonStatePlus(self):
        pass

    def buttonStateMinus(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = knowForm()
    window.show()
    sys.exit(app.exec_())