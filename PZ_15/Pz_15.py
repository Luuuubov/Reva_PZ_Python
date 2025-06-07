# Приложение УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторой
# организации. БД должна содержать таблицу Канцелярия со следующей структурой
# записи: ФИО работника, отдел, вид расхода, сумма.

# Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
# содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
# единицу измерения (штуки, килограммы, литры), количество, стоимость.


import sqlite3 as sq

with sq.connect('УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ.db') as accounting:
    cur = accounting.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS office 
                    (id_office INTEGER PRIMARY KEY AUTOINCREMENT, 
                    fio_customer TEXT NOT NULL, 
                    department TEXT NOT NULL, 
                    type_expenses TEXT NOT NULL, 
                    sum INTEGER NOT NULL); """)
    accounting.commit()

accounting_list = [
    (1, 'Задорожных Светлана Викторовна', 'Отдел продаж', 'Канцтовары', 15000),
    (2, 'Симонов Илья Андреевич',  'Отдел продаж', 'Печать и копирование', 10000),
    (3, 'Зубок Михаил Петрович', 'Отдел маркетинга', 'Обед и питание', 30000),
    (4, 'Зубок Вадим Валерьевич','Отдел транспортных расходов','Расходы на транспорт', 20000),
    (5, 'Степанникова Мария Викторовна', 'Отдел бухгалтерии', 'Обучение и развитие', 50000),
    (6, 'Зиновьева Карина Юрьевна', 'Технический отдел', 'Техническое обслуживание', 10000),
    (7, 'Федоров Михаил Григорьевич', 'Отдел коммунальных услуг', 'Коммунальные услуги', 6000),
    (8, 'Лютая Виктория Кириловна', 'Отдел ИТ', 'Интернет и связь', 4000),
    (9, 'Нестеренко Любовь Андреевна', ' Отдел бухгалтерии ','Прочие расходы', 60000)
]
cur.executemany("""INSERT INTO office VALUES (?, ?, ?, ?, ?) """, accounting_list)

print('\nОтдел продаж:')
cur.execute("select * from office where department =  'Отдел продаж' ")
for i in cur.fetchall():
    print(i)

print('\nСумма меньше 10000:')
cur.execute("select * from office where sum < 10000")
for i in cur.fetchall():
    print(i)

print('\nРаботники с одинаковой фамилией:')
cur.execute("select * from office where fio_customer LIKE 'Зубок%'")
for i in cur.fetchall():
    print(i)

print('\nИзменение вида расходов .')
cur.execute("update office set type_expenses = 'Интернет и мобильная связь' where department = 'Отдел ИТ'")

print('\nИзменение отдела бухгалтерии .')
cur.execute('update office set department = "Финансовый отдел" where type_expenses = "Прочие расходы"')

print('\nИзменение суммы расходов третьего отдела.')
cur.execute('update office set sum = "40000" where id_office = 3')


print('\nУдаление  с одним из видов расхода.')
cur.execute("delete from office where  type_expenses = 'Печать и копирование'")

print('\nУдаление с работником Лютая Виктория Кириловна .')
cur.execute("delete from office where fio_customer = 'Лютая Виктория Кириловна'")

print('\nУдаление с отделом транспортных расходов .')
cur.execute("delete from office where department = 'Отдел транспортных расходов'")



print('\nОбновленная таблица:')
for i in cur.execute('select * from office '):
    print(i)