
# #Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

fruits = {}
fr_1 = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16"
fr_1= fr_1.split()

fruits['Продукт1:'] = fr_1 [0]
fruits['Цена1:'] = []
for i in fr_1[1:6]:
    fruits['Цена1:'].append(int(i))

fruits['Продукт2:'] = fr_1 [6]
fruits['Цена2:'] = []
for i in fr_1[7:]:
    fruits['Цена2:'].append(int(i))

max_price_1 = max(fruits['Цена1:'])
max_price_2 = max(fruits['Цена2:'])

print(f"{fruits['Продукт1:']}: максимальная продажа = {max_price_1} кг")
print(f"{fruits['Продукт2:']}: максимальная продажа = {max_price_2} кг")