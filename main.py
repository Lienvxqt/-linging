import sys
from PyQt6 import *
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Цепляясь")
        self.setGeometry(300, 300, 800, 600)
        self.setUpMainWindow()

    def setUpMainWindow(self):
        label = QLabel("Цепляясь", self)
        label.move(380, 200)

        Start_Button = QPushButton("Начать новую игру", self)
        Start_Button.move(350, 350)
        Start_Button.clicked.connect(self.Start_eve)

        Load_Button = QPushButton("Загрузить", self)
        Load_Button.move(370, 400)
        Load_Button.clicked.connect(self.Load_eve)
        
        Exit_Button = QPushButton("Выйти", self)
        Exit_Button.move(370, 450)
        Exit_Button.clicked.connect(self.Exit_Button_eve)
    
    def Start_eve(self):
        print("В процессе разработки...")

    def Load_eve(self):
        print("В процессе разработки...")

    def Exit_Button_eve(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec())