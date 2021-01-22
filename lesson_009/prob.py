import operator
from pprint import pprint

alpha_count = {}


class CountSymbol:
    def __init__(self, filename):
        self.filename = filename
        self.count_lines = 0
        self.position_on_files = 0
        self.sorted_alpha_count = {}

    def step_by_step(self):
        self.lenght_file()
        while self.count_lines != 0:
            symb_line = self.get_data(self.filename)
            self.count_symb_in_line(symb_line)
        self.sorted_alpha_count = self.sorter()
        self.print_rezults(self.sorted_alpha_count)

    def lenght_file(self):
        ff = open(self.filename, 'r', encoding='cp1251')
        self.count_lines = sum(1 for _ in ff)
        ff.close()

    def get_data(self, filename):
        file = open(filename, 'r', encoding='cp1251')
        file.seek(self.position_on_files)
        data = file.readline()
        self.position_on_files = file.tell()
        self.count_lines -= 1
        file.close()
        return data

    def count_symb_in_line(self, data):
        for char in data:
            if 1040 <= ord(char) <= 1103:
                if char in alpha_count.keys():
                    alpha_count[char] += 1
                else:
                    alpha_count[char] = 1
            elif ord(char) == 1025:
                if char in alpha_count.keys():
                    alpha_count[char] += 1
                else:
                    alpha_count[char] = 1
            elif ord(char) == 1105:
                if char in alpha_count.keys():
                    alpha_count[char] += 1
                else:
                    alpha_count[char] = 1

    def sorter(self, revers=False):
        sorted_list = sorted(alpha_count.items(), key=operator.itemgetter(1), reverse=revers)
        return {k: v for k, v in sorted_list}

    def print_rezults(self, norm_voc):
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Буква', mes2='Кол-во'))
        print('+---------------+')
        for letter, count in norm_voc.items():
            print('|{letter:^6} | {count:6d}|'.format(letter=letter, count=count))
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Итого', mes2=sum(norm_voc.values())))
        print('+---------------+')


file_name = 'voyna-i-mir.txt'
start = CountSymbol(file_name)
start.step_by_step()
res = start.sorter(revers=True)
start.print_rezults(res)

# import operator
# from pprint import pprint
# alpha_count = {}
# file_name = 'voyna-i-mir.txt'
# for cod in range(1040, 1104):
#     alpha_count[chr(cod)] = 0
# alpha_count['Ё'] = 0
# alpha_count['ё'] = 0
# with open(file_name, 'r', encoding='cp1251') as file:
#     for line in file:
#         for char in line:
#             if char in alpha_count.keys():
#                 alpha_count[char] += 1
# sorted_list = sorted(alpha_count.items(), key=operator.itemgetter(1), reverse=True)
# sorted_alpha_count = {k: v for k, v in sorted_list}
# print('+---------------+')
# print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Буква', mes2='Кол-во'))
# print('+---------------+')
# for letter, count in sorted_alpha_count.items():
#     print('|{letter:^6} | {count:6d}|'.format(letter=letter, count=count))
# print('+---------------+')
# print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Итого', mes2=sum(sorted_alpha_count.values())))
# print('+---------------+')