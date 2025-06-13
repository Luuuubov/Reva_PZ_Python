# Программа с применением пакета tk, в качестве условия задача из PZ_2:
# введи целое число, большее 999. Используя одну операцию деления нацело и одну
# операцию взятия остатка от деления, найти цифру,
# соответствующую разряду сотен в записи этого числа
import tkinter as tk
from tkinter import messagebox

def digit():
    try:
        input_text = en_num.get()
        number = int(input_text)
        if number <= 999:
            messagebox.showerror("Ошибка ввода", "Это число явно не больше 999, введите ещё раз!")
            return
        units = number // 100
        digit = units % 10
        result_l.config(text=str(digit))

    except ValueError:
        messagebox.showerror("Ошибка ввода", "Введите ЦЕЛОЕ ЧИСЛО.")

root = tk.Tk()
root.title("Найти разряд сотен")
root.geometry("400x180") #  окно

inst_l = tk.Label(root, text="Введите целое число, большее 999:")
inst_l.grid(row=0, column=0, padx=10, pady=10, sticky="w") # w  по левому краю

en_num = tk.Entry(root, width=30)# Поле ввода
en_num.grid(row=0, column=1, padx=10, pady=10)

calcul_b = tk.Button(root, text="Найти разряд сотен", command=digit)#  Кнопка
calcul_b.grid(row=1, column=0, columnspan=2, pady=10) # зан 2 колонки

text_l = tk.Label(root, text="Цифра сотен:")
text_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")

#  вывода рез
result_l = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="black")
result_l.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Запуск осн цикла
root.mainloop()