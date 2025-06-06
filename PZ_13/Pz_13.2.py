# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

import random

matrix = [[random.randint(1, 20) for _ in range(4)] for _ in range(4)]
print(f"Сгенерированная матрица:")
for i in matrix:
   print(i)

for i in [0, 2]:
    avg = sum(matrix[i]) / len(matrix[i])
    print(f"Среднее арифметическое  нечётной строки c индексом {i}: {avg}")