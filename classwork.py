from abc import abstractmethod, ABC

import math


class Gem_figure(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def calculate_p(self):
        """
        Calculate perimeter of figure
        :return: float
        """
        pass

    def calculate_s(self):
        """
        Calculate square of figure
        :return: float
        """
        pass


class Circle(Gem_figure):

    def calculate_p(self):
        return 2 * math.pi * self.a

    def calculate_s(self):
        return math.pi * self.a ** 2


class Quadrilateral(Gem_figure, ABC):
    def __init__(self, a: float, b: float):
        super().__init__(a)
        self.b = b


class Rectangle(Quadrilateral):
    def calculate_p(self):
        return (self.a + self.b) * 2

    def calculate_s(self):
        return self.a * self.b

class Parallelogram(Quadrilateral):
    def __init__(self, a: float, b: float, h: float):
        super().__init__(a, b)
        self.h = h

    def calculate_p(self):
        return (self.a + self.b) * 2

    def calculate_s(self):
        return self.a * self.h


class Trapezoid(Parallelogram):
    def __init__(self, a: float, b: float, c: float, d: float, h: float):
        super().__init__(a, b, h)
        self.c = c
        self.d = d
        self.h = h

    def calculate_p(self):
        return self.a + self.b + self.c + self.d

    def calculate_s(self):
        return (self.a + self.b) * 0.5 * self.h

figure_list = []
x1 = Circle(23)
x2 = Rectangle(10, 15)
x3 = Parallelogram(10, 14, 7)
x4 = Trapezoid(2, 6, 4, 4, 5)
figure_list.append(x1)
figure_list.append(x2)
figure_list.append(x3)
figure_list.append(x4)
for f in figure_list:
    print(f.calculate_p())
    print(f.calculate_s())