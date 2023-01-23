import sys
import csv

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QApplication, QMainWindow, QHBoxLayout, QMessageBox

from question import Question

# from dict_words import load_dict_words, dictionary_words

global answer


class Crosswords(QMainWindow):
    def __init__(self, cross_name):
        super().__init__()
        self.cross_name = cross_name
        self.count = 0
        self.answer = ""
        self.a = ''
        self.tablo = list()
        self.btna = list()
        self.dictionary_words = dict()
        self.initUI()

    def initUI(self):
        global a
        self.setGeometry(300, 300, 850, 850)
        self.setWindowTitle('Дзырдбыдтæ')
        self.setStyleSheet('background-color: #C19A6B')

        h = QHBoxLayout(self)
        self.btn_animals = QPushButton(self)
        self.btn_animals.setFixedSize(160, 65)
        self.btn_animals.move(60, 690)
        self.btn_animals.setText('Сырдтæ')
        self.btn_animals.setStyleSheet('background-color: #79553D')
        self.btn_animals.setFont(QFont('Times New Roman', 15))

        self.btn_animals.clicked.connect(self.name)

        self.btn_vaget = QPushButton(self)
        self.btn_vaget.setFixedSize(160, 65)
        self.btn_vaget.move(230, 690)
        self.btn_vaget.setText('Халсар')
        self.btn_vaget.setStyleSheet('background-color: #79553D')
        self.btn_vaget.setFont(QFont('Times New Roman', 15))

        self.btn_vaget.clicked.connect(self.name1)

        #   self.btn_animals.clicked.connect(self.gen_cross)
        #    h.addStretch()
        #   h.addWidget(self.btn_animals)

        # def gen_cross(self):
        #    a = ''


        with open(f'data/{self.cross_name}', encoding='UTF-8') as myf:
            reader = csv.reader(myf, delimiter=';')
            for index, row in enumerate(reader):
                if index > 1000:
                    break
                self.tablo.append(row)

        self.question_file = self.tablo[-1][0]
        del self.tablo[-1]

        with open(f'data/data/{self.question_file}', encoding='utf-8') as myf:
            lines = myf.read().split('\n')
            for ind, i in enumerate(lines):
                word_rus, word_ose = i.split()
                self.dictionary_words[str(ind + 1)] = [word_rus, word_ose]
        print(self.question_file)
        print(self.tablo)
        dy = 0
        for i in self.tablo:
            dx = 0
            dy += 60
            temp_btn = list()
            for j in i:
                if j == "'0'":
                    pass
                elif j == '/':
                    break
                elif j.isdigit():
                    self.btn = QPushButton(self)
                    self.btn.resize(60, 60)
                    self.btn.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
                    self.btn.setText(j)
                    self.btn.setFont(QFont('Arial', 25))
                    self.btn.move(dx + 10, dy)
                    self.btn.clicked.connect(self.question)
                else:
                    self.b = QLabel(self)
                    self.b.resize(60, 60)
                    self.b.setStyleSheet(
                        'border-style: solid; border-width: 1px; background-color: #79553D; color: #C19A6B')
                    self.b.setFont(QFont('Times New Roman', 25))
                    self.b.move(dx, dy)
                    temp_btn.append(self.b)

                dx += 60
            self.btna.append(temp_btn)

    def name(self):
        self.sender = self.btn_animals.text()

    def name1(self):
        self.sender = self.btn_vaget.text()

    def question(self):
        # получили индекс слова с кнопки
        s = self.sender()
        ind_word = s.text()
        print(ind_word)
        index = int(ind_word) - 1
        print("btna", len(self.btna[index]))
        try:
            self.quest = Question(ind_word, self.dictionary_words)
            self.quest.setWindowModality(2)

            result = self.quest.exec_()

            print("rez", result)
            if result == 1:
                print(self.dictionary_words[ind_word][1])
                for index, k in enumerate(self.dictionary_words[ind_word][1]):
                    print(ind_word)
                    self.btna[int(ind_word) - 1][index].setText(k)

            self.count += 1
            print(self.count)

        except Exception as e:
            print(e)
        if self.count == len(self.dictionary_words):
            self.message()

    def message(self):
            self.msg = QMessageBox(self)
            self.msg.setWindowTitle('Молодец')
            self.msg.setText('МОЛОДЕЦ!!! ты справился')

            self.msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Crosswords()
    ex.show()
    sys.exit(app.exec_())
