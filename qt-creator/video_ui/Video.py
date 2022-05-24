from form import Ui_Video_UI
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaContent
from PyQt5.QtCore import QUrl


class VideoWindow(QWidget, Ui_Video_UI):
    def __init__(self):
        super(VideoWindow, self).__init__()
        self.setupUi(self)
        self.video_view = QVideoWidget(self)
        self.h_layout.addWidget(self.video_view)
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_view)
        self.play_pause.clicked.connect(self.play_pause_video)
        self.previous.clicked.connect(self.play_network_video)
        self.media_player.mediaStatusChanged.connect(self.on_state_changed)
        self.media_player.positionChanged.connect(self.on_position_changed)

    def play_pause_video(self):
        url = QUrl.fromLocalFile("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4")
        media_content = QMediaContent(url)
        self.media_player.setMedia(media_content)
        self.media_player.play()

    def play_network_video(self):
        url = QUrl("https://vd1.bdstatic.com/mda-hg6uempmez9u6mqi/sc/mda-hg6uempmez9u6mqi.mp4?auth_key=1562172911-0-0-4c22196ad1d0fcc49402d91336c999c5&bcevod_channel=searchbox_feed&pd=bjh&abtest=all")
        media_content = QMediaContent(url)
        self.media_player.setMedia(media_content)
        self.media_player.play()

    def on_state_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.play_network_video()

    def on_position_changed(self, position):
        self.lcdNumber.display(round(position / 1000))


def test():
    app = QApplication([])
    window = VideoWindow()
    window.show()
    window.play_pause_video()
    app.exec()


if __name__ == '__main__':
    test()
