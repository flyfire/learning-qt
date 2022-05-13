from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                               QVBoxLayout, QWidget, QProgressBar)
from PySide6.QtCore import QProcess
import re

progress_re = re.compile("Total complete: (\d+)%")


def simple_percent_parser(output):
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.p = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.progress)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:
            self.message('Executing progress.')
            self.p = QProcess()
            self.p.finished.connect(self.process_finished)
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.start('python', ['dummy_script.py'])

    def process_finished(self):
        self.message('process finished')
        self.p = None

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode('utf8')
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode('utf8')
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not Running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running'
        }
        state_name = states[state]
        self.message(f'State change: {state_name}')


def test():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()
