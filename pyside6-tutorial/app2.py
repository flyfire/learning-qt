import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
)


class MainWindow0(QMainWindow):
    def __init__(self):
        super(MainWindow0, self).__init__()
        self.setWindowTitle('Widgets App')
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        for w in widgets:
            layout.addWidget(QLabel(w.__name__))
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


def test0():
    app = QApplication([])
    window = MainWindow0()
    window.show()
    app.exec()


class MainWindow1(QMainWindow):
    def __init__(self):
        super(MainWindow1, self).__init__()
        self.setWindowTitle('My App')
        widget = QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


def test1():
    app = QApplication([])
    window = MainWindow1()
    window.show()
    app.exec()


class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.setWindowTitle('My App')
        widget = QLabel()
        widget.setPixmap(QPixmap('naruto.jpeg'))
        self.setCentralWidget(widget)


class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()
        self.setWindowTitle('My App')
        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s)
        print(s == Qt.Checked)


class MainWindow4(QMainWindow):
    def __init__(self):
        super(MainWindow4, self).__init__()
        self.setWindowTitle('My App')
        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print('index changed', i)

    def text_changed(self, s):
        print('text changed', s)


def get_window(seq: int):
    window = None
    if seq == 0:
        window = MainWindow0()
    elif seq == 1:
        window = MainWindow1()
    elif seq == 2:
        window = MainWindow2()
    elif seq == 3:
        window = MainWindow3()
    elif seq == 4:
        window = MainWindow4()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(4)
