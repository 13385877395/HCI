import sys
import ACT.actr as actr

from PyQt5.QtWidgets import QApplication



from ui.认知建模 import Ui_Frame
from PyQt5 import QtWidgets

# 重定义输出向
class __Autonomy__(object):
    """ 自定义变量的write方法 """
    def __init__(self):
        """ init """
        self._buff = ""
    def write(self, out_stream):
        """ :param out_stream: :return: """
        self._buff += out_stream

class conForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(conForm, self).__init__()
        self.setupUi(self)
        # 模型预览版快
        self.textEdit.setText("") # lisp文件内容
        self.pushButton_6.clicked.connect(self.check) # 检查lisp文件

        # 模型运行板块
        self.pushButton.clicked.connect(self.run) # 运行model
        self.pushButton_2.clicked.connect(self.pause) # 暂停model
        self.pushButton_3.clicked.connect(self.clear) # 清除运行结果
        self.pushButton_4.clicked.connect(self.restart) # 重新加载文件
    # 检测模型
    def check(self):
        pass
    def run(self):
        # 获取lisp文件地址

        # 加载运行模型并且保存运行结果
        savedStdout = sys.stdout
        read = __Autonomy__()
        sys.stdout = read
        actr.load_act_r_code( r"ACT-R:tutorial;unit1;count.lisp" )
        actr.run( 10 )
        sys.stdout = savedStdout
        self.textBrowser.setText(read._buff.__str__())

    def pause(self):
        # 停止运行模型
        actr.stop_output()

    def clear(self):
        self.textBrowser.clear()

    def restart(self):
        # 重新加载lisp文件
        self.run()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = conForm()
    window.show()
    sys.exit(app.exec_())