'''
    5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
        ◦ A (3,6); B (2,1) -> 5,09
        ◦ A (7,-5); B (1,-1) -> 7,21
'''

def distance_calculation(a, b):
    disrance = ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5
    print(int(disrance * 100)/ 100)

a = list(map(float, input().split()))
b = list(map(float, input().split()))

distance_calculation(a, b)