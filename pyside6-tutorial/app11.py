from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from random import randint, choice


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(QtGui.QColor('white'))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something8()

    def draw_something0(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something1(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something2(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100)
            )
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something3(self):
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100)
            )
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something4(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('#EB5160'))
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('#FFD141'))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(50, 50, 100, 100)
        painter.drawRect(60, 60, 150, 100)
        painter.drawRect(70, 70, 100, 150)
        painter.drawRect(80, 80, 150, 100)
        painter.drawRect(90, 90, 100, 150)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something5(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('#376F9F'))
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something6(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204, 0, 0))
        painter.setPen(pen)

        painter.drawEllipse(10, 10, 100, 100)
        painter.drawEllipse(10, 10, 150, 200)
        painter.drawEllipse(10, 10, 200, 300)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something7(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204, 0, 0))
        painter.setPen(pen)

        painter.drawEllipse(QtCore.QPoint(100, 100), 10, 10)
        painter.drawEllipse(QtCore.QPoint(100, 100), 15, 20)
        painter.drawEllipse(QtCore.QPoint(100, 100), 20, 30)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 25, 40)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 30, 50)
        # painter.drawEllipse(QtCore.QPoint(100, 100), 35, 60)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something8(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, 'Hello, World!')
        painter.drawText(200, 200, 100, 100, Qt.AlignHCenter, 'Hello, World!')
        painter.end()
        self.label.setPixmap(canvas)


def test():
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()
