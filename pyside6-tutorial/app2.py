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


class MainWindow5(QMainWindow):
    def __init__(self):
        super(MainWindow5, self).__init__()
        self.setWindowTitle('My App')
        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print('index changed', i.text())

    def text_changed(self, s):
        print('text changed', s)


class MainWindow6(QMainWindow):
    def __init__(self):
        super(MainWindow6, self).__init__()
        self.setWindowTitle('My App')
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your text')
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        self.setCentralWidget(widget)


    def return_pressed(self):
        print('return pressed!')
        self.centralWidget().setText('BOOM!')

    def selection_changed(self):
        print('selection changed')
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print('text changed...')
        print(s)

    def text_edited(self, s):
        print('text edited...')
        print(s)


class MainWindow7(QMainWindow):
    def __init__(self):
        super(MainWindow7, self).__init__()
        self.setWindowTitle('My App')
        widget = QSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)
        self.setCentralWidget(widget)

    def value_changed(self, i):
        print('value changed', i)

    def value_changed_str(self, s):
        print('valued changed str', s)


class MainWindow8(QMainWindow):
    def __init__(self):
        super(MainWindow8, self).__init__()
        self.setWindowTitle('My App')
        widget = QSlider(Qt.Vertical)
        widget.setMinimum(0)
        widget.setMaximum(10)
        widget.setSingleStep(1)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)

    def value_changed(self, i):
        print('value changed', i)

    def slider_position(self, p):
        print('position', p)

    def slider_pressed(self):
        print('pressed')

    def slider_released(self):
        print('released')


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
    elif seq == 5:
        window = MainWindow5()
    elif seq == 6:
        window = MainWindow6()
    elif seq == 7:
        window = MainWindow7()
    elif seq == 8:
        window = MainWindow8()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(0)
