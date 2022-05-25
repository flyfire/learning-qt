from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


def get_video_size(video_path):
    import subprocess
    import json
    cmd = f'ffprobe -select_streams v -show_entries format=duration,size,bit_rate,filename -show_streams -v quiet -of csv="p=0" -of json -i {video_path}'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    p.wait()
    output = p.stdout.read()
    output_json = json.loads(output)
    width = output_json["streams"][0]["width"]
    height = output_json["streams"][0]["height"]
    print(width, height)
    return width, height


def test_video_size():
    get_video_size("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/1.mp4")


class TestWindow(QMainWindow):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.widget.setLayout(self.v_layout)
        self.video_view = QVideoWidget()
        self.label = QLabel("hello")
        self.v_layout.addWidget(self.label)
        self.h_layout = QHBoxLayout()
        # self.h_layout.addStretch(1)
        self.video_view.resize(640, 360)
        self.h_layout.addWidget(self.video_view)
        self.h_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_view)
        self.setCentralWidget(self.widget)

    def set_media_and_play(self, video_path):
        width, height = get_video_size(video_path)
        real_width, real_height = int(width / 2), int(height / 2)
        self.video_view.resize(real_width, real_height)
        self.resize(width, height)
        media_content = QMediaContent(QUrl.fromLocalFile(video_path))
        self.player.setMedia(media_content)
        self.player.play()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.player.stop()


if __name__ == '__main__':
    # test_video_size()
    app = QApplication([])
    window = TestWindow()
    window.set_media_and_play("/Volumes/share/虚拟内容生产/测试/5min访谈测试/拆分成品/音乐mv/0316批次/2.mp4")
    window.show()
    app.exec()
