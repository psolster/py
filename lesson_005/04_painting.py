# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


import simple_draw as sd
from lesson_005.graph_pack import house
from lesson_005.graph_pack import humans
from lesson_005.graph_pack import rainbow
from lesson_005.graph_pack import smile
from lesson_005.graph_pack import snow_module
from lesson_005.graph_pack import tree

rainbow.rainbow(start_rainbow_point=(650, 800), end_rainbow_point=(1200, 400))
tree.draw_branches(start_point_branch=sd.get_point(1000, 130), angle_branch=90, length_branch=100)
tree.draw_branches(start_point_branch=sd.get_point(1100, 100), angle_branch=90, length_branch=100)
tree.draw_branches(start_point_branch=sd.get_point(1050, 180), angle_branch=90, length_branch=100)
tree.draw_branches(start_point_branch=sd.get_point(900, 90), angle_branch=90, length_branch=100)
house.house(center_of_house=(600, 300), width_house=300)
smile.smile(coordinat_centr=(650, 300), color_smile=sd.COLOR_WHITE)

sd.circle(center_position=sd.get_point(200, 500), radius=50, color=sd.COLOR_ORANGE, width=0)
humans.human(center_body=(950, 200), color_human=sd.COLOR_WHITE)
snow_module.snow_module(left_bottom=(50, 180), right_top=(430, 450), length_snow_line=8, number_snowflake=10)

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# Зачёт!
