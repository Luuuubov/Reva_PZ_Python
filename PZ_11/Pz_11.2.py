# Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.


f1 = open('text18-22 (2).txt', encoding="UTF-16")
k = f1.read()
sum_m = 0
for i in k:
    if i.isupper():
        sum_m += 1

print(k)
print(f"Количество букв в верхнем регистре: {sum_m}")
f1.close()

f2 = open("text18-22 (2).txt", "r", encoding="UTF-8")
k = f2.readlines()
if len(k) >= 3:
    t_line = k[2]
    cod = [str(ord(ch)) for ch in t_line]
    k[2] = ' '.join(cod) + '\n'

f2 = open("2_text18-22.txt", "w", encoding="UTF-8")
f2.writelines(k)
f2.close()