# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

text = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
# Используем filter для отбора только символов пунктуации
res_s= ''.join(filter(lambda ch: ch in string.punctuation, text))
print(res_s)

