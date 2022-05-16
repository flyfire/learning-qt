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

        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if self.last_x is None:
            self.last_x = event.x()
            self.last_y = event.y()
            return
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(self.last_x, self.last_y, event.x(), event.y())
        painter.end()
        self.label.setPixmap(canvas)

        self.last_x = event.x()
        self.last_y = event.y()

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None


def test():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    
if __name__ == '__main__':
    test()