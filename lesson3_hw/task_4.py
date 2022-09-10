'''
    5. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
        ◦ 45 -> 101101
        ◦ 3 -> 11
        ◦ 2 -> 10
'''


def from_ten_to_two(number):
    string = ''
    while number != 0:
        string += str(number % 2)
        number = number // 2
    string = string[::-1]

    return int(string)


num = int(input())
print(from_ten_to_two(num))