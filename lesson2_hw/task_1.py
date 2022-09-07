'''
    1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
        ◦ 6782 -> 23
        ◦ 0,56 -> 11
'''


def summ_digit(number):
    summ = 0
    number = str(number)
    for i in number:
        if i.isdigit():
            summ += int(i)
    return summ


a = float(input())
print(summ_digit(a))
