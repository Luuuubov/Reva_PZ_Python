# Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее
# арифметическое AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух
# положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные
# параметры вещественного типа). С помощью этой функции найти среднее
# арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
# A, B, C, D.
def Mean(X, Y):
    AMean = (X + Y) / 2  #  среднее арифметическое
    GMean = (X * Y) ** 0.5  #  среднее геометрическое
    return AMean, GMean # Возвращает результаты

while True:
    try:
      A =float(input("Введите число А:"))
      break
    except ValueError:
        print("Неправильно ввели!")  # если пользователь ввёл не число, а допустим текст, прогррамма завершается ошибкой выводя текст

while True :
    try:
      B = float(input("Введите число B:"))
      break
    except ValueError:
        print("Неправильно ввели!")

while True:
    try:
        C =float(input("Введите число C:"))
        break
    except ValueError:
        print("Неправильно ввели!")

while True :
    try:
      D = float(input("Введите число D:"))
      break
    except ValueError:
        print( "Неправильно ввели!")

# Вычислила средние для пар (A, B), (A, C), (A, D)
mean_AB = Mean(A, B)
mean_AC = Mean(A, C)
mean_AD = Mean(A, D)


print(f"Среднее арифметическое и геометрическое для (A, B): {mean_AB}")
print(f"Среднее арифметическое и геометрическое для (A, C): {mean_AC}")
print(f"Среднее арифметическое и геометрическое для (A, D): {mean_AD}")