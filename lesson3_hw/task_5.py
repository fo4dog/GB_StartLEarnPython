'''
    6. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
        ◦ для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''


def fibonacci_numb(N):
    lst = [1, 0, 1]
    i = 3
    score = 0
    while i <= 2 * N - 1:
        lst.append(lst[i-2]+ lst[i-1])
        if score % 2 == 1:
            lst.insert(0, lst[-1])
        else:
            lst.insert(0, -lst[-1])
        score += 1
        i += 2
    print(lst)


n = int(input())
fibonacci_numb(n)