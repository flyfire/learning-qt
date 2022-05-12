from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor


class LayoutWindow0(QMainWindow):
    def __init__(self):
        super(LayoutWindow0, self).__init__()
        self.setWindowTitle('My App')


def get_window(seq: int):
    window = None
    if seq == 0:
        window = LayoutWindow0()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(0)