'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

def check_predicate():
    a = [0, 1]
    b = [0, 1]
    c = [0, 1]
    for x in a:
        for y in b:
            for z in c:
                if not (x or y or z) == (not x and not y and not z):

                    print("Утверждение истинно")
                else:

                    print(f"Утверждение ложно")
check_predicate()