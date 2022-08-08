import csv
import pandas as pd

class Note:

    def __init__(self):

        self.product = None
        self.shop = None
        self.prise = None
        self.array = [('Товар', 'Магазин', 'Цена товара')]

    def choose(self):

        choose = 0

        while choose != 6:
            print('Выберите что вы хотите сделать\n'
                  '1 - Добавить новую запись.\n'
                  '2 - Сохранить в файл.\n'
                  '3 - Показать данные.\n'
                  '4 - Вывести запись по названию товара.\n'
                  '5 - Отсортировать по названию товара\n'
                  '6 - Отсортировать по названию магазина\n'
                  '7 - Отсортировать по цене\n'
                  '0 - Выйти')
            choose = int(input())
            if choose == 1:
                self.write_to_array()
            elif choose == 2:
                self.save_in_file()
            elif choose == 3:
                self.show()
            elif choose == 4:
                self.find()
            elif choose == 5:
                self.insertion_item()
            elif choose == 6:
                self.insertion_market()
            elif choose == 7:
                self.insertion_cost()

    def write_to_array(self):
        self.product = input('Введите название товара> ')
        self.shop = input('Введите магазин> ')
        self.prise = input('Введите цену товара> ')
        print('\n')

        self.array.extend([(self.product, self.shop, self.prise)])

    def show(self):
        if (len(self.array) == 0):
            self.load_from_file()
        for i in range(len(self.array)):
            print("Название: " + self.array[i][0] + "; Магазин: " + self.array[i][1] + "; Цена: " +
                    self.array[i][2])

    def save_in_file(self):
        Filepath = "c:/DB/"
        self.filename = Filepath + input('Введите название файла> ') + '.txt'
        with open(self.filename, "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.array)

    def load_from_file(self):
        Filepath = "c:/DB/"
        filename = Filepath + input('Введите название файла, с которого нужно считать данные> ') + '.txt'
        File = open(filename, 'r', encoding='utf-8')
        while True:
            Line = File.readline()
            if not Line:
                break
            Text = Line.split(',')
            Text2 = Text[3].split('\n')
            self.array.append([Text[0], Text[1], Text[2], Text2[0]])

    def insertion_item(self):
        if (len(self.array) == 0):
            self.load_from_file()
        for i in range(len(self.array)):
            for k in range(i + 1, len(self.array)):
                if self.array[i][0] > self.array[k][0]:
                    for j in range(len(self.array) + 1):
                        self.array[i][j], self.array[k][j] = self.array[k][j], self.array[i][j]
        print(len(self.array))
        self.save_in_file()

    def insertion_market(self):
        if (len(self.array) == 0):
            self.load_from_file()
        for i in range(len(self.array)):
            for k in range(i + 1, len(self.array)):
                if self.array[i][1] > self.array[k][1]:
                    for j in range(len(self.array) + 1):
                        self.array[i][j], self.array[k][j] = self.array[k][j], self.array[i][j]
        print(len(self.array))
        self.save_in_file()

    def insertion_cost(self):
        if (len(self.array) == 0):
            self.load_from_file()
        for i in range(len(self.array)):
            for k in range(i + 1, len(self.array)):
                if self.array[i][2] < self.array[k][2]:
                    for j in range(len(self.array) + 1):
                        self.array[i][j], self.array[k][j] = self.array[k][j], self.array[i][j]
        print(len(self.array))
        self.save_in_file()

    def find(self):
        if (len(self.array) == 0):
            self.load_from_file()
        NameFind = input("Введите Название товара для поиска> ")
        for i in range(len(self.array)):
            if (self.array[i][0] == NameFind):
                print("Название: " + self.array[i][0] + "; Цена: " + self.array[i][2] + "; Магазин: " +
                      self.array[i][1])

some = Note()
some.choose()