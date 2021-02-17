# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


class NotNameError(Exception):

    def __init__(self):
        self.message = 'Ошибка в указании имени'

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self):
        self.message = 'Ошибка при вводе e-mail'

    def __str__(self):
        return self.message


def filling_check(file):
    with open(file, 'r', encoding='utf8') as ff:
        for line in ff:
            line = line[:-1]
            try:
                name, e_male, age = line.split(' ')
            except ValueError as ve1:
                print(f'ошибка не соответствия содержания строки {ve1}')
            if len(name) or len(e_male) or len(age) != 0:
                if not name.isalpha():
                    try:
                        raise NotNameError
                    except NotNameError as exc:
                        print(f'Поймано исключение {exc}')
                elif '@' and '.' not in e_male:
                    try:
                        raise NotEmailError
                    except NotEmailError as exc:
                        print(f'Поймано исключение {exc}')
                elif 10 > int(age) > 99:
                    try:
                        raise ValueError
                    except ValueError as exc:
                        print(f'Поймано исключение {exc}')
            else:
                fgood = open('C:\\Users\\kampa\\PycharmProjects\\python_base\\lesson_010\\registrations_good.log', 'w',
                             encoding='utf8')
                fgood.write(line)
                fgood.close()


name_file = 'C:\\Users\\kampa\\PycharmProjects\\python_base\\lesson_010\\registrations.txt'
name_file = os.path.normpath(name_file)
filling_check(name_file)
