from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import QProcess
import sys
import func
import threading

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None  # Default empty value.
        self.setWindowOpacity(0.2)
        self.setGeometry(-1, -1, 1367, 769)
        self.show()
        thread = threading.Thread(target=func.task)   
        thread.start()

    def start_process(self):
        print("start")
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            print("1")
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            print("2")
            
            
            
            
    def chek(self):
        while True:
            s = self.p.state()
            if s == 0:
                print("gg")
                quit()
                
                
    def process_finished(self):
        quit()
        self.p = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MainWindow()
    #w.show()
    
    app.exec_()