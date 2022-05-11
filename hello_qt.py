from PyQt6.QtWidgets import QApplication, QWidget
import sys


def hello():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()


if __name__ == '__main__':
    hello()