from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

class ArmyTIGER(object):
    cpath =""
    
    def __init__(self, path):
        self.cpath = path
        #Size
        self.pw, self.ph = 1000, 650
        # Color
        self.main_color = QColor('#06101a')
        self.blue_color = '#299CD7'
        self.green_color = '#315947'
        # Font
        font_bold = QFontDatabase.addApplicationFont(f"{self.cpath}/OTF/강한육군BoldOTF.otf")
        self.families = QFontDatabase.applicationFontFamilies(font_bold)
    
    def initUI(self, ArmyTIGER_UI):
        ArmyTIGER_UI.setObjectName("ArmyTIGER_UI")
        ArmyTIGER_UI.resize(self.pw, self.ph)
        
        # background
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, self.main_color)
        ArmyTIGER_UI.setPalette(self.palette)
        
        # main widget
        self.centralwidget = QWidget(ArmyTIGER_UI)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(self.pw, self.ph)
        
        self.label_base = QLabel(self.centralwidget)
        img = QPixmap(f"{self.cpath}/IMG/ArmyTIGER_removebg.png")
        h = int(self.ph/2 - img.height()/2)
        self.label_base.setGeometry(QRect(50, h-30, img.width(), img.height()))
        self.label_base.setPixmap(img)
        self.label_base.setObjectName("main_label")
        
        # STT Label
        self.label_text = QLabel(self.centralwidget)
        self.label_text.setGeometry(QRect(560, 30, 400, 800))
        self.label_text.setObjectName("text_label")
        
        self.lbl1 = QLabel('Assitant\'s Answer')
        self.lbl1.setFont(QFont(self.families[0],20)) #폰트,크기 조절
        self.lbl1.setStyleSheet(f"color: {self.green_color};") #글자색 변환
        
        self.te_anw = QTextEdit()
        self.te_anw.setAcceptRichText(False)
        
        self.lbl2 = QLabel('\nUser\'s Speech')
        self.lbl2.setFont(QFont(self.families[0],20))
        self.lbl2.setStyleSheet(f"color: {self.green_color};") #글자색 변환
        
        self.te_q = QTextEdit()
        self.te_q.setAcceptRichText(False)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te_anw)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.te_q)
        vbox.addStretch()
        self.label_text.setLayout(vbox)
        
        # 음성인식 버튼
        self.btn_listening = QPushButton(self.centralwidget)
        self.btn_listening.setGeometry(QRect(190, 580, 100, 30))
        self.btn_listening.setFont(QFont(self.families[0], 20))
        self.btn_listening.setStyleSheet("background-color: white;")
        self.btn_listening.setObjectName("btn_listening")
        
        # 중지 버튼
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QRect(290, 580, 100, 30))
        self.btn_stop.setFont(QFont(self.families[0], 20))
        self.btn_stop.setStyleSheet(f"background-color: {self.blue_color};")
        self.btn_stop.setObjectName("btn_stop")
        
        # listening
        self.label_listening = QLabel(self.centralwidget)
        self.label_listening.setGeometry(QRect(-30, 0, 600, 450))
        self.label_listening.setObjectName("label_listening")
        
        # processing
        self.label_processing = QLabel(self.centralwidget)
        self.label_processing.setGeometry(QRect(-30, 0, 600, 450))
        self.label_processing.setObjectName("label_processing")
        
        #voice_problem
        self.label_error = QLabel(self.centralwidget)
        self.label_error.setGeometry(QRect(-30, 0, 600, 450))
        self.label_error.setObjectName("label_problem")
        
        ArmyTIGER_UI.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArmyTIGER_UI)
        QMetaObject.connectSlotsByName(ArmyTIGER_UI)
        
        
    def listeningUI(self):
        self.btn_listening.setStyleSheet(f"background-color: {self.blue_color};")
        self.btn_stop.setStyleSheet("background-color: white;")
        self.label_listening.raise_()
        
        self.movie_listening = QMovie(f"{self.cpath}/IMG/listening.gif")
        self.label_listening.setMovie(self.movie_listening)
        self.movie_listening.start()
               
    def processingUI(self):
        self.label_processing.raise_()
        self.movie_processing = QMovie(f"{self.cpath}/IMG/processing.gif")
        # self.movie.setCacheMode(QMovie.CacheAll)
        self.label_processing.setMovie(self.movie_processing)
        self.movie_processing.start()
        
    def stopUI(self):
        self.btn_listening.setStyleSheet("background-color: white;")
        self.btn_stop.setStyleSheet(f"background-color: {self.blue_color};")
        
        self.label_error.raise_()
        self.movie_error = QMovie(f"{self.cpath}/IMG/processing.gif")
        # self.movie.setCacheMode(QMovie.CacheAll)
        self.label_error.setMovie(self.movie_error)
        self.movie_error.start()

    def retranslateUi(self, ArmyTIGER_UI):
        _translate = QCoreApplication.translate
        ArmyTIGER_UI.setWindowTitle(_translate("ArmyTIGER_UI", "MainWindow"))
        self.btn_listening.setText(_translate("ArmyTIGER_UI", "REC"))
        self.btn_stop.setText(_translate("ArmyTIGER_UI", "STOP"))
        

    

if __name__ == "__main__":
    import sys
    import os
    
    current_path = os.getcwd()
    app = QApplication(sys.argv)
    ArmyTIGER_UI = QMainWindow()
    ui = ArmyTIGER(path=current_path)
    ui.initUI(ArmyTIGER_UI)
    ArmyTIGER_UI.show()
    sys.exit(app.exec_())