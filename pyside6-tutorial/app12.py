from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import PySide6


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPoint(event.x(), event.y())
        painter.end()
        self.label.setPixmap(canvas)


def test():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()