import math


class Shape:
    _type = "плоская"
    
    def __init__(self, name):
        self._name = name
    
    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

    def __str__(self):
        return self._name

    def get_type(self):
        return self._type


class Parallelogram(Shape):
    def __init__(self, side1, side2, angle):
        super().__init__("Параллелограмм")
        self._side1 = side1
        self._side2 = side2
        self._angle = angle

    def area(self):
        return self._side1 * self._side2 * math.sin(math.radians(self._angle))

    def perimeter(self):
        return (self._side1 + self._side2) * 2

    def __str__(self):
        return (f"Название: {super().__str__()}\n" 
        f"Первая сторона: {self._side1}\n"
        f"Вторая сторона: {self._side2}\n" 
        f"Угол между сторонами: {self._angle}")


class Rectangle(Parallelogram):
    def __init__(self, side1, side2):
        super(Parallelogram, self).__init__("Прямоугольник")
        self._side1 = side1
        self._side2 = side2
        self._angle = 90
    
    def __str__(self):
        return (f"Название: {super(Parallelogram, self).__str__()}\n" 
        f"Первая сторона: {self._side1}\n"
        f"Вторая сторона: {self._side2}")


class Square(Rectangle):
    def __init__(self, side1):
        super(Parallelogram, self).__init__("Квадрат")
        self._side1 = side1
        self._side2 = side1
        self._angle = 90

    def __str__(self):
        return (f"Название: {super(Parallelogram, self).__str__()}\n" 
        f"Cторона: {self._side1}")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Круг")
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return math.pi * self._radius * 2

    def __str__(self):
        return (f"Название: {super().__str__()}\n" 
        f"Радиус: {self._radius}")


class Triangle(Shape):
    def __init__(self, side1, side2, angle):
        super().__init__("Треугольник")
        self._side1 = side1
        self._side2 = side2
        self._angle = angle 
        self._side3 = math.sqrt(self._side1**2 + self._side2**2 - 
        2*self._side1*self._side1*math.cos(math.radians(self._angle))) 
    
    def area(self):
        return (self._side1 * self._side2 * 
        math.sin(math.radians(self._angle)) / 2)

    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    def __str__(self):
        return (f"Название: {super().__str__()}\n" 
        f"Первая сторона: {self._side1}\n"
        f"Вторая сторона: {self._side2}\n"
        f"Третья сторона: {self._side3:.2f}\n"  
        f"Угол между сторонами: {self._angle}")


class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Шар")
        self._radius = radius
        self._type = "объёмная"

    def area(self):
        return 4 * math.pi * self._radius ** 2

    def volume(self):
        return 4/3 * math.pi * self._radius ** 3

    def __str__(self):
        return (f"Название: {super().__str__()}\n" 
        f"Радиус: {self._radius}")


class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__("Цилиндр")
        self._radius = radius
        self._height = height
        self._type = "объёмная"

    def area(self):
        return 2 * math.pi * self._radius * (self._height + self._radius)

    def volume(self):
        return math.pi * self._height * self._radius ** 2

    def __str__(self):
        return (f"Название: {super().__str__()}\n" 
        f"Радиус: {self._radius}\n"
        f"Высота: {self._height}")


if __name__ == "__main__":
    SHAPE_SELECTOR = {
        1: Parallelogram,
        2: Rectangle,
        3: Square,
        4: Circle,
        5: Triangle,
        6: Sphere,
        7: Cylinder
    }


    def get_operation_codes(shape_type):
        if shape_type >= 1 and shape_type <= 5:
            return ("Введите код операции:\n"
            "1 - найти периметр\n"
            "2 - найти площадь\n")
        else:
            return ("Введите код операции:\n"
            "1 - найти площадь\n"
            "2 - найти объём\n")
            

    def print_res(shape, shape_num):
        print(shape)
        op = input(get_operation_codes(shape_num))
        if shape.get_type() == 'плоская':
            if op == '1':
                print(f"{shape.perimeter():.2f}")
            elif op == '2':
                print(f"{shape.area():.2f}")
            else:
                print("Введите корректные данные")
        else:
            if op == '1':
                print(f"{shape.area():.2f}")
            elif op == '2':
                print(f"{shape.volume():.2f}")
            else:
                print("Введите корректные данные")


    def is_int(string_number):
        try:
            int(string_number)
            return True
        except ValueError:
            return False 


    def is_float(string_number):
        try:
            float(string_number)
            return True
        except ValueError:
            return False 


    while True:
        string = input("Пожалуйста, введите номер фигуры "
        "(Enter - чтобы выйти):\n"
        "1 - Параллелограмм\n"
        "2 - Прямоугольник\n"
        "3 - Квадрат\n"
        "4 - Круг\n"
        "5 - Треугольник\n"
        "6 - Шар\n"
        "7 - Цилиндр\n")
        if is_int(string):
            shape_num = int(string)
            flag = True
            if shape_num in {1, 5}:
                try:
                    a, b, ang = input("Введите параметры фигуры через пробел "
                    "(1 сторона, 2 сторона, угол между ними)\n").split()
                except ValueError:
                    print("Введите корректные данные")
                    flag = False
                if flag:
                    if is_float(a) and is_float(b) and is_int(ang):
                        a = float(a)
                        b = float(b)
                        ang = int(ang)
                        if a > 0 and b > 0 and ang > 0:
                            shape = SHAPE_SELECTOR[shape_num](a, b, ang)
                            print_res(shape, shape_num)
                        else:
                            print("Введите корректные данные")        
                    else:
                        print("Введите корректные данные")    
            elif shape_num in {4, 6}:
                try:
                    r = input("Введите радиус фигуры\n")
                except ValueError:
                    print("Введите корректные данные")
                    flag = False
                if flag: 
                    if is_float(r):
                        r = float(r)
                        if r > 0:
                            shape = SHAPE_SELECTOR[shape_num](r)
                            print_res(shape, shape_num)
                        else:
                            print("Введите корректные данные")        
                    else:
                        print("Введите корректные данные")         
            elif shape_num == 2:
                try:
                    a, b = input("Введите параметры фигуры через пробел "
                "(1 сторона, 2 сторона)\n").split()
                except ValueError:
                    print("Введите корректные данные")
                    flag = False
                if flag:    
                    if is_float(a) and is_float(b):
                        a = float(a)
                        b = float(b)
                        if a > 0 and b > 0:
                            shape = SHAPE_SELECTOR[shape_num](a, b)
                            print_res(shape, shape_num)
                        else:
                            print("Введите корректные данные")        
                    else:
                        print("Введите корректные данные")
            elif shape_num == 3:
                try:
                    a = input("Введите параметры фигуры через пробел "
                "(сторона)\n")
                except ValueError:
                    print("Введите корректные данные")
                    flag = False
                if flag:
                    if is_float(a):
                        a = float(a)
                        if a > 0:
                            shape = SHAPE_SELECTOR[shape_num](a)
                            print_res(shape, shape_num)
                        else:
                            print("Введите корректные данные")        
                    else:
                        print("Введите корректные данные")
            elif shape_num == 7:
                try:
                    r, h = input("Введите радиус и высоту фигуры " 
                    "(через пробел)\n").split()
                except ValueError:
                    print("Введите корректные данные")
                    flag = False
                if flag:
                    if is_float(r) and is_float(h):
                        r = float(r)
                        h = float(h)
                        if r > 0 and h > 0:
                            shape = SHAPE_SELECTOR[shape_num](r, h)
                            print_res(shape, shape_num)
                        else:
                            print("Введите корректные данные")        
                    else:
                        print("Введите корректные данные")
        elif string == '':
            break
        else:
            print("Введите корректные данные")