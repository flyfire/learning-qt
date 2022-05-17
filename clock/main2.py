import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer, QObject, Signal

from time import strftime, localtime


class Backend(QObject):
    updated = Signal(str, arguments=['time'])
    hms = Signal(int, int, int, arguments=['hours', 'minutes', 'seconds'])

    def __init__(self):
        super(Backend, self).__init__()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        time = localtime()
        curr_time = strftime("%H:%M:%S", time)
        self.updated.emit(curr_time)
        self.hms.emit(time.tm_hour, time.tm_min, time.tm_sec)


def test():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')

    backend = Backend()
    engine.rootObjects()[0].setProperty('backend', backend)

    backend.update_time()
    sys.exit(app.exec())


if __name__ == '__main__':
    test()
