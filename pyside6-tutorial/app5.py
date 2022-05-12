from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel
)


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('hello')
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Something happened, is that OK?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class DialogWindow0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        button = QPushButton('Press me for a dialog!')
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print('click', s)
        # dlg = QDialog(self)
        # dlg.setWindowTitle('Hello!')
        # dlg.exec()
        dlg = CustomDialog(self)
        if dlg.exec():
            print('success!')
        else:
            print('cancel!')


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