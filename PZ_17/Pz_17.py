import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Форма регистрации пользователя") #окно
root.geometry("500x600")


title = tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 14, "bold"))
title.pack(pady=10)


form = tk.Frame(root) # Фрейм для формы
form.pack(pady=10, padx=20)


def create_row(label_text, row, entry_width=30, is_text=False): # Поля ввода
    label = tk.Label(form, text=label_text)
    label.grid(row=row, column=0, sticky="e", pady=5)
    if is_text:
        text = tk.Text(form, height=2, width=entry_width)
        text.grid(row=row, column=1, pady=5)
        return text
    else:
        entry = tk.Entry(form, width=entry_width)
        entry.grid(row=row, column=1, pady=5)
        return entry

name = create_row("Ваше имя:", 0)
password = create_row("Пароль:", 1)
age = create_row("Возраст:", 2)


gender_label = tk.Label(form, text="Пол:")
gender_label.grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
male_rb = tk.Radiobutton(form, text="Мужской", variable=gender_var, value="Мужской")
female_rb = tk.Radiobutton(form, text="Женский", variable=gender_var, value="Женский")
male_rb.grid(row=3, column=1, sticky="w")
female_rb.grid(row=3, column=1, sticky="e")


hobby_label = tk.Label(form, text="Ваши увлечения:")
hobby_label.grid(row=4, column=0, sticky="e", pady=5)
music_var = tk.IntVar()
video_var = tk.IntVar()
draw_var = tk.IntVar()
music_cb = tk.Checkbutton(form, text="Музыка", variable=music_var)
video_cb = tk.Checkbutton(form, text="Видео", variable=video_var)
draw_cb = tk.Checkbutton(form, text="Рисование", variable=draw_var)
music_cb.grid(row=4, column=1, sticky="w")
video_cb.grid(row=4, column=1)
draw_cb.grid(row=4, column=1, sticky="e")


country_label = tk.Label(form, text="Ваша страна:")
country_label.grid(row=5, column=0, sticky="e", pady=5)
country_cb = ttk.Combobox(form, values=["Россия", "США", "Казахстан", "Другое"])
country_cb.grid(row=5, column=1, pady=5)

city_label = tk.Label(form, text="Ваш город:")
city_label.grid(row=6, column=0, sticky="e", pady=5)
city_cb = ttk.Combobox(form, values=["Москва", "Нью-Йорк", "Алматы", "Другой"])
city_cb.grid(row=6, column=1, pady=5)


about_label = tk.Label(form, text="Кратко о себе:")
about_label.grid(row=7, column=0, sticky="ne", pady=5)
about_text = tk.Text(form, height=3, width=30)
about_text.grid(row=7, column=1, pady=5)


math_label = tk.Label(form, text="Решите пример, запишите результат в поле ниже:")
math_label.grid(row=8, column=0, columnspan=2, pady=10)
math_entry = tk.Entry(form, width=30)
math_entry.grid(row=9, column=0, columnspan=2)


btn_frame = tk.Frame(root) # Кнопки
btn_frame.pack(pady=15)

cancel_btn = tk.Button(btn_frame, text="Отменить ввод", width=20)
cancel_btn.pack(side="left", padx=10)

submit_btn = tk.Button(btn_frame, text="Данные подтверждаю", width=20)
submit_btn.pack(side="right", padx=10)


root.mainloop() # запуск
