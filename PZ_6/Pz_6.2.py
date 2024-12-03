# Даны списки A и B одинакового размера N. Поменять местами их содержимое и
# вывести вначале элементы преобразованного списка A, а затем — элементы
# преобразованного списка B.

while True:
 try:
   N = int(input("Введите размер списков N: "))
   break
 except ValueError:
   print("Неправильно ввели!")

A = []
for i in range(N):
    while True:
        try:
            A_elem = float(input(f"Введите элемент {i + 1} для списка A: "))
            A.append(A_elem)
            break
        except ValueError:
            print("Пожалуйста,введите число.")

B = []
for i in range(N):
    while True:
        try:
            B_elem = float(input(f"Введите элемент {i + 1} для списка B: "))
            B.append(B_elem)
            break
        except ValueError:
            print("Пожалуйста, введите число.")

A, B = B, A # меняю местами содержимое списков

print("Преобразованный список A:", A)
print("Преобразованный список B:", B)