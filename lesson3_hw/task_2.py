'''
    2. Напишите программу, которая найдёт произведение пар чисел списка.
     Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
        ◦ [2, 3, 4, 5, 6] => [12, 15, 16];
        ◦ [2, 3, 5, 6] => [12, 15]
'''
import math


def multipluy(lst):
    new_lst = []
    for i in range(math.ceil(len(lst)/2)):
        new_lst.append(lst[i] * lst[-i - 1])
    return new_lst


lst = list(map(int, input().split()))

print(multipluy(lst))