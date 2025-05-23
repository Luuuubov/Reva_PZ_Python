# Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц



from functools import reduce

spisok = [5, 4, 5, 3, 2, 3, 5]
count_2 = len(list(filter(lambda x: x == 2, spisok)))
count_3 = len(list(filter(lambda x: x == 3, spisok)))
count_4 = len(list(filter(lambda x: x == 4, spisok)))
count_5 = len(list(filter(lambda x: x == 5, spisok)))

# Вычисление среднего арифметического с помощью reduce
re_s = reduce(lambda a, b: a + b, spisok) / len(spisok)
final_s = round(re_s)

print(f"Количество '2': {count_2}")
print(f"Количество '3': {count_3}")
print(f"Количество '4': {count_4}")
print(f"Количество '5': {count_5}")
print(f"Итоговая оценка: {final_s}")