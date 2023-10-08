from math import pi, sqrt

from figarea.figabstract import BaseABCFigure
from figarea.utils import check_value


class Circle(BaseABCFigure):
    """
    Класс круга
    """
    def __init__(self, radius: float, prec: int = 5) -> None:
        """
        Так как по условию непонятно с какой точностью необходим результат,
        то добавим возможность настройки точности вывода с помощью параметра prec
        """
        if check_value(radius, prec):
            self.radius = radius
            self.prec = prec

    @property
    def area(self) -> float:
        return round(pi * self.radius ** 2, self.prec)


class Triangle(BaseABCFigure):
    """
    Класс треугольника
    """
    def __init__(self, side1: float, side2: float, side3: float, prec: int = 5) -> None:
       
        if check_value(side1, side2, side3, prec):
            self.a = side1
            self.b = side2
            self.c = side3
            self.prec = prec

        if not (side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2): 
            raise ValueError("Triangle axiom is not true!")

    def is_right_triangle(self) -> bool:
        """
        Функция проверки прямоугольности треугольника
        Так как точность float до 15 знаков, то для иррациональных 
        чисел (например sqrt(2) sqrt(3) sqrt(5)) равенство 
        a^2 + b^2 = c^2 не будет выпольняться, воспользуемся 
        round, чтобы ограничить числа сторон до 10 знаков после ,
        """
        _prec = 10
        sides = sorted([self.a, self.b, self.c])
        if round(sides[0] ** 2, _prec) + round(sides[1] ** 2, _prec) == round(sides[2] ** 2, _prec):
            return True
        return False


    @property
    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), self.prec)


class Square(BaseABCFigure):
    """
    Класс квадрата, для демонстрации добавления фигур
    """
    def __init__(self, side: float, prec: int = 5) -> None:
        if check_value(side, prec):
            self.a = side
            self.prec = prec

    @property
    def area(self) -> float:
        return round(self.a ** 2, self.prec)
