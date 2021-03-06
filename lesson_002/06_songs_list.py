#!/usr/bin/env python3
# -*- coding: utf-8 -*-


violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]


time_3_songs = (
    violator_songs_list[3][1]
    + violator_songs_list[5][1]
    + violator_songs_list[8][1]
)

print('Три песни звучат-> ', round(time_3_songs, 2), ' минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


other_3_songs = (
    violator_songs_dict['Sweetest Perfection']
    + violator_songs_dict['Policy of Truth']
    + violator_songs_dict['Blue Dress']
)


print('А другие 3 песни звучат приблизительно -> ', round(other_3_songs, 0), ' минут')

# Зачёт!
