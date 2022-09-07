'''
    3. Задайте список из n чисел последовательности  выведите на экран их сумму.
'''


def order(N):
    list_of_order = []
    for i in range(1, N+1):
        list_of_order.append((1 + (1 / i)) ** i)
    return list_of_order


a = int(input())
generated_order = order(a)
order_summ = sum(generated_order)
print(generated_order)
print(order_summ)