import csv
from flask_wtf import FlaskForm

a = 0


class Crosswords():
    a = 0
    count = 0

    def __init__(self):
        super().__init__()
        self.table = []
        self.maxx = 0
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
            for i in self.table:
                self.count += 1
                self.maxx = max(self.maxx, len(i))
        # print(self.table)

    def question_show(self):
        with open(f'data/crosswords/{self.a}', encoding='utf-8') as file:
            lines = file.read().split('\n')
            for ind, i in enumerate(lines):
                word_rus, word_ose = i.split()
                self.dictionary_words[str(ind + 1)] = [word_rus, word_ose]

    def new_table(self):
        # print("table", self.table)
        self.tab = [[' '] * self.maxx for i in range(self.count)]
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                # if self.tab[i][j].isalpha():
                #   self.tab[i][j] = '0'
                if self.table[i][j].isdigit():
                    self.tab[i][j] = self.table[i][j]
                else:
                    self.tab[i][j] = ' '
        # print("table", self.table)
        # print(self.tab)

    def add_word(self, id_of_question):
#        print('add', len(id_of_question))
 #       print(self.table)
        print('dfgh', self.dictionary_words)
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                # print(len(self.tab[i][j]))
                if self.tab[i][j] == id_of_question:
                    print(i, j)
                    for k in range(len(self.dictionary_words[id_of_question][1])):
                        self.tab[i][j + k + 1] = self.table[i][j + k + 1]
                    break

    def old_table(self, crossword):
        if crossword is not None:

            print('разгаданные слова', len(crossword))
            for k in crossword:
                self.add_word(k)
            print(self.tab)
        else:
            print('нет разгаданных слов')

# open_file()
