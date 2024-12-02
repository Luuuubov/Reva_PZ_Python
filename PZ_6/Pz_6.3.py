# Дано множество A из N точек (точки заданы своими координатами х, у). Среди всех
# точек этого множества, лежащих во второй четверти, найти точку, наиболее
# удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми
# координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# .
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.

import math


N = int(input("Введите количество точек N: "))

#  для хранения координат
points = []

for i in range(N):
    x = float(input(f"Введите абсциссу {i + 1}-й точки: "))
    y = float(input(f"Введите ординату {i + 1}-й точки: "))
    points.append((x, y))

# Поиск точки во второй четверти с максимальным расстоянием от начала координат
max_point = None  # Изначально нет точки
max_distance = 0  # Изменение начального значения расстояния

for x, y in points:
    if x < 0 and y > 0:  # во второй ли четверти
        distance = math.sqrt(x**2 + y**2)  # Расчет расстояния
        if distance > max_distance:
            max_distance = distance
            max_point = (x, y)


if max_point:
    print("Точка, наиболее удаленная от начала координат:", max_point)
else:
    print("Нет точек во второй четверти. Координаты: (0, 0)")