'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
'''


def coordinates_range(number):
    if number == 1:
        print('X > 0 and Y > 0')
    elif number == 2:
        print('X < 0 and Y > 0')
    elif number == 3:
        print('X < 0 and Y < 0')
    elif number == 4:
        print('X > 0 and Y < 0')
    else:
        print('Такой четверти не существует')

a = int(input())
coordinates_range(a)