import sys

sys.path.append('../Lessons/lesson8')

import task2


class TestRectangle:
    def test_rectangle_area(self):
        r = task2.Rectangle(2, 3) 
        assert r.area() == 6

    def test_rectangle_print_with_negative_parameters(self):
        assert str(task2.Rectangle(-2, -3)) == 'Прямоугольник: (2, 3)'

    def test_rectangle_perimeter(self):
        r = task2.Rectangle(2, 3)
        assert r.perimeter() == 10

    r1 = task2.Rectangle(1, 2)
    r2 = task2.Rectangle(3, 3)

    def test_eq(self):
        assert (self.r1 == self.r2) == False

    def test_eq(self):
        assert (self.r1 == self.r2) == False

    def test_lt(self):
        assert (self.r1 < self.r2) == True

    def test_le(self):
        assert (self.r1 <= self.r2) == True

    def test_ne(self):
        assert (self.r1 != self.r2) == True

    def test_gt(self):
        assert (self.r1 > self.r2) == False

    def test_ge(self):
        assert (self.r1 >= self.r2) == False

    def test_add(self):
        assert str(self.r1 + self.r2) == 'Прямоугольник: (4, 5)'

    def test_sub(self):
        assert str(self.r1 - self.r2) == 'Прямоугольник: (0, 0)'

    def test_iadd(self):
        self.r1 += self.r2
        assert str(self.r1) == 'Прямоугольник: (4, 5)'

    def test_isub(self):
        self.r2 = task2.Rectangle(10, 10)
        self.r1 -= self.r2
        assert str(self.r1) == 'Прямоугольник: (0, 0)'
