# Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
# функции
def duble(a, b=20):
 ploch = a * b
 perim = 2 * (a + b)
 return ploch, perim
width = float(input('Введи ширину: '))
height = float(input('Введи высоту: '))
g_ploch, g_perim = duble(width, height)
print('Площадь прямоугольника: ', g_ploch)
print('Периметр прямоугольника: ', g_perim)
