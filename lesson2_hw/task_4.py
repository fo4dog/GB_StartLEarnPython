'''
Задайте числами список из N элементов, заполненных из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях.
 Позиции хранятся в файле file.txt в одной строке одно число.
'''
import random

def create_list(N):
    lst = []
    for i in range(0, N):
        lst.append(random.randint(-N, N))
    return lst


def multipluy_lst(poses, lst):
    mult = 1
    for i in poses:
        mult = mult * lst[int(i) - 1]
    return mult


with open('numbers.txt') as f: # файл должен находиться в той же директории
    file = f.read()

numb = file.split()


a = int(input())
my_lst = create_list(a)
print(my_lst)
print(multipluy_lst(numb, my_lst))
