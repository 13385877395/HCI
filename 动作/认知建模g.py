import os
import sys

import math
from PyQt5.QtCore import pyqtSignal, QTime, QThread, QEventLoop

from PyQt5.QtWidgets import QApplication, QFileDialog

from ui.认知建模 import Ui_Frame
from PyQt5 import QtWidgets
from time import time, sleep


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
        self.run_process = RunModelHandler()
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
    cogCircle = 0.5


    def __init__(self,parent=None):
        super( RunModelHandler, self ).__init__( parent )
        self.roal = 2 # 角色判断 1为声纳检测员 2为指挥官 3为武器系统(需要传参赋值)

        self.sginal = True
        self.Now = lambda: float( round( time() * 1000 ) )  # 毫秒级时间戳
        self.Declarative = []
        self.Imaginal = []
        self.Manual = []
        self.Goal = []
        self.Vision = []
        self.Speech = []
        self.Auditory = []
        self. N = [self.Declarative, self.Imaginal, self.Manual, self.Goal, self.Vision, self.Speech, self.Auditory]
        self.Weight = [1.0, 5.0, 1.0, 1.2, 1.8, 2.0, 2.0]
        self.totalActiveTime = 0
        self.totalWorkload = 0
        self.Td = 0.0
        self.Ti = 0.0
        self.Tm = 0.0
        self.Tg = 0.0
        self.Tv = 0.0
        self.Ts = 0.0
        self.Ta = 0.0
        self.Wd = 0.0
        self.Wi = 0.0
        self.Wm = 0.0
        self.Wg = 0.0
        self.Wv = 0.0
        self.Ws = 0.0
        self.Wa = 0.0
        self.startTime = self.Now()

    def run(self):
        # 判断运行哪个角色
        if self.roal==1:
            self.RunModel_Sonar(QTime.currentTime())
        elif self.roal==2:
            self.RunModel_commander(QTime.currentTime())
    def RunModel_Sonar(self, now):
        self.startModel()
        self.auditoryModule( tac=100 )
        self.declarativeModule( tac=2500 )
        self.imaginalModule( tac=2500 )
        self.procedualModule( tac=100 )
        self.motorSpeechModule( tac=5000, speech='异常目标' )  # 报告异常
        self.vacancyOrWait( tac=1000 )  # 等待3秒
        self.auditoryModule( tac=100 )
        self.declarativeModule( tac=100 )
        self.imaginalModule( tac=100 )
        self.procedualModule( tac=100 )
        self.motorManualModule( tac=3000 )  # 调节仪表
        self.visionModule( tac=150 )
        self.declarativeModule( tac=150 )
        self.imaginalModule( tac=150 )
        self.procedualModule( tac=150 )
        self.motorSpeechModule( tac=5000, speech='目标方位、距离、运动方向' )  # 报告位置方向
        self.vacancyOrWait( tac=1000 )  # 等待3秒
        self.auditoryModule( tac=500 )
        self.declarativeModule( tac=1000 )
        self.visionModule( tac=150 )
        self.imaginalModule( tac=1000 )
        self.declarativeModule( tac=150 )
        self.imaginalModule( tac=150 )
        self.procedualModule( tac=150 )
        self.motorManualModule( tac=600 )  # 启动预案
        self.vacancyOrWait( tac=1000 )  # 等待20秒
        self.auditoryModule( tac=150 )
        self.declarativeModule( tac=1500 )
        self.procedualModule( tac=1500 )
        self.imaginalModule( tac=1500 )
        self.procedualModule( tac=150 )
        self.motorSpeechModule( tac=5000, speech='目标远离' )  # 报告目标远离
        self.vacancyOrWait( tac=3000 )  # 等待3秒
        self.auditoryModule( tac=150 )
        self.declarativeModule( tac=150 )
        self.imaginalModule( tac=150 )
        self.procedualModule( tac=150 )
        self.motorManualModule( tac=600 )  # 结束预案
        self.endModel()
        self.totalModelTime = self.Now() - self.startTime
        self.trigger.emit( ''  )
        self.trigger.emit( '' )
        self.trigger.emit( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        self.trigger.emit( 'Active Time' )
        self.trigger.emit( '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts, self.Ta ) )
        self.trigger.emit(
            '{0}%\t{1}%\t{2}%\t{3}%\t{4}%\t{5}%\t{6}'.format( round( 100 * self.Td / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ti / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tm / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tg / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tv / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ts / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ta / self.totalActiveTime, 1 ) ) )
        self.trigger.emit( 'Cognitive Workload' )
        self.trigger.emit(
            '{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t{6:.3f}'.format( self.Wd, self.Wi, self.Wm, self.Wg, self.Wv, self.Ws, self.Wa ) )
        self.trigger.emit(
            '{0:.2f}%\t{1:.2f}%\t{2:.2f}%\t{3:.2f}%\t{4:.2f}%\t{5:.2f}%\t{6:.2f}%'.format( 100 * self.Wd / self.totalWorkload,
                                                                                           100 * self.Wi / self.totalWorkload,
                                                                                           100 * self.Wm / self.totalWorkload,
                                                                                           100 * self.Wg / self.totalWorkload,
                                                                                           100 * self.Wv / self.totalWorkload,
                                                                                           100 * self.Ws / self.totalWorkload,
                                                                                           100 * self.Wa / self.totalWorkload ) )
        self.trigger.emit( '' )
        self.trigger.emit( 'Total Workload: {0}'.format( self.totalWorkload ) )
        self.trigger.emit( 'Total Module Active Time: {0} ms'.format( self.totalActiveTime ) )
        self.trigger.emit( 'Total Modle Run Time: {0} ms'.format( self.totalModelTime ) )
    def RunModel_commander(self,now):
        self.startModel()
        self.acceptModule( tac=100 )  # 接受声纳员信号
        self.declarativeModule( tac=2500 )  # 陈述知识
        self.imaginalModule( tac=2500 )  # 知识检索
        self.procedualModule( tac=100 )  # 知识触发
        self.motorSpeechModule( tac=5000, speech='异常目标' )  # 报告异常
        self.vacancyOrWait( tac=1000 )  # 等待3秒
        self.acceptModule( tac=100 )  # 再次查看声纳员信号
        self.declarativeModule( tac=100 )  # 陈述知识
        self.imaginalModule( tac=100 )  # 知识检索
        self.procedualModule( tac=100 )  # 知识触发
        self.motorManualModule( tac=3000 )  # 发送信息给武器系统
        self.visionModule( tac=150 )  # 得到武器系统反馈
        self.declarativeModule( tac=150 )  # 陈述知识
        self.imaginalModule( tac=150 )  # 知识检索
        self.procedualModule( tac=150 )  # 知识触发
        self.motorSpeechModule( tac=5000, speech='事件记录' )  # 基本本次事件
        self.vacancyOrWait( tac=1000 )  # 等待3
        self.endModel()
        self.totalModelTime = self.Now() - self.startTime
        self.trigger.emit( '' )
        self.trigger.emit( '' )
        self.trigger.emit( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        self.trigger.emit( 'Active Time' )
        self.trigger.emit(
            '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts,
                                                        self.Ta ) )
        self.trigger.emit(
            '{0}%\t{1}%\t{2}%\t{3}%\t{4}%\t{5}%\t{6}'.format( round( 100 * self.Td / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ti / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tm / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tg / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tv / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ts / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ta / self.totalActiveTime, 1 ) ) )
        self.trigger.emit( 'Cognitive Workload' )
        self.trigger.emit(
            '{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t{6:.3f}'.format( self.Wd, self.Wi, self.Wm, self.Wg,
                                                                                    self.Wv, self.Ws, self.Wa ) )
        self.trigger.emit(
            '{0:.2f}%\t{1:.2f}%\t{2:.2f}%\t{3:.2f}%\t{4:.2f}%\t{5:.2f}%\t{6:.2f}%'.format(
                100 * self.Wd / self.totalWorkload,
                100 * self.Wi / self.totalWorkload,
                100 * self.Wm / self.totalWorkload,
                100 * self.Wg / self.totalWorkload,
                100 * self.Wv / self.totalWorkload,
                100 * self.Ws / self.totalWorkload,
                100 * self.Wa / self.totalWorkload ) )
        self.trigger.emit( '' )
        self.trigger.emit( 'Total Workload: {0}'.format( self.totalWorkload ) )
        self.trigger.emit( 'Total Module Active Time: {0} ms'.format( self.totalActiveTime ) )
        self.trigger.emit( 'Total Modle Run Time: {0} ms'.format( self.totalModelTime ) )
    def startModel(self):
        # now = datetime.now().strftime('%M:%S %f')
        self.Td = 0.0
        self.Ti = 0.0
        self.Tm = 0.0
        self.Tg = 0.0
        self.Tv = 0.0
        self.Ts = 0.0
        self.Ta = 0.0
        self.Wd = 0.0
        self.Wi = 0.0
        self.Wm = 0.0
        self.Wg = 0.0
        self.Wv = 0.0
        self.Ws = 0.0
        self.Wa = 0.0
        self.totalActiveTime = 0
        self.totalWorkload = 0
        self.startTime = self.Now()
        self.tmr = self.Now() - self.startTime  # 模型已运行时间：毫秒
        self.showInfo( self.tmr, '模型运行' )

    def endModel(self):
        self.tmr = self.Now() - self.startTime  # 模型已运行时间：毫秒
        self.showInfo( self.tmr, '模型结束' )

    def modelSetGoal(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '目标\t设置目标' )
        sleep( tac / 1000 )
        self.Tg = self.Tg + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[3] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Tg / 1000 + 1 ))
        self.Wg = self.Wg + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def auditoryModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '听觉\t听觉注意' )
        sleep( tac / 1000 )
        self.Ta = self.Ta + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[6] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Ta / 1000 + 1 ))
        self.Wa = self.Wa + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def visionModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '视觉\t视觉注意' )
        sleep( tac / 1000 )
        self.Tv = self.Tv + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[4] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Tv / 1000 + 1 ))
        self.Wv = self.Wv + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def declarativeModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '陈述\t陈述知识' )
        sleep( tac / 1000 )
        self.Td = self.Td + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[0] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Td / 1000 + 1 ))
        self.Wd = self.Wd + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def imaginalModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '过程\t知识检索' )
        sleep( tac / 1000 )
        self.Tm = self.Tm + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[2] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Tm / 1000 + 1 ))
        self.Wm = self.Wm + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def procedualModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '过程\t知识触发' )
        sleep( tac / 1000 )
        self.Ti = self.Ti + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[1] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Ti / 1000 + 1 ))
        self.Wi = self.Wi + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def motorSpeechModule(self, tac=cogCircle, speech=''):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '运动\t语言:' + speech )
        sleep( tac / 1000 )
        self.Ts = self.Ts + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[5] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Ts / 1000 + 1 ))
        self.Ws = self.Ws + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def motorManualModule(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '运动\t手工操作' )
        sleep( tac / 1000 )
        self.Ts = self.Ts + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[5] * (math.exp( tac / 1000.0 ) - 1 + math.log( self.Ts / 1000 + 1 ))
        self.Ws = self.Ws + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def vacancyOrWait(self, tac=cogCircle):
        self.tmr = self.Now() - self.startTime
        self.showInfo( self.tmr, '等待\t等待指令' )
        sleep( tac / 1000 )
        # Ts = Ts + tac
        # totalActiveTime = totalActiveTime + tac

    def acceptModule(self,tac=cogCircle):
        self.tmr = self.Now()-self.startTime
        self.showInfo(self.tmr,'信号\t信号注意')
        sleep(tac/1000)
        self.Ta = self.Ta + tac
        self.totalActiveTime = self.totalActiveTime + tac
        self.W = self.Weight[6]*(math.exp(tac/1000.0)-1+math.log(self.Ta/1000+1))
        self.Wa = self.Wa + self.W
        self.totalWorkload = self.totalWorkload + self.W

    def showInfo(self, str1, str2):
        self.trigger.emit( '{0:>15}\t{1:<30}'.format( str1, str2 ) )
        # 在指定的区域显示提示信息
        # 'Temperature:{0}(℃)    Pressure: {1}(Torr)    StartTime: {2}    Now: {3}'.format(self.TP_Data[0], self.TP_Data[1], self.starttime,str(datetime.now())[9:19])
        # datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] , time.toString(Qt.DefaultLocaleLongDate)[:-3]
        # self.cursor = self.textBrowser.textCursor()
        # self.textBrowser.moveCursor( self.cursor.End )  # 光标移到最后，这样就会自动显示出来
        # QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def on_files_open_triggered(self):
        print( "打开" )
        dialog = QFileDialog()
        # my_file_path = dialog.getOpenFileName(self, "打开文件", "/", "*.txt")
        my_file_path = QFileDialog.getOpenFileName( self.centralwidget, '选择文件', '', 'Excel files(*.txt , *.mds)' )
        print( my_file_path )
        f = open( my_file_path[0], "r", encoding="utf-8" )
        j = 1
        for line in f:
            print( type( line ) )
            # str1=line.strip('\n').split(',')
            self.trigger.emit( '{0} {1}'.format( j, line ) )
            j = j + 1
        # my_data = f.read()
        f.close()
        # self.trigger.emit(my_data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = conForm()
    window.show()
    sys.exit(app.exec_())