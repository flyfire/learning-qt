from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget
)
from random import randint


class AnotherWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(f'Another Window {randint(0, 100)}')
        layout.addWidget(self.label)
        self.setLayout(layout)


class Window0(QMainWindow):
    def __init__(self):
        super(Window0, self).__init__()
        self.w = None
        self.button = QPushButton('Push for Window')
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWidget()
            self.w.show()
        else:
            self.w.close()
            self.w = None


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWidget()
        self.button = QPushButton('Push for window')
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWidget()
        self.window2 = AnotherWidget()

        l = QVBoxLayout()
        button1 = QPushButton('Push for window 1')
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton('Push for window 2')
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


def get_window(seq: int):
    window = None
    if seq == 0:
        window = Window0()
    elif seq == 1:
        window = Window1()
    elif seq == 2:
        window = Window2()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(2)
