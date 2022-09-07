'''
Реализуйте алгоритм перемешивания списка.
'''
import random

def new_shufle(lst):
    for i in range(random.randint(100, 100000)):
        rand_poses_1 = random.randint(0, len(lst) - 1)
        rand_poses_2 = random.randint(0, len(lst) - 1)
        lst[rand_poses_1], lst[rand_poses_2] = lst[rand_poses_2], lst[rand_poses_1]
    return lst

my_lst = input().split()
print(new_shufle(my_lst))