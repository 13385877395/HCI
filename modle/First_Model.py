from PyQt5.QtCore import QTime
import sys
sys.path.append(r"C:/Users/ASUS/Desktop/PYProjects/test")
from modle.Base_Model import BaseModel

class Model(BaseModel):
    def __init__(self):
        super(Model, self).__init__()

    def run(self,now):
        super(Model, self).run()
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
        print( '' )
        print( '' )
        print( 'Declarative\tImaginal\tManual\tGoal\tVision\tSpeech\tAuditory' )
        print( 'Active Time' )
        print( '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format( self.Td, self.Ti, self.Tm, self.Tg, self.Tv, self.Ts,
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

Model().run(QTime.currentTime())