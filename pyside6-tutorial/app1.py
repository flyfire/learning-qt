import sys
import PySide6.QtGui
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QTextEdit, QMenu
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.button_is_checked = True
        self.setWindowTitle('My App')
        self.button = QPushButton('Press Me!')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("clicked!")

    def the_button_was_toggled(self, checked):
        print('Checked?', checked)
        self.button_is_checked = checked
        print('toggled', self.button_is_checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print('released', self.button_is_checked)


def test0():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.button = QPushButton('Press Me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText('You already clicked me.')
        self.button.setEnabled(False)
        self.setWindowTitle('My Oneshot App')


def test1():
    app = QApplication([])
    window = MainWindow1()
    window.show()
    app.exec()


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle('My App')
        self.button = QPushButton('Press Me!')
        self.window_titles = [
            'My App',
            'My App',
            'Still My App',
            'Still My App',
            'What on earth',
            'What on earth',
            'This is surprising',
            'This is surprising',
            'Something went wrong'
        ]
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('clicked')
        new_window_title = choice(self.window_titles)
        print(f'setting title {new_window_title}')
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f'window title changed {window_title}')
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


def test2():
    app = QApplication([])
    window = MainWindow2()
    window.show()
    app.exec()


class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


def test3():
    app = QApplication([])
    window = MainWindow3()
    window.show()
    app.exec()


class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.label.setText('mousePressEvent')

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.label.setText('mouseReleaseEvent')

    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.label.setText('mouseDoubleClickEvent')


def test4():
    app = QApplication([])
    window = MainWindow4()
    window.show()
    app.exec()


class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        if e.button() == 1:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == 4:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")
        elif e.button() == 2:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        if e.button() == 1:
            self.label.setText("mouseReleaseEvent LEFT")
        elif e.button() == 4:
            self.label.setText("mouseReleaseEvent MIDDLE")
        elif e.button() == 2:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        if e.button() == 1:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == 4:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif e.button() == 2:
            self.label.setText("mouseDoubleClickEvent RIGHT")


def test5():
    app = QApplication([])
    window = MainWindow5()
    window.show()
    app.exec()


class MainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None:
        context = QMenu(self)
        context.addAction(PySide6.QtGui.QAction('test 1', self))
        context.addAction(PySide6.QtGui.QAction('test 2', self))
        context.addAction(PySide6.QtGui.QAction('test 3', self))
        context.exec(event.globalPos())


def test6():
    app = QApplication([])
    window = MainWindow6()
    window.show()
    app.exec()


class MainWindow7(QMainWindow):
    def __init__(self):
        super(MainWindow7, self).__init__()
        self.show()
        self.setContextMenuPolicy(PySide6.QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(PySide6.QtGui.QAction('test 1', self))
        context.addAction(PySide6.QtGui.QAction('test 2', self))
        context.addAction(PySide6.QtGui.QAction('test 3', self))
        context.exec(self.mapToGlobal(pos))


def test7():
    app = QApplication([])
    window = MainWindow7()
    app.exec()


class MainWindow8(QMainWindow):
    def __init__(self):
        super(MainWindow8, self).__init__()
        self.show()

    def mousePressEvent(self, event) -> None:
        print('Mouse Pressed!')
        super(self, MainWindow8).contextMenuEvent(event) # error


def test8():
    app = QApplication([])
    window = MainWindow8()
    app.exec()


class CustomButton0(QPushButton):
    def mousePressEvent(self, e: PySide6.QtGui.QMouseEvent) -> None:
        e.accept()


class CustomButton1(QPushButton):
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        e.ignore()
        return True


if __name__ == '__main__':
    # test0()
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    test8()
