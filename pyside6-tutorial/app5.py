from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class DialogWindow0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        button = QPushButton('Press me for a dialog!')
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print('click', s)


def get_window(seq: int):
    window = None
    if seq == 0:
        window = DialogWindow0()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(0)