'''
    3. Задайте список из вещественных чисел.
       Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
        ◦ [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


# def subtraction_of_max_and_min_fractional_parts(lst):
#     return max(lst) - min(lst)
#
#
# a = [round(float(s) - int(float(s)), 5) for s in input().split() if float(s) != int(float(s))]
# print(subtraction_of_max_and_min_fractional_parts(a))

# если прям совсем коротко, то так:

b = [round(float(s) - int(float(s)), 5) for s in input().split() if float(s) != int(float(s))]
print(max(b) - min(b))