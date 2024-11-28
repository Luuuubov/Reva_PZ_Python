# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.
def n_sum(n):
    total = 0  # Локальная переменная для хранения суммы
    a_number = 1  # Локальная переменная для текущего числа

    while a_number <= n:
        total += a_number
        a_number += 1

    return total 


result = n_sum(60)
print("Сумма чисел от 1 до 60:", result)