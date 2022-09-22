'''
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
 многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

'''
возможно не совсем компактное решение, но я не смог придумать лучше, (чтобы при этом обрабатывались все опасные ситуации)'''
def the_polynomial(k):
    kof = []
    for i in range(k+1):
        kof.append(random.randint(0, 100))
    return kof


k = int(input())
idk = the_polynomial(k)
with open('test.txt', 'w') as file:
    polynomial = ''
    for i in range(len(idk)):
        if len(idk) - i - 1 == 0 and idk[i] != 0:
            polynomial += f'{idk[i]} = 0'
        elif idk[i] != 0 and idk[i] != 1:
            polynomial += f'{idk[i]}x**{len(idk) - i - 1} + '
        elif idk[i] == 1 and idk[i] != 0:
            polynomial += f'x**{len(idk) - i - 1} + '
        elif len(idk) - i - 1 == 0 and idk[i] == 0:
            polynomial = polynomial[:-2] + f'= 0'
    file.write(polynomial)
print(polynomial)