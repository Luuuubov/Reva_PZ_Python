#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое четных элементов:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма нечетных положительных элементов:


l = ['-99 6 12 -36 20 45 100 -15']
f1 = open('data_1.txt', 'w', encoding="UTF-8")
f1.writelines(l)
f1.close()

f2 = open('data_2.txt', 'w', encoding="UTF-8")
f2.write('Содержимое первого файла: ')
f2.write('\n')
f2.writelines(l)
f2.close()

f1 = open('data_1.txt',encoding="UTF-8")
k = f1.read()
k = k.split()
ev = []
# num = []
for num_str in k:
    num = int(num_str)
    if num % 2 == 0:
     ev.append(num)

aver = sum(ev) / len(ev)

f2 = open('data_2.txt', 'a', encoding="UTF-8")
f2.write('\n')
f2.write(f"Четные элементы: {ev}\n")
f2.write(f"Количество четных элементов: {len(ev)}\n")
f2.write(f"Среднее арифметическое четных элементов: {aver}\n")
f2.close()



l2 = ['-45 3 14 -67 24 45 88 -4']
f3 = open('data_2.txt', 'w', encoding="UTF-8")
f3.writelines(l2)
f3.close()

f2 = open('data_4.txt', 'w', encoding="UTF-8")
f2.write('Содержимое второго файла: ')
f2.write('\n')
f2.writelines(l2)
f2.close()

f3 = open('data_3.txt', encoding="UTF-8")
k = f3.read()
k = k.split()
ret = []
positive = 0
for num_str in k:
  num = int(num_str)
  if num % 2 != 0:
   ret.append(num)
   if num > 0:
    positive += num

f2 = open('data_2.txt', 'a', encoding="UTF-8")
f2.write('Содержимое второго файла: ')
f2.write('\n')
f2.writelines(l2)
f2.close()

f2 = open('data_2.txt', 'a', encoding="UTF-8")
f2.write('\n')
f2.write(f"Нечетные элементы: {ret}\n")
f2.write(f"Количество нечетных элементов: {len(ret)}\n")
f2.write(f"Сумма нечетных положительных  элементов: {positive}\n")
f2.close()