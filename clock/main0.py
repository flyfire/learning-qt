from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer
import sys
from time import strftime, localtime


def test():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')

    def update_time():
        curr_time = strftime("%H:%M:%S", localtime())
        engine.rootObjects()[0].setProperty('currTime', curr_time)

    timer = QTimer()
    timer.setInterval(100)
    timer.timeout.connect(update_time)
    timer.start()

    update_time()
    sys.exit(app.exec())


if __name__ == '__main__':
    test()