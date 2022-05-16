from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import PySide6


class _Bar(QtWidgets.QWidget):
    clickedValue = QtCore.Signal(int)

    def __init__(self, steps, *args, **kwargs):
        super(_Bar, self).__init__(*args, **kwargs)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        if isinstance(steps, list):
            self.n_steps = len(steps)
            self.steps = steps
        elif isinstance(steps, int):
            self.n_steps = steps
            self.steps = ['red'] * steps
        else:
            raise TypeError('steps must be a list or int')

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._padding = 4.0

    def sizeHint(self) -> PySide6.QtCore.QSize:
        return QtCore.QSize(40, 120)

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)

        # pen = painter.pen()
        # pen.setColor(QtGui.QColor('red'))
        # painter.setPen(pen)
        #
        # font = painter.font()
        # font.setFamily('Times')
        # font.setPointSize(18)
        # painter.setFont(font)
        #
        # painter.drawText(25, 25, f"{vmin}-->{value}<--{vmax}")
        # painter.drawText(40, 40, f"{n_steps_to_draw}")

        padding = 5
        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)
        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent
        bar_spacer = step_size * (1 - self._bar_solid_percent) / 2

        brush.setColor(QtGui.QColor('red'))
        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            rect = QtCore.QRect(
                padding,
                padding + d_height - ((n + 1) * step_size) + bar_spacer,
                d_width,
                bar_height
            )
            painter.fillRect(rect, brush)
        painter.end()

    def _trigger_refresh(self):
        self.update()

    def _calculate_clicked_value(self, e):
        parent = self.parent()
        vmin, vmax = parent.minimum(), parent.maximum()
        d_height = self.size().height() + (self._padding * 2)
        step_size = d_height / self.n_steps
        click_y = e.y() - self._padding - step_size / 2

        pc = (d_height - click_y) / d_height
        value = vmin + pc * (vmax - vmin)
        self.clickedValue.emit(value)

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(event)

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self._calculate_clicked_value(event)


class PowerBar(QtWidgets.QWidget):
    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar(steps)
        layout.addWidget(self._bar)
        self._dial = QtWidgets.QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setWrapping(False)
        layout.addWidget(self._dial)
        self.setLayout(layout)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        self._bar.clickedValue.connect(self._dial.setValue)

    def setColor(self, color):
        self._bar.steps = [color] * self._bar.n_steps
        self._bar.update()

    def setColors(self, colors):
        self._bar.n_steps = len(colors)
        self._bar.steps = colors
        self._bar.update()

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()

    def setBarSolidPercent(self, f):
        self._bar._bar_solid_percent = float(f)
        self._bar.update()

    def setBackgroundColor(self, color):
        self._bar._background_color = QtGui.QColor(color)
        self._bar.update()

    # def setNotchsVisible(self, b):
    #     return self._dial.setNotchesVisible(b)
    def __getattr__(self, item):
        if item in self.__dict__:
            return self[item]
        try:
            return getattr(self._dial, item)
        except AttributeError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")


def test():
    app = QtWidgets.QApplication([])
    # volume = PowerBar()
    volume = PowerBar(
        ["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f",
         "#9e0142"])
    volume.setBarPadding(2)
    volume.setBarSolidPercent(0.9)
    volume.setBackgroundColor('gray')
    volume.show()
    app.exec()


if __name__ == '__main__':
    test()
