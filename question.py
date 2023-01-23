import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5.uic.properties import QtWidgets

#from dict_words import sender


class Question(QDialog):
    def __init__(self, number_word, dictionary_words):
        super().__init__()
        self.label = QLabel(self)
        self.number_word = number_word
        self.dictionary_words = dictionary_words
        print("qqq", number_word)
        self.initUI()
        #sender = self.sender()
        #if sender == 'Сырдтæ':
        #self.label.setText(f'   {dictionary_words[number_word][0]}')
        print('ani')
   #     elif sender.text() == 'Халсар':
        self.label.setText(f'   {self.dictionary_words[number_word][0]}')
        print('veg')

    def initUI(self):
        self.setGeometry(800, 400, 600, 300)
        self.setWindowTitle('Фарста')
        self.setStyleSheet('background-color: #C19A6B')
        #self.setModal(True)

        v = QVBoxLayout(self)

        self.bbtn = QPushButton(self)
        self.bbtn.setText('Басгарын')
        self.bbtn.clicked.connect(self.check_word)
        self.bbtn.setFixedSize(230, 50)
        self.bbtn.move(185, 230)
        v.addWidget(self.bbtn)

        self.label = QLabel(self)
        self.label.setFixedSize(600, 100)
        self.label.setFont(QFont('Times New Roman', 27))
        self.label.move(0, 0)
        v.addWidget(self.label)

        h1 = QHBoxLayout(self)
        self.text = QLineEdit(self)
        self.text.setFixedSize(530, 50)
        # self.text.setText()
        self.text.setFont(QFont('Times New Roman', 25))
        self.text.move(0, 130)
        h1.addWidget(self.text)

        self.ae = QPushButton(self)
        self.ae.setFixedSize(50, 50)
        self.ae.setText('æ')
        self.ae.setStyleSheet('background-color: #79553D')
        self.ae.move(540, 130)
        self.ae.clicked.connect(self.print_ae)

        h1.addWidget(self.ae)
        v.addLayout(h1)

    def print_ae(self):
        self.text.setText('{}'.format(self.text.text() + 'æ'))

    def check_word(self):
        if self.text.text() == self.dictionary_words[self.number_word][1]:
            print('yes')
            #self.hide()
            #print(self.parent().answer)
            self.accept()
        else:
            self.message()


    def message(self):
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle('Рæдыд - ошибка')
        self.msg.setText('Фарст  æнæраст у! - Ответ неправильный!')

        self.msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Question()
    ex.exec_()
    sys.exit(app.exec_())
