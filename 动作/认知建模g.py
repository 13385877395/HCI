import os
import sys


from gevent import thread

import ACT.actr as actr

from PyQt5.QtWidgets import QApplication
from ui.认知建模 import Ui_Frame
from PyQt5 import QtWidgets

sys.path.append('../ACT/')


class __Autonomy__( object ):
    """ 自定义变量的write方法 """

    def __init__(self,textBrowser):
        """ init """
        self._buff = ""
        self.textBrowser = textBrowser
    def write(self, out_stream):
        """ :param out_stream: :return: """
        self.textBrowser.append(out_stream)

class conForm(QtWidgets.QWidget, Ui_Frame):
    def __init__(self):
        super(conForm, self).__init__()
        self.setupUi(self)
        self.tag = 0
        # 模型预览版快
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
        try:
            self.textBrowser.clear()
            savedStdout = sys.stdout
            read = __Autonomy__(self.textBrowser)
            sys.stdout = read
            actr.load_act_r_code( r"ACT-R:tutorial;unit1;count1.lisp" )
            actr.run( 10 )
            sys.stdout = savedStdout
            # os.popen( "taskkill /f /t /im act-r.exe" )
        except Exception as e:
            print(e)



    def pause(self):
        # 停止运行模型
        try:
            self.textBrowser.clear()
            savedStdout = sys.stdout
            read = __Autonomy__(self.textBrowser)
            sys.stdout = read
            actr.stop_output()
            sys.stdout = savedStdout
        except Exception as e:
            print(e)
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