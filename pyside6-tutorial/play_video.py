import PySide6
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout, QApplication, QVBoxLayout


class VideoWidget(QWidget):
    def __init__(self):
        super(VideoWidget, self).__init__()
        self.resize(800, 400)
        self.setStyleSheet("background-color:grey")
        v_layout = QVBoxLayout()
        layout = QHBoxLayout()
        self.video_view = QVideoWidget()
        self.video_view.resize(640, 360)
        layout.addStretch(1)
        layout.addWidget(self.video_view, 4)
        layout.addStretch(1)
        v_layout.addLayout(layout, 9)
        v_layout.addStretch(1)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_view)
        video_url = QUrl("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4")
        self.media_player.setSource(video_url)

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        self.media_player.play()


def test():
    app = QApplication([])
    window = VideoWidget()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()
