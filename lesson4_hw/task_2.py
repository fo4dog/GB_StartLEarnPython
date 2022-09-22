'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''


def simple_numbers(number):
    i = 2
    lst_of_simle_numbers = []
    while number >= i:
        if number % i == 0:
            number = number // i
            lst_of_simle_numbers.append(i)
        else:
            i += 1
    return lst_of_simle_numbers


num = int(input())
print(simple_numbers(num))