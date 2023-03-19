# GUI
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ArmyTIGER_UI import ArmyTIGER

# NLP
import speech_recognition as sr

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
        self.working = True
        self.total_command = []
        
    def stop(self):
        self.working = False
        self.quit()
        self.wait(5000) #5000ms = 5s
        
    def resume(self):
        self.working = True
        
    def run(self):
        while self.working:
            command = self.stt()
            if command is not None:
                armyTIGER.update_STT.emit(command)
                self.total_command.append(command)
                print(f"Current Command : {command}")
                print(f"Total Command : {self.total_command}")
    
    def stt(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command = listener.recognize_google(voice,language='ko-KR')
            return command
        except:
            return None
            
            
                # armyTIGER.update_STT.emit("응답없음")
            
            # if '훈련상황' in self.command:
            #     self.yt(self.command)
            # else "실제상황" in self.command:
            #     self.yt(self.command)
                

class AnalysisThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.working = True
        self.total_command = ""
        self.parent = parent
    
    def start(self, text):
        self.run(text)
    
    def run(self, text):
        print(f"AnalysisThread : {text}")
        self.parent.ui.te_anw.setText(text)
        self.parent.ui.te_anw.repaint()
        self.quit()
        
        
        

startExecution = MainThread()

class Main(QMainWindow):
    cpath =""
    update_STT = pyqtSignal(str)
    
    def __init__(self, path):
        self.cpath = path
        super().__init__()
        self.ui = ArmyTIGER(path=current_path)
        self.ui.initUI(self)
        self.ui.btn_listening.clicked.connect(self.listeningTask)
        self.ui.btn_stop.clicked.connect(self.stopTask)
        self.update_STT.connect(self.ui.te_q.append)
        self.ui.te_q.textChanged.connect(self.analysisTask)
        self.analysisThread = AnalysisThread(self)
        
    def listeningTask(self):
        try:
            self.listening
            self.listening.deleteLater()
        except:
            self.listening = self.ui.listeningUI()
            startExecution.start()
    
    def processingTask(self):
        try:
            self.processing
            self.processing.deleteLater()
        except:
            self.processing = self.ui.processingUI()
            # startExecution.start()
    
    def stopTask(self):
        try:
            self.stop
            self.stop.deleteLater()
        except:
            self.stop = self.ui.stopUI()
            startExecution.stop()
        
    def analysisTask(self):
        self.analysisThread.start(self.ui.te_q.toPlainText())
        
            
    

current_path = os.getcwd()
app = QApplication(sys.argv)
armyTIGER = Main(path=current_path)
armyTIGER.show()
exit(app.exec_())    
    