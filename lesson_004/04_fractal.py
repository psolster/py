# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# sd.resolution = (600, 600)
# start_point = sd.get_point(300, 5)
# angle = 45
# lenght = 100


# def draw_branches(start_point_brench, angle_brench, lenght_brench):
#
#     angle_brench_1 = angle_brench - 30
#     v1 = sd.get_vector(start_point_brench, angle_brench_1, lenght_brench, width=3)
#     v1.draw()
#     angle_brench_2 = angle_brench + 30
#     v2 = sd.get_vector(start_point_brench, angle_brench_2, lenght_brench, width=3)
#     v2.draw()
#
#
# draw_branches(start_point_brench=start_point, angle_brench=angle, lenght_brench=lenght)
#

# def draw_branches(start_point_brench, angle_brench, lenght_brench):
#     if lenght_brench < 10:
#         return
#
#     v1 = sd.get_vector(start_point_brench, angle_brench, lenght_brench, width=1)
#     v1.draw()
#     delta_angle_1 = angle_brench - 30
#     delta_angle_2 = angle_brench + 30
#     next_lenght_branches = lenght_brench * .75
#     draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_1, lenght_brench=next_lenght_branches)
#     draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_2, lenght_brench=next_lenght_branches)
#
#
# sd.resolution = (1200, 600)
# start_point = sd.get_point(600, 30)
# angle = 90
# lenght = 100


# draw_branches(start_point_brench=start_point, angle_brench=angle, lenght_brench=lenght)

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)
# draw_branches(start_point_brench=start_point, angle_brench=angle, lenght_brench=lenght)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branches(start_point_brench, angle_brench, lenght_brench):
    if lenght_brench < 2:
        return

    v1 = sd.get_vector(start_point_brench, angle_brench, lenght_brench, width=1)
    v1.draw()
    deviation_size = 30-(30 * (sd.random_number(0, 40) / 100))
    deviation_size_lenght = .75 - (.75 * (sd.random_number(0, 40) / 100))
    delta_angle_1 = angle_brench - deviation_size
    delta_angle_2 = angle_brench + deviation_size
    next_lenght_branches = lenght_brench * deviation_size_lenght
    draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_1, lenght_brench=next_lenght_branches)
    draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_2, lenght_brench=next_lenght_branches)


sd.resolution = (1200, 600)
start_point = sd.get_point(600, 30)
angle = 90
lenght = 100

draw_branches(start_point_brench=start_point, angle_brench=angle, lenght_brench=lenght)

# Пригодятся функции
# sd.random_number()

sd.pause()

# Зачёт!
