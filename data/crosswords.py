import csv
from flask_wtf import FlaskForm

a = 0


class Crosswords():
    a = 0

    def __init__(self):
        super().__init__()
        self.table = []
        self.dictionary_words = dict()

    def open_file(self):
        with open(f'data/crosswords/animals.csv', encoding='UTF-8') as myf:
            reader = csv.reader(myf, delimiter=';')
            for index, row in enumerate(reader):
                if index > 1000:
                    break
                self.table.append(row)
            self.a = self.table[-1][0]
            self.table.pop()
            self.tab = self.table.copy()
        print(self.table)

    def question_show(self):
        with open(f'data/crosswords/{self.a}', encoding='utf-8') as file:
            lines = file.read().split('\n')
            for ind, i in enumerate(lines):
                word_rus, word_ose = i.split()
                self.dictionary_words[str(ind + 1)] = [word_rus, word_ose]

    def new_table(self):
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i][j].isalpha():
                    self.tab[i][j] = '0'
                if self.tab[i][j].isdigit():
                    self.tab[i][j] = int(self.tab[i][j])

# open_file()
