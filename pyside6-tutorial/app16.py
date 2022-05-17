from PySide6.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSequentialAnimationGroup, QSize, \
    QParallelAnimationGroup


class Window0(QWidget):
    def __init__(self):
        super(Window0, self).__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        # self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        # self.anim.setEasingCurve(QEasingCurve.OutInCubic)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        self.anim.start()


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250, 150))
        self.anim_2.setDuration(2000)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2500)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


def get_window(seq: int):
    window = None
    if seq == 0:
        window = Window0()
    elif seq == 1:
        window = Window1()
    elif seq == 2:
        window = Window2()
    return window


def test(seq: int):
    app = QApplication([])
    window = get_window(seq)
    window.show()
    app.exec()


if __name__ == '__main__':
    test(2)
