# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figure:
    def __init__(self, width, height): #в конструк зад свойства
        self.width = width # сохр как атрибут
        self.height = height

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)

class Square(Figure):
    def __init__(self, side):
        super().__init__(side, side) # Конст ожидает два аргумента
        self.side = side

    def area(self):
        return self.side * 2

    def perimeter(self):
        return 4 * self.side
