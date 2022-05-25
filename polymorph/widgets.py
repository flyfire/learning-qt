from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFrame, QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel

from question import QuestionInfo
from interactive_container_window import InteractiveMainWindow


class Intro1(QWidget):
    def __init__(self, question):
        super(Intro1, self).__init__()
        self.resize(1125, 800)
        v_layout = QVBoxLayout()
        label_1 = QLabel()
        label_1.setText(question.title)
        label_1.setStyleSheet("font-size:20px")
        label_1.setWordWrap(True)
        v_layout.addWidget(label_1, alignment=Qt.AlignCenter)
        label_2 = QLabel()
        label_2.setText(question.subtitle)
        label_2.setStyleSheet("font-size:16px")
        label_2.setWordWrap(True)
        v_layout.addWidget(label_2, alignment=Qt.AlignCenter)
        self.video_view = QVideoWidget()
        self.video_view.resize(640, 360)
        self.video_view.setGeometry(243, 300, 640, 360)
        v_layout.addWidget(self.video_view, alignment=Qt.AlignCenter)
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_view)
        media_content = QMediaContent(QUrl.fromLocalFile(question.video_path))
        self.media_player.setMedia(media_content)
        self.setLayout(v_layout)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.media_player.play()


def test():
    app = QApplication([])
    question = QuestionInfo(title="第一题", subtitle="请仔细看视频",
                            video_path="/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4")
    intro1 = Intro1(question)
    # window = InteractiveMainWindow()
    # window.question_container.addWidget(intro1)
    # window.show()
    intro1.show()
    app.exec()


if __name__ == '__main__':
    test()
