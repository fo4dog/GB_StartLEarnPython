'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
        ◦ пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
'''


def multipluy_numbers(N):
    list_of_multiplies = [1]
    for i in range(2, N + 1):
        list_of_multiplies.append(list_of_multiplies[-1] * i)
    return list_of_multiplies


def idk(N):
    list_of_numbers = [1]
    for i in range(2, N + 1):
        list_of_numbers.append(int(str(list_of_numbers[-1]) + str(i)))
    return list_of_numbers

a = int(input())
print(multipluy_numbers(a))
print(idk(a))