import sys
from typing import Any, Union

import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self._data)

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


def test():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    test()
