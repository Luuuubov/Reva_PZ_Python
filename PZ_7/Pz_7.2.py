# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти длину самого длинного слова.

def txt_word(s):
    tx = s.split()
    lengs = list(map(len, tx))  #  длины всех слов
    return max(lengs)   # Возвращаем максимальную длину ( 0, если слов нет)

while True:
    text_i = input("Введите русские слова через пробел: ")
    if text_i.strip():
        break
    else:
        print("Строка не должна быть пустой! Попробуйте снова.")

result = txt_word(text_i)
print("Длина самого длинного слова:", result)