# GUI
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ArmyTIGER_UI import ArmyTIGER

# NLP
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import Audio, load_dataset

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        self.working = True
        
    def run(self):
        # self.Intro()
        print("Thread Working")
        
    def stop(self):
        self.working = False
        self.quit()
        # print("Thread Stop")
        self.wait(5000) #5000ms = 5s
        
    # #function that will take the commands  to convert voice into text
    # def take_Command(self): 
    #     self.
    
    

class Main(QMainWindow):
    cpath =""
    
    def __init__(self, path):
        self.cpath = path
        super().__init__()
        self.setWindowTitle("ArmyTIGER Assistant")
        self.ui = ArmyTIGER(path=current_path)
        self.ui.initUI(self)
        self.ui.btn_listening.clicked.connect(self.listeningTask)
        self.ui.btn_stop.clicked.connect(self.stopTask)
        
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

if __name__ == "__main__":
    startExecution = MainThread()
    
    current_path = os.getcwd()
    app = QApplication(sys.argv)
    armyTIGER = Main(path=current_path)
    armyTIGER.show()
    exit(app.exec_())

    
    