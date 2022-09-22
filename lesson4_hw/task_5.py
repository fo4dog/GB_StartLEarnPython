'''
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
'''


def pol_sum(p1, p2):
    p1_new = []
    p2_new = []
    p_sum = []
    p1 = p1.split()
    p2 = p2.split()
    for i in range(len(p1)):
        if p1[i].split('x')[0] == '':
            p1_new.append(1)
        elif p1[i].split('x')[0].isdigit():
            p1_new.append(int(p1[i].split('x')[0]))
    for i in range(len(p2)):
        if p2[i].split('x')[0] == '':
            p2_new.append(0)
        elif p2[i].split('x')[0].isdigit():
            p2_new.append(int(p2[i].split('x')[0]))

    if len(p2_new) >= len(p1_new):
        p1_new.reverse()
        for i in range(len(p2_new) - len(p1_new)):
            p1_new.append(0)
        p1_new.reverse()

    elif len(p2_new) <= len(p1_new):
        p2_new.reverse()
        for i in range(len(p1_new) - len(p2_new)):
            p2_new.append(0)
        p2_new.reverse()
    for i in range(len(p2_new)):
        p_sum.append(p2_new[i] + p1_new[i])
    return p_sum

with open("test.txt", 'r') as f:
    pol1 = f.read()

with open("test1.txt", 'r') as f:
    pol2 = f.read()

polinomal_sum = pol_sum(pol1, pol2)

with open('test2.txt', 'w') as file:
    polynomial = ''
    for i in range(len(polinomal_sum)):
        if len(polinomal_sum) - i - 1 == 0 and polinomal_sum[i] != 0:
            polynomial += f'{polinomal_sum[i]} = 0'
        elif polinomal_sum[i] != 0 and polinomal_sum[i] != 1:
            polynomial += f'{polinomal_sum[i]}x**{len(polinomal_sum) - i - 1} + '
        elif polinomal_sum[i] == 1 and polinomal_sum[i] != 0:
            polynomial += f'x**{len(polinomal_sum) - i - 1} + '
        elif len(polinomal_sum) - i - 1 == 0 and polinomal_sum[i] == 0:
            polynomial = polynomial[:-2] + f'= 0'
    file.write(polynomial)
print(polynomial)