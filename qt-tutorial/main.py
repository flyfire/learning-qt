import argparse
import sys

import pandas as pd
from PySide6.QtCore import QDateTime, QTimeZone, Slot, Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QKeySequence, QAction, QColor, QPainter
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QHeaderView, QSizePolicy, QTableView, QWidget, QApplication
import PySide6.QtCharts as QtCharts
from typing import Union, Any
import PySide6


def transform_data(utc, timezone=None):
    utc_fmt = 'yyyy-MM-ddTHH:mm:ss.zzzZ'
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_data(fname):
    df = pd.read_csv(fname)
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    timezone = QTimeZone(b"Europe/Berlin")

    times = df["time"].apply(
        lambda x: transform_data(x, timezone)
    )
    return times, magnitudes


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Earthquakes information")
        self.setCentralWidget(widget)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.input_dates = data[0].values
        self.input_magnitudes = data[1].values
        self.column_count = 2
        self.row_count = len(self.input_magnitudes)

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return self.row_count

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return self.column_count

    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Date", "Magnitude")[section]
        else:
            return f"{section}"

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            if column == 0:
                raw_date = self.input_dates[row]
                date = "{}".format(raw_date.toPython())
                return date[:-3]
            elif column == 1:
                return "{:.2f}".format(self.input_magnitudes[row])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None


class Widget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.model = CustomTableModel(data)
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.vertical_header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.horizontal_header.setStretchLastSection(True)

        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.add_series("Magnitude (Column 1)", [0, 1])
        
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.main_layout = QHBoxLayout()
        size = QSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Preferred
        )
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chart_view)

        self.setLayout(self.main_layout)

    def add_series(self, name, columns):
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        for i in range(self.model.rowCount()):
            t = self.model.index(i, 0).data()
            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"
            x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
            y = float(self.model.index(i, 1).data())
            if x > 0 and y > 0:
                self.series.append(x, y)

        self.chart.addSeries(self.series)

        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.model.color = "{}".format(self.series.pen().color().name())



def test():
    options = argparse.ArgumentParser()
    options.add_argument('-f', '--file', type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    # print(data)

    app = QApplication([])

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    test()
