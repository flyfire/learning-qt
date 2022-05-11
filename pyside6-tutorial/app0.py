from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PySide6.QtCore import QSize, Qt
import sys


def hello():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()

    app.exec()


def test0():
    app = QApplication([])
    window = QPushButton("Push Me")
    window.show()
    app.exec()


def test1():
    app = QApplication([])
    window = QMainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)


def test2():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    # hello()
    # test0()
    # test1()
    test2()