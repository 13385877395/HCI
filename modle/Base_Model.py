from time import time

from PyQt5.QtCore import QTime
from time import time, sleep
import math

class BaseModel():
    cogCircle = 0.5
    def __init__(self,parent=None):
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
        print("开始运行")
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
        print( ''  )
        print( '' )
        print( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        print( 'Active Time' )
        print( '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts, self.Ta ) )
        print(
            '{0}%\t{1}%\t{2}%\t{3}%\t{4}%\t{5}%\t{6}'.format( round( 100 * self.Td / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ti / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tm / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tg / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tv / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ts / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ta / self.totalActiveTime, 1 ) ) )
        print( 'Cognitive Workload' )
        print(
            '{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t{6:.3f}'.format( self.Wd, self.Wi, self.Wm, self.Wg, self.Wv, self.Ws, self.Wa ) )
        print(
            '{0:.2f}%\t{1:.2f}%\t{2:.2f}%\t{3:.2f}%\t{4:.2f}%\t{5:.2f}%\t{6:.2f}%'.format( 100 * self.Wd / self.totalWorkload,
                                                                                           100 * self.Wi / self.totalWorkload,
                                                                                           100 * self.Wm / self.totalWorkload,
                                                                                           100 * self.Wg / self.totalWorkload,
                                                                                           100 * self.Wv / self.totalWorkload,
                                                                                           100 * self.Ws / self.totalWorkload,
                                                                                           100 * self.Wa / self.totalWorkload ) )
        print( '' )
        print( 'Total Workload: {0}'.format( self.totalWorkload ) )
        print( 'Total Module Active Time: {0} ms'.format( self.totalActiveTime ) )
        print( 'Total Modle Run Time: {0} ms'.format( self.totalModelTime ) )
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
        print( '' )
        print( '' )
        print( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        print( 'Active Time' )
        print(
            '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts,
                                                        self.Ta ) )
        print(
            '{0}%\t{1}%\t{2}%\t{3}%\t{4}%\t{5}%\t{6}'.format( round( 100 * self.Td / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ti / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tm / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tg / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tv / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ts / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ta / self.totalActiveTime, 1 ) ) )
        print( 'Cognitive Workload' )
        print(
            '{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t{6:.3f}'.format( self.Wd, self.Wi, self.Wm, self.Wg,
                                                                                    self.Wv, self.Ws, self.Wa ) )
        print(
            '{0:.2f}%\t{1:.2f}%\t{2:.2f}%\t{3:.2f}%\t{4:.2f}%\t{5:.2f}%\t{6:.2f}%'.format(
                100 * self.Wd / self.totalWorkload,
                100 * self.Wi / self.totalWorkload,
                100 * self.Wm / self.totalWorkload,
                100 * self.Wg / self.totalWorkload,
                100 * self.Wv / self.totalWorkload,
                100 * self.Ws / self.totalWorkload,
                100 * self.Wa / self.totalWorkload ) )
        print( '' )
        print( 'Total Workload: {0}'.format( self.totalWorkload ) )
        print( 'Total Module Active Time: {0} ms'.format( self.totalActiveTime ) )
        print( 'Total Modle Run Time: {0} ms'.format( self.totalModelTime ) )

    def RunModel_arms(self,now):
        self.startModel()
        self.acceptModule( tac=100 )  # 接受指挥信号
        self.declarativeModule( tac=2500 )  # 陈述知识
        self.imaginalModule( tac=2500 )  # 知识检索
        self.procedualModule( tac=100 )  # 知识触发
        self.visionModule( tac=150 )  # 瞄准目标方位
        self.motorSpeechModule( tac=5000, speech='收到指令、剩余武器种类、剩余武器数目，命令是否存在冲突' )  # 报告收到，发送武器系统基本信息给指挥
        self.acceptModule( tac=100 )  # 再次接受指挥信号
        self.declarativeModule( tac=100 )  # 陈述知识
        self.imaginalModule( tac=100 )  # 知识检索
        self.procedualModule( tac=100 )  # 知识触发
        self.motorManualModule( tac=3000 )  # 执行命令
        self.motorSpeechModule( tac=5000, speech='完成指令、剩余武器种类、剩余武器数目' )  # 报告完成
        self.endModel()
        self.totalModelTime = self.Now() - self.startTime
        print( '' )
        print( '' )
        print( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        print( 'Active Time' )
        print(
            '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts,
                                                        self.Ta ) )
        print(
            '{0}%\t{1}%\t{2}%\t{3}%\t{4}%\t{5}%\t{6}'.format( round( 100 * self.Td / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ti / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tm / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tg / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Tv / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ts / self.totalActiveTime, 1 ),
                                                              round( 100 * self.Ta / self.totalActiveTime, 1 ) ) )
        print( 'Cognitive Workload' )
        print(
            '{0:.3f}\t{1:.3f}\t{2:.3f}\t{3:.3f}\t{4:.3f}\t{5:.3f}\t{6:.3f}'.format( self.Wd, self.Wi, self.Wm, self.Wg,
                                                                                    self.Wv, self.Ws, self.Wa ) )
        print(
            '{0:.2f}%\t{1:.2f}%\t{2:.2f}%\t{3:.2f}%\t{4:.2f}%\t{5:.2f}%\t{6:.2f}%'.format(
                100 * self.Wd / self.totalWorkload,
                100 * self.Wi / self.totalWorkload,
                100 * self.Wm / self.totalWorkload,
                100 * self.Wg / self.totalWorkload,
                100 * self.Wv / self.totalWorkload,
                100 * self.Ws / self.totalWorkload,
                100 * self.Wa / self.totalWorkload ) )
        print( '' )
        print( 'Total Workload: {0}'.format( self.totalWorkload ) )
        print( 'Total Module Active Time: {0} ms'.format( self.totalActiveTime ) )
        print( 'Total Modle Run Time: {0} ms'.format( self.totalModelTime ) )
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
        print( '{0:>15}\t{1:<30}'.format( str1, str2 ) )
        # 在指定的区域显示提示信息
        # 'Temperature:{0}(℃)    Pressure: {1}(Torr)    StartTime: {2}    Now: {3}'.format(self.TP_Data[0], self.TP_Data[1], self.starttime,str(datetime.now())[9:19])
        # datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] , time.toString(Qt.DefaultLocaleLongDate)[:-3]
        # self.cursor = self.textBrowser.textCursor()
        # self.textBrowser.moveCursor( self.cursor.End )  # 光标移到最后，这样就会自动显示出来
        # QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

