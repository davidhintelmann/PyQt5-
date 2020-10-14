import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QVBoxLayout
from PyQt5.QtWidgets import QAction, QPushButton, QWidget, QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.answer_ = ''

        self.setWindowTitle("Simple Calculator")
        self.setGeometry(500, 250, 300, 300)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)

        """names = ['AC', '+/-', '%', '',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '+', '=']

        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):

            if name == '':
                label = QLabel("Ans")
                grid.addWidget(label, *position)
            else:
                button = QPushButton(name)
                print(button.objectName())
                #button.clicked.connect(self.handleButton(name))
                button.clicked.connect(lambda x: self.my_custom_fn(name))
                grid.addWidget(button, *position)"""

        #button = QPushButton('+/-')
        #button.clicked.connect(lambda x: self.my_custom_fn('5'))
        #grid.addWidget(button, *(2,3))

        #button = QPushButton('%')
        #button.clicked.connect(lambda x: self.my_custom_fn('6'))
        #grid.addWidget(button, *(2,4))

        button = QPushButton('/')
        button.clicked.connect(lambda x: self.my_custom_fn('/'))
        grid.addWidget(button, *(1,5))

        button = QPushButton('7')
        button.clicked.connect(lambda x: self.my_custom_fn('7'))
        grid.addWidget(button, *(2,2))

        button = QPushButton('8')
        button.clicked.connect(lambda x: self.my_custom_fn('8'))
        grid.addWidget(button, *(2,3))

        button = QPushButton('9')
        button.clicked.connect(lambda x: self.my_custom_fn('9'))
        grid.addWidget(button, *(2,4))

        button = QPushButton('X')
        button.clicked.connect(lambda x: self.my_custom_fn('*'))
        grid.addWidget(button, *(2,5))

        button = QPushButton('4')
        button.clicked.connect(lambda x: self.my_custom_fn('4'))
        grid.addWidget(button, *(3,2))

        button = QPushButton('5')
        button.clicked.connect(lambda x: self.my_custom_fn('5'))
        grid.addWidget(button, *(3,3))

        button = QPushButton('6')
        button.clicked.connect(lambda x: self.my_custom_fn('6'))
        grid.addWidget(button, *(3,4))

        button = QPushButton('-')
        button.clicked.connect(lambda x: self.my_custom_fn('-'))
        grid.addWidget(button, *(3,5))

        button = QPushButton('1')
        button.clicked.connect(lambda x: self.my_custom_fn('1'))
        grid.addWidget(button, *(4,2))

        button = QPushButton('2')
        button.clicked.connect(lambda x: self.my_custom_fn('2'))
        grid.addWidget(button, *(4,3))

        button = QPushButton('3')
        button.clicked.connect(lambda x: self.my_custom_fn('3'))
        grid.addWidget(button, *(4,4))

        button = QPushButton('+')
        button.clicked.connect(lambda x: self.my_custom_fn('+'))
        grid.addWidget(button, *(4,5))

        button = QPushButton('0')
        button.clicked.connect(lambda x: self.my_custom_fn('0'))
        grid.addWidget(button, *(5,3))

        button = QPushButton('.')
        button.clicked.connect(lambda x: self.my_custom_fn('.'))
        grid.addWidget(button, *(5,4))

        label = QLabel("Ans")
        grid.addWidget(label, *(0,0))

        button = QPushButton('=')
        button.clicked.connect(lambda x: self.my_custom_equal(label))
        grid.addWidget(button, *(5,5))

        button = QPushButton('AC')
        button.clicked.connect(lambda x: self.my_custom_clear(label))
        grid.addWidget(button, *(1,2))

    def my_custom_fn(self, a):
        self.answer_ += a #string concatenation, eval() below will solve it

    def my_custom_equal(self, b):
        try:
            answer_ = eval(self.answer_) #evaluate the mathematical expression
        except Exception as e:
            print(e)
        else:
            b.setText(str(answer_))
            self.answer_ = str(answer_) #return result to int so user can continue calculations

    def my_custom_clear(self, b):
        b.setText('0')
        self.answer_ = ''

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
