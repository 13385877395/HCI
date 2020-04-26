import sys

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication,QPushButton,QLineEdit,QComboBox,QLabel

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
        # 预览参数
        self.SYSTEMSTRING=""
        self.SYSTEMCLASSFEATURE=""
        self.SYSTEMFEATURE=""
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
        self.stateClassFeatureList = list()
        self.state_all_class.addItem('知识名\t\t知识槽\t\t...')
        self.state_add_class.clicked.connect(self.buttonStateClassAdd)

        # 陈述知识类参数右键菜单
        self.state_all_class.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.state_all_class.customContextMenuRequested.connect( self.rightMenuShowSTATACLASS )

        #陈述知识参数
        self.stateFeatureList = list()
        self.state_all.addItem('知识名\t知识类\t\t知识槽\t...')
        self.state_add.clicked.connect(self.buttonStateAdd)

        # 陈述知识参数右键菜单
        self.state_all.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.state_all.customContextMenuRequested.connect( self.rightMenuShowSTATA )

        # 陈述知识槽增减
        self.WIDGETSLIST = []
        self.count = 0
        plus = QPushButton( '+' );
        plus.setMaximumWidth( 30 )
        minus = QPushButton( '-' );
        minus.setMaximumWidth( 30 )
        solt = QLabel('槽')
        box = QComboBox();
        box.setMaximumWidth( 100 )
        value = QLabel('值')
        Edit = QLineEdit();
        Edit.setMaximumWidth( 100 )
        plus.clicked.connect( self.buttonStatePlus )
        minus.clicked.connect( self.buttonStateMinus )
        self.WIDGETSLIST.append( plus )
        self.WIDGETSLIST.append( minus )
        self.WIDGETSLIST.append( solt )
        self.WIDGETSLIST.append( box )
        self.WIDGETSLIST.append( value )
        self.WIDGETSLIST.append( Edit )
        self.gridLayout_6.addWidget( plus, self.count, 0 )
        self.gridLayout_6.addWidget( minus, self.count, 1 )
        self.gridLayout_6.addWidget( solt, self.count, 2 )
        self.gridLayout_6.addWidget( box, self.count, 3 )
        self.gridLayout_6.addWidget( value, self.count, 4 )
        self.gridLayout_6.addWidget( Edit, self.count, 5 )
        self.count = 1
        plus = QPushButton( '+' )
        plus.setMaximumWidth( 30 )
        minus = QPushButton( '-' )
        minus.setMaximumWidth( 30 )
        solt = QLabel( '槽' )
        box = QComboBox()
        box.setMaximumWidth( 100 )
        value = QLabel( '值' )
        Edit = QLineEdit()
        Edit.setMaximumWidth( 100 )
        plus.clicked.connect( self.buttonStatePlus )
        minus.clicked.connect( self.buttonStateMinus )
        self.WIDGETSLIST.append( plus )
        self.WIDGETSLIST.append( minus )
        self.WIDGETSLIST.append( solt )
        self.WIDGETSLIST.append( box )
        self.WIDGETSLIST.append( value )
        self.WIDGETSLIST.append( Edit )
        self.gridLayout_6.addWidget( plus, self.count, 0 )
        self.gridLayout_6.addWidget( minus, self.count, 1 )
        self.gridLayout_6.addWidget( solt, self.count, 2 )
        self.gridLayout_6.addWidget( box, self.count, 3 )
        self.gridLayout_6.addWidget( value, self.count, 4 )
        self.gridLayout_6.addWidget( Edit, self.count, 5 )
        self.count = 2


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
        # 调用函数返回预览字符串
        self.SYSTEMSTRING = getprint1( self.systemFeatureList )
        # 在预览中加载字符串
        self.sys_textBrowser.setText( self.SYSTEMSTRING )

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
        self.MODELSTRING = getprint3( self.modelFeatureList )
        # 在预览中加载字符串
        self.model_textBrowser.setText( self.MODELSTRING )

        # 更改陈述知识类知识槽
        self.state_comboBox_kge.clear()
        for feature in self.modelFeatureList:
            self.state_comboBox_kge.addItem( feature[0] )
        # 更改陈述知识槽
        for  i in range(self.count):
            box = self.WIDGETSLIST[i*6+3]
            box.clear()
            for feature in self.modelFeatureList:
                box.addItem( feature[0] )
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
        #判断参数是否存在，如果存在则修改参数，如果不存在则插入参数

        StateClassFeatureState = False
        freeFeature = list()
        for feature in self.stateClassFeatureList:
            if stateClssName in feature:
                StateClassFeatureState = True
                itemStr = feature[0] + '\t' + feature[1]
                if len(feature)>2:
                    for i in feature[2:]:
                        itemStr+=' '+ i
                item = self.state_all_class.findItems( itemStr, Qt.MatchExactly )[0]
                row = self.state_all_class.row( item )
                self.state_all_class.takeItem( row )
                self.state_all_class.addItem( itemStr + ' ' + stateSlot )
                freeFeature = feature
        if StateClassFeatureState:
            self.stateClassFeatureList.remove( freeFeature )
            freeFeature.append( stateSlot )
            self.stateClassFeatureList.append( freeFeature )
        else:
            self.state_all_class.addItem( stateClssName + '\t' + stateSlot )
            self.stateClassFeatureList.append( [stateClssName, stateSlot] )
        # 调用函数返回预览字符串
        self.SYSTEMCLASSFEATURE = getprint4( self.stateClassFeatureList )

        # 在预览中加载字符串
        self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE )

        # 更改陈述知识内知识类
        self.state_comboBox_Class.clear()
        for feature in self.stateClassFeatureList:
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
            for feature in self.stateClassFeatureList:
                if self.state_all_class.item( row ).text().split()[0] in feature:
                    stateFeatureState = True
                    freeFeature = feature
            if stateFeatureState:
                self.stateClassFeatureList.remove( freeFeature )
                self.state_all_class.takeItem(row)
                # 调用函数返回预览字符串
                self.SYSTEMCLASSFEATURE = getprint4( self.stateClassFeatureList )

                # 在预览中加载字符串
                self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE )

                # 更改陈述知识内知识类
                self.state_comboBox_Class.clear()
                for feature in self.stateClassFeatureList:
                    self.state_comboBox_Class.addItem( feature[0] )



    # 陈述知识类参数右键清除
    def onActionClearSTATECLASS(self):
        self.state_all_class.clear()
        self.stateClassFeatureList = list()
        self.state_all_class.addItem('知识名\t\t知识槽\t\t...')
        # 调用函数返回预览字符串
        self.SYSTEMCLASSFEATURE = getprint4( self.stateClassFeatureList )
        # 在预览中加载字符串
        self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE )

        # 更改陈述知识内知识类
        self.state_comboBox_Class.clear()
        for feature in self.stateClassFeatureList:
            self.state_comboBox_Class.addItem( feature[0] )

    # 陈述知识参数
    def buttonStateAdd(self):
        # 获取参数
        stateName = self.state_lineEdit_name.text()
        stateClassName = self.state_comboBox_Class.currentText()
        freeFeature = list()
        StateFeatureState = False
        for feature in self.stateFeatureList:
            if stateName in feature[0]:
                StateFeatureState = True
                itemStr = feature[0] + '\t' + feature[1] + '\t'
                for featureItem in feature[2:]:
                    itemStr = itemStr + featureItem + ' '
                item = self.state_all.findItems( itemStr, Qt.MatchExactly )[0]
                row = self.state_all.row( item )
                self.state_all.takeItem( row )
                itemStr = stateName + '\t' + stateClassName + '\t'
                for i in range( self.count ):
                    box = self.WIDGETSLIST[i * 6 + 3]
                    boxText = box.currentText()
                    Edit = self.WIDGETSLIST[i * 6 + 5]
                    EditText = Edit.text()
                    itemStr = itemStr + boxText + ' ' + EditText + ' '
                self.state_all.addItem( itemStr )
                freeFeature = feature
        if StateFeatureState:
            self.stateFeatureList.remove( freeFeature )
        else:
            itemStr = stateName + '\t' + stateClassName + '\t'
            for i in range( self.count ):
                boxText = self.WIDGETSLIST[i * 6 + 3].currentText()
                EditText = self.WIDGETSLIST[i * 6 + 5].text()
                itemStr = itemStr + boxText + ' ' + EditText + ' '
            self.state_all.addItem( itemStr )
        List = list()
        List.append( stateName )
        List.append( stateClassName )
        for i in range( self.count ):
            box = self.WIDGETSLIST[i * 6 + 3]
            boxText = box.currentText()
            Edit =self.WIDGETSLIST[i * 6 + 5]
            EditText = Edit.text()
            List.append( boxText )
            List.append( EditText )
        self.stateFeatureList.append( List )
        # 调用函数返回预览字符串
        self.SYSTEMFEATURE = getprint5( self.stateFeatureList )

        # 在预览中加载字符串
        self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE + self.SYSTEMFEATURE )
        pass
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
                # 调用函数返回预览字符串
                self.SYSTEMFEATURE = getprint5( self.stateFeatureList )
                # 在预览中加载字符串
                self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE + self.SYSTEMFEATURE )


    # 陈述知识参数右键清除
    def onActionClearSTATE(self):
        self.state_all.clear()
        self.stateFeatureList = list()
        self.state_all.addItem('知识名\t\t知识类\t\t知识槽\t\t...')
        # 调用函数返回预览字符串
        self.SYSTEMFEATURE = getprint5( self.stateFeatureList )
        # 在预览中加载字符串
        self.state_textBrowser.setText( self.SYSTEMCLASSFEATURE + self.SYSTEMFEATURE )


    # 陈述知识槽增减
    def buttonStatePlus(self):
        plus = QPushButton( '+' );
        plus.setMaximumWidth( 30 )
        minus = QPushButton( '-' );
        minus.setMaximumWidth( 30 )
        solt = QLabel( '槽' )
        box = QComboBox()
        box.setMaximumWidth( 100 )
        value = QLabel( '值' )
        Edit = QLineEdit()
        Edit.setMaximumWidth( 100 )
        plus.clicked.connect( self.buttonStatePlus )
        minus.clicked.connect( self.buttonStateMinus )
        for feature in self.modelFeatureList:
            box.addItem( feature[0] )
        self.WIDGETSLIST.append( plus )
        self.WIDGETSLIST.append( minus )
        self.WIDGETSLIST.append( solt )
        self.WIDGETSLIST.append( box )
        self.WIDGETSLIST.append( value )
        self.WIDGETSLIST.append( Edit )
        self.gridLayout_6.addWidget( plus, self.count, 0 )
        self.gridLayout_6.addWidget( minus, self.count, 1 )
        self.gridLayout_6.addWidget( solt, self.count, 2 )
        self.gridLayout_6.addWidget( box, self.count, 3 )
        self.gridLayout_6.addWidget( value, self.count, 4 )
        self.gridLayout_6.addWidget( Edit, self.count, 5 )
        self.count = self.count+1

    def buttonStateMinus(self):
        print(self.count)
        if(self.count>2):
            plus = self.WIDGETSLIST[self.count * 6 - 6]
            minus = self.WIDGETSLIST[self.count * 6 - 5]
            solt = self.WIDGETSLIST[self.count * 6 - 4]
            box = self.WIDGETSLIST[self.count * 6 - 3]
            value = self.WIDGETSLIST[self.count * 6 - 2]
            Edit = self.WIDGETSLIST[self.count * 6 - 1]
            plus.deleteLater()
            minus.deleteLater()
            solt.deleteLater()
            box.deleteLater()
            value.deleteLater()
            Edit.deleteLater()
            self.WIDGETSLIST.remove(plus)
            self.WIDGETSLIST.remove( minus )
            self.WIDGETSLIST.remove( solt )
            self.WIDGETSLIST.remove( box )
            self.WIDGETSLIST.remove( value )
            self.WIDGETSLIST.remove( Edit )
            self.count = self.count - 1

    #每个操作后用于保存数据
    # def saveData(self):
    #     #获取model名称
    #     fileName = 'kown.lisp'
    #     with open( fileName, "w", encoding='utf-8' ) as f:
    #         str = '''(clear-all)\n\n(define-model count\n'''+self.SYSTEMSTRING+"\n"+self.SYSTEMCLASSFEATURE+self.SYSTEMFEATURE;
    #         f.write( str )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = knowForm()
    window.show()
    sys.exit(app.exec_())