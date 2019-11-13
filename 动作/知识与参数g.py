import sys

from PyQt5.QtWidgets import QApplication

sys.path.append('../ui/')

from ui.知识与参数 import Ui_Frame
from PyQt5 import QtWidgets

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
        self.modelFeatureState = False
        # 判断参数是否存在，如果存在则修改参数，如果不存在则插入参数
        freeFeature = list()
        for feature in self.modelFeatureList:
            if modelName in feature:
                self.modelFeatureState = True
                item = self.model_all.findItems(feature[0] + '\t\t' +feature[1] + '\t\t' +feature[2], Qt.MatchExactly)[0]
                row = self.model_all.row(item)
                self.model_all.takeItem(row)
                self.model_all.addItem(modelName + '\t\t' + modelType + '\t\t' + modelDefault)
                freeFeature = feature
        if self.modelFeatureState:
            self.modelFeatureList.remove(freeFeature)
            self.modelFeatureList.append((modelName,modelType,modelDefault))
        else:
            self.model_all.addItem(modelName + '\t\t' + modelType + '\t\t' + modelDefault)
        self.modelFeatureList.append((modelName, modelType, modelDefault))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = knowForm()
    window.show()
    sys.exit(app.exec_())