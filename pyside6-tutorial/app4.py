from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar,
    QCheckBox
)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize


class ToolbarWindow0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar('My Main Toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('bug.png'), '&your button', self)
        button_action.setStatusTip('This is Your Button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence('Ctrl+p'))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action_2 = QAction(QIcon('bug.png'), '&your button2', self)
        button_action_2.setStatusTip('This is you button2')
        button_action_2.triggered.connect(self.onMyToolBarButtonClick)
        button_action_2.setCheckable(True)
        toolbar.addAction(button_action_2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action_2)

    def onMyToolBarButtonClick(self, s):
        print('click', s)


def get_window(seq: int):
    window = None
    if seq == 0:
        window = ToolbarWindow0()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(0)
