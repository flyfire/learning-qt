from PySide6.QtMultimedia import QAudio, QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, QUrl, Signal, QRunnable, QThreadPool, QObject, Qt
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply


def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


class MediaWindow(QMainWindow):
    def __init__(self):
        super(MediaWindow, self).__init__()
        widget = QWidget()
        layout = QVBoxLayout()
        self._label1 = QLabel()
        self._label1.resize(400, 400)
        layout.addWidget(self._label1)
        self._label2 = QLabel()
        self._label2.resize(400, 400)
        layout.addWidget(self._label2)
        self._videoview = QVideoWidget()
        self._videoview.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        layout.addWidget(self._videoview)
        btn1 = QPushButton("load local image")
        layout.addWidget(btn1)
        btn1.clicked.connect(self.load_local_image)
        btn2 = QPushButton("load network image")
        btn2.clicked.connect(self.load_network_image)
        layout.addWidget(btn2)
        btn3 = QPushButton("play video")
        btn3.clicked.connect(self.play_video)
        layout.addWidget(btn3)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_local_image(self):
        image = QImage('/Users/ruhouhou/avatar0.png')
        self._label1.setPixmap(QPixmap.fromImage(image))

    def load_network_image(self):
        self.network_manager = QNetworkAccessManager()
        self.url = QUrl(
            "https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics3.baidu.com%2Ffeed%2F4b90f603738da9771fc82df753e998138418e34e.jpeg%3Ftoken%3Dbaa4897084d2f3de57cf6868d1937189&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1653411600&t=8a08636c320056b82ddf85479264f414")
        self.request = QNetworkRequest(self.url)
        self.reply = self.network_manager.get(self.request)
        self.reply.readyRead.connect(self.on_ready_read)

    def play_video(self):
        self._player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._player.setAudioOutput(self._audio_output)
        self._player.setVideoOutput(self._videoview)
        file = QUrl("/Users/ruhouhou/Downloads/引导.mp4")
        self._player.setSource(file)
        self._player.play()

    def on_ready_read(self):
        if self.reply.error() == QNetworkReply.NoError:
            pixel_map = QPixmap()
            pixel_map.loadFromData(self.reply.readAll())
            self._label2.setPixmap(pixel_map)


def test():
    app = QApplication([])
    window = MediaWindow()
    available_geometry = window.screen().availableGeometry()
    window.resize(int(available_geometry.width() / 2), int(available_geometry.height() / 2))
    window.show()
    app.exec()


def test_format():
    result = get_supported_mime_types()
    for type in result:
        print(type)


if __name__ == '__main__':
    # test()
    test_format()
