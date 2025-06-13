# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}"

# product = Product("Молоко", 59, 10)
# print(product.display())