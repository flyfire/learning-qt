import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QGridLayout)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimerEvent


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        images = [
            '/Users/ruhouhou/avatar0.png', '/Users/ruhouhou/avatar0.png', '/Users/ruhouhou/avatar0.png',
            '', '10', ''
        ]
        positions = [(i, j) for i in range(2) for j in range(3)]
        for position, image in zip(positions, images):
            if image == '':
                continue
            elif image == '10':
                self.timer_label = QLabel(image)
                self.timer_label.setStyleSheet("font-size:36px")
                grid.addWidget(self.timer_label, *position, alignment=Qt.AlignCenter)
            else:
                label = QLabel()
                label.setPixmap(QPixmap.fromImage(QImage(image)))
                grid.addWidget(label, *position, alignment=Qt.AlignCenter)

    def start_timer(self):
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        current = int(self.timer_label.text())
        current -= 1
        self.timer_label.setText(str(current))
        if current == 0:
            self.killTimer(self.timer_id)


def test():
    app = QApplication([])
    window = Example()
    window.show()
    window.start_timer()
    app.exec()


if __name__ == '__main__':
    test()
