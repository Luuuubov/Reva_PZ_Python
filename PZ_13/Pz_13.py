#  В двумерном списке найти минимальный элемент в предпоследнем столбце

import random
matrix = [[random.randint(0, 20) for _ in range(4)] for _ in range(4)]
print(f"Сгенерированная матрица: ")
for i in matrix:
   print(i)

print("Минимальный элемент в предпоследнем столбце:", min(i[-2] for i in matrix))