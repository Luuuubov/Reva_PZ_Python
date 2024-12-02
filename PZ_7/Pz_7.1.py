# Дана строка, изображающая целое положительное число. Вывести сумму цифр этого
# числа.

def sum_dig(number_1):
    total = 0
    for digit in number_1:
        total += int(digit)
    return total

number = input("Введите целое положительное число: ")
result = sum_dig(number)
print(f"Сумма цифр числа {number} равна {result}.")