import sys

from PyQt5.QtWidgets import QApplication

sys.path.append('../ui/')

from ui.知识与参数 import Ui_Frame
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class knowForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(knowForm, self).__init__()
        self.setupUi(self)
        # 系统参数
        self.systemFeatureDict = dict()
        self.systemFeatureList = list()
        self.sys_all.addItem('参数\t\t取值\t\t缺省值')
        self.sys_add.clicked.connect(self.butonSysAdd)

        # 模型参数
        self.modelFeatureList = list()
        self.model_all.addItem('参数\t\t类型\t\t缺省值')
        self.model_add.clicked.connect(self.buttonModelAdd)

        #陈述知识类参数
        self.stateCalssFeatureList = list()
        self.state_all_class.addItem('知识名\t\t知识槽\t\t...')
        self.state_add_class.clicked.connect(self.buttonStateClassAdd)

        #陈述知识参数
        self.stateFeatureList = list()
        self.state_all.addItem('知识名\t\t知识类\t\t知识槽\t\t...')
        self.state_add.clicked.connect(self.buttonStateAdd)

        # 陈述知识槽增减

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

        #在预览中加载字符串
        self.sys_textBrowser.setText(self.systemFeatureList.__str__())

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
        # 调用函数返回预览字符串

        # 在预览中加载字符串
        self.model_textBrowser.setText( self.modelFeatureList.__str__())

        # 更改陈述知识内知识槽
        self.state_comboBox_kge.clear()
        for feature in self.modelFeatureList:
            self.state_comboBox_kge.addItem(feature[0])
        # 更改陈述知识内槽
        # 通过计数方式更改

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

    def buttonStateAdd(self):
        # 获取参数
        stateName = self.state_lineEdit_name.text()
        stateClassName = self.state_comboBox_Class.currentText()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = knowForm()
    window.show()
    sys.exit(app.exec_())