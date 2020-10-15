import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QTabWidget, QTableWidget
from PyQt5.QtWidgets import QPushButton, QFormLayout, QHBoxLayout, QVBoxLayout, QTableWidgetItem
from PyQt5.QtWidgets import QRadioButton, QLineEdit, QCheckBox, QTableView, QFileDialog, QHeaderView
from PyQt5.QtCore import Qt, QAbstractTableModel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import random
import csv

class tabdemo(QTabWidget):
    def __init__(self, parent = None):
        super(tabdemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")
        self.tab1UI()
        self.graphUI()
        self.tableUI()
        self.setWindowTitle("tab demo")

    def tab1UI(self):
        layout = QHBoxLayout()
        button = QPushButton("Select File", self)

        layout.addWidget(button)
        button.clicked.connect(lambda: self.openFileNameDialog())

        txt = ("""Note: \nProgram can only accept csv files.\n"""
        """Can only take 2 columns for input data.\nEx: Price vs. Time or """
        """Velocity vs. Time.\nAs of right now, this program is only capable line plots""")

        label = QLabel(txt)
        layout.addWidget(label)
        layout.addStretch(1)

        button3 = QPushButton("Show Table", self)
        layout.addWidget(button3)
        button3.clicked.connect(lambda: self.createTable(self.data_))

        self.setTabText(0,"Data")
        self.tab1.setLayout(layout)
        self.resize(800,480)

    def graphUI(self):
        self.setTabText(1,"Graph")
        self.figure = plt.figure(figsize=(8,8))
        self.canvas = FigureCanvasQTAgg(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        button2 = QPushButton("Graph", self)
        layout.addWidget(button2)
        button2.clicked.connect(lambda: self.plot(self.x_, self.y_))

        self.tab2.setLayout(layout)

    def tableUI(self):
        self.setTabText(2,"Table")
        self.layout = QVBoxLayout()


    def plot(self, x, y):
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, '*-')
        self.canvas.draw_idle()

    def getCSV(self, csvpath_tmp):
        with open('out.csv', newline='') as f:
            reader = csv.reader(f)
            next(reader) #skip first line, assume csv file has header
            data_ = list(reader)
            self.data_ = data_
            self.x_ = []
            self.y_ = []
            for i in data_:
                self.x_.append(int(i[0]))
                self.y_.append(int(i[1]))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",".csv Files (*.csv)", options=options)
        if fileName:
            self.getCSV(fileName)

    def createTable(self, data):
        self.tableWidget = QTableWidget()

        #Row count
        self.tableWidget.setRowCount(len(self.x_))

        #Column count
        self.tableWidget.setColumnCount(2)

        for (i, data_) in enumerate(data, 0):
            x, y = data_
            self.tableWidget.setItem(i,0, QTableWidgetItem(x))
            self.tableWidget.setItem(i,1, QTableWidgetItem(y))

        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.layout.addWidget(self.tableWidget)
        #self.setLayout(self.layout)
        self.tab3.setLayout(self.layout)

        self.show()


def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
