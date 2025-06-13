import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма регистрации пользователя") #окно
root.geometry("500x600")

title = tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 14, "bold"))
title.pack(pady=10)


form = tk.Frame(root) # для формы
form.pack(pady=10, padx=20)


def create_r(label_text, row, entry_width=30, is_text=False): #  ввод
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

name = create_r("Ваше имя:", 0)
password = create_r("Пароль:", 1)
age = create_r("Возраст:", 2)


gender_l = tk.Label(form, text="Пол:")
gender_l.grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
m_rb = tk.Radiobutton(form, text="Мужской", variable=gender_var, value="Мужской")
j_rb = tk.Radiobutton(form, text="Женский", variable=gender_var, value="Женский")
m_rb.grid(row=3, column=1, sticky="w")
j_rb.grid(row=3, column=1, sticky="e")


hobby_l = tk.Label(form, text="Ваши увлечения:")
hobby_l.grid(row=4, column=0, sticky="e", pady=5)
music = tk.IntVar()
video = tk.IntVar()
ris = tk.IntVar()
music_s = tk.Checkbutton(form, text="Музыка", variable=music)
video_s = tk.Checkbutton(form, text="Видео", variable=video)
ris_s = tk.Checkbutton(form, text="Рисование", variable=ris)
music_s.grid(row=4, column=1, sticky="w")
video_s.grid(row=4, column=1)
ris_s.grid(row=4, column=1, sticky="e")


country_l = tk.Label(form, text="Ваша страна:")
country_l.grid(row=5, column=0, sticky="e", pady=5)
country_s = ttk.Combobox(form, values=["Россия", "США", "Грузия", "Другое"])
country_s.grid(row=5, column=1, pady=5)

city_l = tk.Label(form, text="Ваш город:")
city_l.grid(row=6, column=0, sticky="e", pady=5)
city_s = ttk.Combobox(form, values=["Москва", "Нью-Йорк", "Ростов-на-Дону", "Другой"])
city_s.grid(row=6, column=1, pady=5)


you_l = tk.Label(form, text="Кратко о себе:")
you_l.grid(row=7, column=0, sticky="ne", pady=5)
text = tk.Text(form, height=3, width=30)
text.grid(row=7, column=1, pady=5)


matem_l = tk.Label(form, text="Решите пример, запишите результат в поле ниже:")
matem_l.grid(row=8, column=0, columnspan=2, pady=10)
math = tk.Entry(form, width=30)
math.grid(row=9, column=0, columnspan=2)


frame = tk.Frame(root) # Кнопки
frame.pack(pady=15)

galia_otmena = tk.Button(frame, text="Отменить ввод", width=20)
galia_otmena.pack(side="left", padx=10)

submit = tk.Button(frame, text="Данные подтверждаю", width=20)
submit.pack(side="right", padx=10)


root.mainloop() # запуск
