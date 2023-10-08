import sys
from pathlib import Path

# Добавим package figarea в sys.path
# чтобы использовать абсолютный импорт
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import unittest
from math import pi, sqrt

from figarea.figures import Circle, Triangle, Square
from figarea.figinterface import compute_area
from figarea.utils import check_value


class TestFigures(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(2)
        self.triangle = Triangle(3, 4, 5)
        self.square = Square(3)

    def test_circle_area(self):
        self.assertEqual(self.circle.area, round(pi * 4, 5))

    def test_square_area(self):
        self.assertEqual(self.square.area, 9)

    def test_triangle_area(self):
        a = 3; b = 4; c = 5; prec = 5
        p = (a + b + c) / 2
        s = round(sqrt(p * (p - a) * (p - b) * (p - c)), prec)
        self.assertEqual(self.triangle.area, s)

    def test_triangle_axiom(self):
        data = [[3, 4, 8], [7, 3, 3], [6, 9, 3]]
        for item in data:
            with self.assertRaises(ValueError):
                Triangle(item[0], item[1], item[2])

    def test_triangle_is_right(self):
        data = {
            (3, 4, 5): True,
            (sqrt(3), sqrt(2), sqrt(5)): True,
            (11, 12, 13): False,
        }
        for key, res in data.items():
            self.assertEqual(Triangle(*key).is_right_triangle(), res)


class TrashFigure():
            pass


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4, 5)
        self.trashfig = TrashFigure()

    def test_compute_area_with_trashfig(self):
        with self.assertRaises(AttributeError):
            compute_area(self.trashfig)

    def test_compute_area_with_truefig(self):
        self.assertIsInstance(compute_area(self.triangle), float)


class TestUtils(unittest.TestCase):
    def test_check_value_type(self):
        value = 'test_string'
        with self.assertRaises(ValueError):
            check_value(value)

    def test_check_value_not_zero(self):
        value = 0
        with self.assertRaises(ValueError):
            check_value(value)


if __name__ == "__main__":
    unittest.main()