import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QFileDialog, QComboBox

from crosswords import Crosswords


class ToCrosswords(QMainWindow):
    def __init__(self):
        #self.parent = parent
        super().__init__()
        #self.crossowrd_2 = Crossword2(self)
        #self.crosswords = Crosswords()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 500, 400)
        self.setStyleSheet('background-color: #C19A6B')
        self.setWindowTitle('Равзарут дзырдбыд')
        v = QVBoxLayout(self)

        self.select_cross = QComboBox(self)
        self.select_cross.resize(400, 50)
        self.select_cross.setFont(QFont('Times', 12))
        self.select_cross.move(10, 120)
        #self.select_cross.addItem('Равзарут дзырдбыд:D')
        self.select_cross.addItem('animals.csv')
        self.select_cross.addItem('vegetables.csv')
        self.select_cross.addItem('fruits.csv')
        print(self.select_cross.currentText())

        '''self.btn1 = QPushButton(self)
        self.btn1.resize(60, 50)
        self.btn1.move(420, 90)
        self.btn1.setText('крос')
        self.btn1.setFont(QFont('Times', 10))
        self.btn1.setStyleSheet('background-color: #673923')

        self.btn1.clicked.connect(self.cr1)'''
        '''self.cross1 = QLineEdit(self)
        self.cross1.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.cross1.setFont(QFont('Times', 10))
        cf1 = self.cross1.sender()
        print(cf1)
        self.cross1.setFixedSize(400, 50)
        self.cross1.move(10, 90)
        

        v.addWidget(self.cross1)

        self.cross2 = QLineEdit(self)
        self.cross2.setStyleSheet('QPushButton {background-color: #8A6642}')
        self.cross2.setFont(QFont('Times', 10))
        self.cf2 = self.cross2.sender()
        self.cross2.setFixedSize(400, 50)
        self.cross2.move(10, 160)
        self.btn2 = QPushButton(self)
        self.btn2.resize(60, 50)
        self.btn2.move(420, 160)
        self.btn2.setText('воп')
        self.btn2.setFont(QFont('Times', 10))
        self.btn2.setStyleSheet('background-color: #673923')

        self.btn2.clicked.connect(self.cr2)'''

        #v.addWidget(self.cross2)

        self.generate = QPushButton(self)
        self.generate.setFixedSize(300, 50)
        self.generate.move(90, 230)
        self.generate.setText('Скæнын')
        self.generate.setFont(QFont('Times', 16))
        self.generate.setStyleSheet('background-color: #673923')
        self.generate.clicked.connect(self.entr)

        #v.addWidget(self.generate)
        v.addStretch()




    def cr1(self):
        self.cross = QFileDialog.getOpenFileName()
        self.select_cross.currentText(str(self.cross[0]))
        #self.crosswords.show()
        #self.hide()


   # def cr2(self):
    #    self.cros =QFileDialog.getOpenFileName()
     #   self.cross2.setText(str(self.cros[0]))

    def entr(self):
        self.crosswords = Crosswords(self.select_cross.currentText())
        self.crosswords.show()
        self.hide()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToCrosswords()
    ex.show()
    sys.exit(app.exec_())
