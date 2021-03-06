# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом


# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()

# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def trianlge(point_zero, angle_tr, lenght_tri, color):
    angle_fig = [angle_tr + 0, angle_tr + 120, angle_tr + 240]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght_tri, width=3)
    v.draw(color)
    for i in range(1, 3):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri, width=3)
        v.draw(color)


def kub(point_zero, angle_kub, lenght, color):
    angle_fig = [angle_kub + 0, angle_kub + 90, angle_kub + 180, angle_kub + 270]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color)
    for i in range(1, 4):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color)


def pentakl(point_zero, angle_pent, lenght, color):
    angle_fig = [angle_pent + 0, angle_pent + 72, angle_pent + 144, angle_pent + 144 + 72, angle_pent + 144 + 72 + 72]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color)
    for i in range(1, 5):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color)


def hexagon(point_zero, angle_hex, lenght, color):
    angle_fig = [angle_hex + 0, angle_hex + 60, angle_hex + 120, angle_hex + 180, angle_hex + 240, angle_hex + 300]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color)
    for i in range(1, 6):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color)


sd.resolution = (1200, 800)
point_zer_triangle = sd.get_point(300, 300)
point_zer_kub = sd.get_point(80, 80)
point_zer_pent = sd.get_point(200, 200)
point_zer_hex = sd.get_point(400, 400)
dlinna_vector = 80
angle = 0


color_maps = {'1': ['красный', sd.COLOR_RED],
              '2': ['оранжевый', sd.COLOR_ORANGE],
              '3': ['желтый', sd.COLOR_YELLOW],
              '4': ['зеленый', sd.COLOR_GREEN],
              '5': ['морской', sd.COLOR_CYAN],
              '6': ['голубой', sd.COLOR_BLUE],
              '7': ['фиолетовый', sd.COLOR_PURPLE]
              }

for key, value in color_maps.items():
    print(key, value[0])

a = input('Укажите № желаемого цвета фигуры. Цвета на выбор: Ваш выбор-> ')

if a in color_maps:
    trianlge(point_zero=point_zer_triangle, angle_tr=angle, lenght_tri=dlinna_vector, color=color_maps[a][1])
    kub(point_zero=point_zer_kub, angle_kub=angle, lenght=dlinna_vector, color=color_maps[a][1])
    pentakl(point_zero=point_zer_pent, angle_pent=angle, lenght=dlinna_vector, color=color_maps[a][1])
    hexagon(point_zero=point_zer_hex, angle_hex=angle, lenght=dlinna_vector, color=color_maps[a][1])
else:
    print('ну не попал в нужный')
    exit()
sd.pause()

# Зачёт!
