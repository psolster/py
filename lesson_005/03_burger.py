# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from lesson_005 import my_burger

my_burger.cutlet()
my_burger.cheese()
my_burger.bun()
my_burger.cucumber()
my_burger.onion()
my_burger.mustard()

print('мой бургер:')
my_burger.bun()
my_burger.cheese()
my_burger.cutlet()
my_burger.cutlet()
my_burger.cucumber()
my_burger.mustard()

print('и тут нет ошибки')
