class Rectangle:
    def __init__(self, side1, side2):
        self._name = "Прямоугольник"
        self._side1 = abs(side1)
        self._side2 = abs(side2)
    
    def area(self):
        return self._side1 * self._side2

    def perimeter(self):
        return (self._side1 + self._side2) * 2
    
    def __str__(self):
        return (f"{self._name}: ({self._side1}, {self._side2})")
    
    def __lt__(self, other):
        return self._side1 < other._side1 and self._side2 < other._side2
    
    def __le__(self, other):
        return self._side1 <= other._side1 and self._side2 <= other._side2

    def __eq__(self, other):
        return self._side1 == other._side1 and self._side2 == other._side2

    def __ne__(self, other):
        return self._side1 != other._side1 or self._side2 != other._side2

    def __gt__(self, other):
        return self._side1 > other._side1 and self._side2 > other._side2

    def __ge__(self, other):
        return self._side1 >= other._side1 and self._side2 >= other._side2

    def __add__(self, other):
        return Rectangle(self._side1 + other._side1, self._side2 + other._side2)

    def __sub__(self, other):
        return Rectangle(self._side1 - other._side1 if 
        self._side1 - other._side1 > 0 else 0, 
        self._side2 - other._side2 if 
        self._side2 - other._side2 > 0 else 0)

    def __iadd__(self, other):
        self._side1 += other._side1 
        self._side2 += other._side2
        return self

    def __isub__(self, other):
        self._side1 -= other._side1
        if self._side1 < 0: self._side1 = 0
        self._side2 -= other._side2
        if self._side2 < 0: self._side2 = 0
        return self


if __name__ == "__main__":
    r = Rectangle(2, 3)
    r2 = Rectangle(3, 4)
    r -= r2
    print(r)
    # r1 = Rectangle(1, 2)
    # print(f"r1: {r1}")
    # r2 = Rectangle(3, 3)
    # print(f"r2: {r2}")
    # r1 += r2
    # print(f"r1: {r1}")

    # print(f"r1 == r2 {r1 == r2}")
    # print(f"r1 < r2 {r1 < r2}")
    # print(f"r1 <= r2 {r1 <= r2}")
    # print(f"r1 > r2 {r1 > r2}")
    # print(f"r1 >= r2 {r1 >= r2}")
    # print(f"r1 != r2 {r1 != r2}")

    # r1 -= r2
    # print(f"r1: {r1}")

    # print(f"r1 == r2 {r1 == r2}")
    # print(f"r1 < r2 {r1 < r2}")
    # print(f"r1 <= r2 {r1 <= r2}")
    # print(f"r1 > r2 {r1 > r2}")
    # print(f"r1 >= r2 {r1 >= r2}")
    # print(f"r1 != r2 {r1 != r2}")

    # print(f"r1 + r2: {r1 + r2}")
    # print(f"r1 - r2: {r1 - r2}")