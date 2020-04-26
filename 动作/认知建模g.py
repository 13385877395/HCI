
import sys
from subprocess import *
import threading

from PyQt5.QtCore import pyqtSignal, QTime, QThread, QEventLoop

from PyQt5.QtWidgets import QApplication, QFileDialog

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
        # 模型预览版快
        self.pushButton_6.clicked.connect(self.check) # 检查lisp文件

        # 模型运行板块
        self.pushButton.clicked.connect(lambda: self.RunModel( QTime.currentTime())) # 运行model
        self.pushButton_2.clicked.connect(self.pause) # 暂停model
        self.pushButton_3.clicked.connect(self.clear) # 清除运行结果
        self.pushButton_4.clicked.connect(self.restart) # 重新加载文件

        self.tag = 0
        self.model_path = None
    # 检测模型
    def check(self):
        pass
    def RunModel(self,now):
        # 获取lisp文件地址
        # 加载运行模型并且保存运行结果
        # try:
        #     self.textBrowser.clear()
        #     savedStdout = sys.stdout
        #     read = __Autonomy__(self.textBrowser)
        #     sys.stdout = read
        #     actr.load_act_r_code( r"ACT-R:tutorial;unit1;count1.lisp" )
        #     actr.run( 10 )
        #     sys.stdout = savedStdout
        #     # os.popen( "taskkill /f /t /im act-r.exe" )
        # except Exception as e:
        #     print(e)

        print( "打开" )
        # my_file_path = dialog.getOpenFileName(self, "打开文件", "/", "*.txt")
        my_file_path = QFileDialog.getOpenFileName( self, '选择文件', '', 'Excel files(*.txt , *.py)' )
        self.model_path = my_file_path[0]
        # 路径不能包含中文
        print( self.model_path )
        if self.model_path == None:
            pass
        else:
            self.run_process = RunModelHandler( self.model_path )
            self.run_process.trigger.connect( self.call_backlog )
            self.run_process.start()
    def call_backlog(self, str):
        self.textBrowser.append(str)
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor( self.cursor.End )  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿


    def pause(self):
    #     # 停止运行模型
    #     try:
    #         self.textBrowser.clear()
    #         savedStdout = sys.stdout
    #         read = __Autonomy__(self.textBrowser)
    #         sys.stdout = read
    #         actr.stop_output()
    #         sys.stdout = savedStdout
    #     except Exception as e:
    #         print(e)
    # def clear(self):
    #     self.textBrowser.clear()
        if self.run_process.isRunning():
            #QEventLoop
            loop = QEventLoop


    def restart(self):
        # 重新加载lisp文件
        self.run_process.restart()

    def clear(self):
        pass



class RunModelHandler( QThread ):
    #  通过类成员对象定义信号对象
    trigger = pyqtSignal( str )

    def __init__(self, model_path):
        super( RunModelHandler, self ).__init__()
        self.model_path = model_path
        self.Flag = True
    def run(self):
        cmd = r'python ' + self.model_path
        """"输出重定向"""
        savedStdout = sys.stdout
        sys.stdout = self
        p = Popen( cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True )
        self.thr = threading.Thread( target=self.listenTo, args=[p] )
        self.thr.start()
        sys.stdout = savedStdout

    def listenTo(self, proc):
        while self.Flag:
            savedStdout = sys.stdout
            sys.stdout = self
            srv_out = proc.stdout.readline()
            if (srv_out):
                sys.stdout.write( srv_out.decode( 'utf-8' ) )
            if (proc.poll() == 0):
                sys.stdout = savedStdout
                exit()
            sys.stdout = savedStdout



    def write(self, out_stream):
        """ :param out_stream: :return: """
        self.trigger.emit( out_stream )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = conForm()
    window.show()
    sys.exit(app.exec_())