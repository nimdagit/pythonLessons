# ДЗ*:
# 1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры) 
# 2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта.
# 3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры)
# 4. Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)
# 5. Создать класс Circle (круг), наследовать его от класса Figure.
# 6. Добавить в класс Circle атрибут radius (радиус круга), атрибут должен быть приватным.
# 7. В классе Circle переопределить метод calculate_area, который бы считал и возвращал площадь круга.
# 8. В классе  Circle переопределить метод info, который бы распечатывал всю информацию о круге следующим образом: 
# Например -  Circle radius: 2cm, area: 12.57cm.
# 9. Создать класс RightTriangle (правильный треугольник - 90 градусов), наследовать его от класса Figure.
# 10. Добавить в класс RightTriangle атрибут side_a (сторона а) и side_b (сторона б), атрибуты должны быть приватными.
# 11. В классе RightTriangle переопределить метод calculate_area, который бы считал и возвращал площадь треугольника.
# 12. В классе RightTriangle переопределить метод info, который бы распечатывал всю информацию о треугольнике следующим образом: 
# Например - RightTriangle side a: 5cm, side b: 8cm, area: 20cm.
# 13. В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников
# 14. Затем через цикл вызвать у всех объектов списка метод info

class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area():
        pass
    def info():
        pass

class Circle(Figure):
    def __init__(self, radius):
        super().__init__() 
        self.__radius = radius

    def calculate_area(self):
        return 3.14*(self.__radius**2)

    def info(self):
        print(f'Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}^2')

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_a*self.__side_b/2

    def info(self):
        print(f'RightTriangle  sidea: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}^2')

figure_list = Circle(5), Circle(6), RightTriangle(4,6), RightTriangle(3,4), RightTriangle(7,9)

for i in figure_list:
    i.info()

# 13. В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников
# 14. Затем через цикл вызвать у всех объектов списка метод info