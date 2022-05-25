from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QFrame


class InteractiveMainWindow(QMainWindow):
    def __init__(self):
        super(InteractiveMainWindow, self).__init__()
        self.resize(1125, 2436)
        frame = QFrame(self)
        frame.setGeometry(0, 0, 1125, 2436)
        question_widget = QWidget(frame)
        question_widget.setGeometry(0, 200, 1125, 800)
        question_widget.setStyleSheet("background-color:red")
        self.question_container = QHBoxLayout(question_widget)
        self.setCentralWidget(frame)
