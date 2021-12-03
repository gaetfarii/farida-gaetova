import math

class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self, new):
        new_a = self.a + new.a
        new_b = self.b + new.b
        return ComplexNumber(new_a, new_b)

    def add2(self, new):
        self.a += new.a
        self.b += new.b

    def sub(self, new):
        new_a = self.a - new.a
        new_b = self.b - new.b
        return ComplexNumber(new_a, new_b)

    def sub2(self, new):
        self.a -= new.a
        self.b -= new.b

    def multNumber(self, num):
        new_a = self.a * num
        new_b = self.b * num
        return ComplexNumber(new_a, new_b)

    def multNumber2(self, num):
        self.a *= num
        self.a *= num

    def mult(self, new):
        new_a = self.a * new.a - self.b * new.b
        new_b = self.a * new.b + self.b * new.a
        return ComplexNumber(new_a, new_b)

    def mult2(self, new):
        self.a = self.a * new.a - self.b * new.b
        self.b = self.a * new.b + self.b * new.a

    def div(self, new):
        new_a = (self.a * new.a + self.b * new.b) / ((new.a) ** 2 - (new.b) ** 2)
        new_b = (self.b * new.a - self.a + new.b) / ((new.a) ** 2 - (new.b) ** 2)
        return ComplexNumber(new_a, new_b)

    def div2(self, new):
        self.a = (self.a * new.a + self.b * new.b) / (new.a ** 2 - new.b ** 2)
        self.b = (self.b * new.a - self.a + new.b) / (new.a ** 2 - new.b ** 2)

    def len(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def str(self):
        if self.b > 0:
            return str(self.a) + ' + ' + str(self.b) + ' * i'
        else:
            return str(self.a) + ' - ' + str(abs(self.b)) + ' * i'

    def arg(self):
        return math.degrees(math.atan(self.a / self.b))

    def pow(self, num):
        f = self.arg()
        c = self.len() ** num
        self.a = c * math.cos(f * num)
        self.b = c * math.sin(f * num)

    def equals(self, new):
        if (self.a ** 2 + self.b ** 2) ** 0.5 > (new.a ** 2 + new.b ** 2) ** 0.5:
            return 'Первая число ' + str(self.a) + ' + ' + str(self.b) + ' * i' + ' больше'
        elif (self.a ** 2 + self.b ** 2) ** 0.5 < (new.a ** 2 + new.b ** 2) ** 0.5:
            return 'Второе число ' + str(new.a) + ' + ' + str(new.b) + ' * i' + ' больше'
        else:
            return 'Числа равны'
