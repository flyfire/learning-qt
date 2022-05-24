from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import PyQt5.QtGui as QtGui


class Example(QLabel):
    def __init__(self):
        super(Example, self).__init__()
        self.setStyleSheet("font-size:72px")
        self.resize(200, 150)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.setText("100")


def test():
    app = QApplication([])
    window = Example()
    window.show()
    app.exec()


if __name__ == "__main__":
    test()
