# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

import random
matrix = [[random.randint(1, 20) for _ in range(4)] for _ in range(4)]
print(f"Сгенерированная матрица: {matrix}")
# for row in matrix:
#     print(row)

ind = [0, 2]
a = list(map(lambda i: sum(matrix[i]) / len(matrix[i]), ind))
for i, avg in zip(ind, a):
    print(f"Среднее арифметическое  нечётной строки c индексом {i}: {avg}")