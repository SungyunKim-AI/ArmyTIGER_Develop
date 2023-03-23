# GUI
import sys
import os
import config
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ArmyTIGER_UI import ArmyTIGER
import time

# NLP
import speech_recognition as sr
import scipy.io.wavfile
import sounddevice as sd

class MainThread(QThread):
    def __init__(self):
        super().__init__()
        self.working = True
        
    def stop(self):
        self.working = False
        self.wait(3000)
        self.quit()
        
    def resume(self):
        self.working = True
        
    def run(self):
        # while self.working:
        command = self.stt()
        if command is not None:
            print(f"Command : {command}")
            self.analysis(command)
    
    def stt(self):
        try:
            listener = sr.Recognizer()
            file_path = "./IMG/시나리오1_훈련상황.wav"
            # file_path = "./IMG/시나리오2_실제상황.wav"
            audio_file = sr.AudioFile(file_path)
            v_samplerate, v_data = scipy.io.wavfile.read(file_path)
            sd.play(v_data, v_samplerate)
            time.sleep(26)
            print("Audio File Open")
            with audio_file as source:
                audio = listener.record(source)
            command = listener.recognize_google(audio, language='ko-KR')
            # with sr.Microphone() as source:
            #     print('Listening...')
            #     listener.pause_threshold = 1
            #     voice = listener.listen(source,timeout=4,phrase_time_limit=7)
            #     print("Recognizing...")
            #     command = listener.recognize_google(voice,language='ko-KR')
            return command
        except:
            return None
        
    def analysis(self, command):
        print(f"AnalysisThread : {command}")
        if "훈련 상황" in command:
            print("훈련상황")
            form = config.form_drill
            ASS = config.ASS_drill
        elif "실제 상황" in command:
            print("실제상황")
            form = config.form_real
            ASS = config.ASS_real
        else:
            print("기타상황")
            self.quit()
        form_text = f"{form['title']}\n1.시간 : {form['time']}\n2.장소 : {form['place']}\n3.식별자 : {form['identifier']}\n4.내용 : {form['situation']}\n5.조치내용 : {form['act']}"
        ASS_text = f"{ASS['date']}\n{ASS['force']}\n{ASS['act']}"
        
        armyTIGER.update_Anw.emit(form_text)
        armyTIGER.update_Q.emit(ASS_text)
        armyTIGER.baseUI_1.emit(True)
        armyTIGER.baseUI_2.emit(True)
        armyTIGER.repaint()
        self.stop()

class Main(QMainWindow):
    cpath =""
    update_Q = pyqtSignal(str)
    update_Anw = pyqtSignal(str)
    baseUI_1 = pyqtSignal(bool)
    baseUI_2 = pyqtSignal(bool)
    
    def __init__(self, path):
        self.cpath = path
        super().__init__()
        self.ui = ArmyTIGER(path=current_path)
        self.ui.initUI(self)
        self.ui.btn_listening.clicked.connect(self.listeningTask)
        self.ui.btn_stop.clicked.connect(self.stopTask)
        self.update_Q.connect(self.ui.te_q.setText)
        self.update_Anw.connect(self.ui.te_anw.setText)
        self.baseUI_1.connect(self.ui.label_listening.setHidden)
        self.baseUI_2.connect(self.ui.label_processing.setHidden)
        
    def listeningTask(self):
        # try:
        #     self.listening
        #     self.listening.deleteLater()
        # except:
        # self.listening = 
        self.ui.listeningUI()
        main_thread.start()
    
    def baseUITask(self):
        self.ui.label_base.hi
        # self.ui.label_listening.setHi hide()
        
    def stopTask(self):
        # try:
        #     self.stop
        #     self.stop.deleteLater()
        # except:
        # self.stop = 
        self.ui.stopUI()
        

main_thread = MainThread()
current_path = os.getcwd()
app = QApplication(sys.argv)
armyTIGER = Main(path=current_path)
armyTIGER.show()
exit(app.exec_())    
    