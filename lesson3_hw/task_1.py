'''
    1. Задайте список из нескольких чисел.
    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
        ◦ [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

def lst_summ(lst):
    summ = sum(lst[1::2])
    return summ

lst = list(map(int,input().split()))
print(lst_summ(lst))
