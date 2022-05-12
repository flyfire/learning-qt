from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton, QLabel, QTabWidget
from PySide6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class LayoutWindow0(QMainWindow):
    def __init__(self):
        super(LayoutWindow0, self).__init__()
        self.setWindowTitle('My App')
        widget = Color('red')
        self.setCentralWidget(widget)


class LayoutWindow1(QMainWindow):
    def __init__(self):
        super(LayoutWindow1, self).__init__()
        self.setWindowTitle('My App')
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class LayoutWindow2(QMainWindow):
    def __init__(self):
        super(LayoutWindow2, self).__init__()
        self.setWindowTitle('My App')
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


class LayoutWindow3(QMainWindow):
    def __init__(self):
        super(LayoutWindow3, self).__init__()
        self.setWindowTitle('My App')
        layout = QGridLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class LayoutWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))

        layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class LayoutWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        pageLayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        pageLayout.addLayout(button_layout)
        pageLayout.addLayout(self.stack_layout)

        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab_0)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('red'))

        btn = QPushButton('green')
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('green'))

        btn = QPushButton('yellow')
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activate_tab_0(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(2)


class LayoutWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setDocumentMode(True)
        tabs.setMovable(True)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


def get_window(seq: int):
    window = None
    if seq == 0:
        window = LayoutWindow0()
    elif seq == 1:
        window = LayoutWindow1()
    elif seq == 2:
        window = LayoutWindow2()
    elif seq == 3:
        window = LayoutWindow3()
    elif seq == 4:
        window = LayoutWindow4()
    elif seq == 5:
        window = LayoutWindow5()
    elif seq == 6:
        window = LayoutWindow6()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(6)
