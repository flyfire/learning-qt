# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Video_UI(object):
    def setupUi(self, Video_UI):
        Video_UI.setObjectName("Video_UI")
        Video_UI.resize(880, 600)
        self.frame = QtWidgets.QFrame(Video_UI)
        self.frame.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.frame.setMinimumSize(QtCore.QSize(640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 641, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(0)
        self.h_layout.setObjectName("h_layout")
        self.listView = QtWidgets.QListView(Video_UI)
        self.listView.setGeometry(QtCore.QRect(690, 10, 181, 581))
        self.listView.setObjectName("listView")
        self.previous = QtWidgets.QPushButton(Video_UI)
        self.previous.setGeometry(QtCore.QRect(10, 510, 100, 50))
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(Video_UI)
        self.next.setGeometry(QtCore.QRect(130, 510, 100, 50))
        self.next.setObjectName("next")
        self.play_pause = QtWidgets.QPushButton(Video_UI)
        self.play_pause.setGeometry(QtCore.QRect(250, 510, 100, 50))
        self.play_pause.setObjectName("play_pause")
        self.add_network_video = QtWidgets.QPushButton(Video_UI)
        self.add_network_video.setGeometry(QtCore.QRect(360, 510, 110, 50))
        self.add_network_video.setObjectName("add_network_video")
        self.add_local_video = QtWidgets.QPushButton(Video_UI)
        self.add_local_video.setGeometry(QtCore.QRect(480, 510, 110, 50))
        self.add_local_video.setObjectName("add_local_video")
        self.horizontalSlider = QtWidgets.QSlider(Video_UI)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 570, 640, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(Video_UI)
        self.lcdNumber.setGeometry(QtCore.QRect(610, 515, 75, 35))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Video_UI)
        QtCore.QMetaObject.connectSlotsByName(Video_UI)

    def retranslateUi(self, Video_UI):
        _translate = QtCore.QCoreApplication.translate
        Video_UI.setWindowTitle(_translate("Video_UI", "Video_UI"))
        self.previous.setText(_translate("Video_UI", "?????????"))
        self.next.setText(_translate("Video_UI", "?????????"))
        self.play_pause.setText(_translate("Video_UI", "??????"))
        self.add_network_video.setText(_translate("Video_UI", "??????????????????"))
        self.add_local_video.setText(_translate("Video_UI", "??????????????????"))
