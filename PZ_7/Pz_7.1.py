# Дана строка, изображающая целое положительное число. Вывести сумму цифр этого
# числа.

def sum_dig(number_1):
    total = 0
    for digit in number_1:
        total += int(digit)
    return total

while True:
 try:
   number = int(input("Введите целое положительное число: "))
   break
 except ValueError:
   print("Неправильно ввели!")

result = sum_dig(str(number))
print(f"Сумма цифр числа {number} равна {result}.")