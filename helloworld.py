import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar
from PyQt5.QtWidgets import QAction, QStatusBar, QMenu, QCheckBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        path_to_icon1 = 'fugue-icons-3/icons/bug.png'
        button_action = QAction(QIcon(path_to_icon1), "Your button", self)
        button_action.setStatusTip("This is Bug Button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu) #Stop from toolbar disapearing from a right clicking it

        toolbar.addSeparator()

        path_to_icon2 = 'fugue-icons-3/icons/beer.png'
        button_action2 = QAction(QIcon(path_to_icon2), "Your button2", self)
        button_action2.setStatusTip("This is Beer Button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        box = QCheckBox()
        box.stateChanged.connect(self.clickBox)
        toolbar.addWidget(box)

        path_to_icon3 = 'fugue-icons-3/icons/prohibition.png'
        action4 = QAction(QIcon(path_to_icon3), "Quit", self)
        action4.triggered.connect(app.quit)
        toolbar.addAction(action4)

        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
        print("click", s)

    def clickBox(self, state):
        if state == Qt.Checked:
            print('Checked')
            label = QLabel("Hello")
            label.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(label)
        else:
            print('Unchecked')
            label = QLabel("This is a PyQt5 window!")
            label.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
