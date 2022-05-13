from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from FormGenerated0 import Ui_MainWindow


def test0():
    loader = QUiLoader()
    app = QtWidgets.QApplication([])
    window = loader.load('../qt-creator/0/form.ui', None)
    window.show()
    app.exec()



class Window0(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window0, self).__init__()
        self.setupUi(self)


def test1():
    app = QtWidgets.QApplication([])
    window = Window0()
    window.show()
    app.exec()


if __name__ == '__main__':
    # test0()
    test1()