import math


class RationalFraction:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def reduce(self):
        nod = math.gcd(self.x, self.y)
        self.x //= nod
        self.y //= nod

    def add(self, new):
        new_y = (self.y * new.y) // math.gcd(self.y * new.y)
        new_x = self.x * (new_y // self.y) + new.x * (new_y // new.y)
        n = RationalFraction(new_x, new_y)
        n.reduce()
        return n

    def add2(self, new):
        nok = (self.y * new.y) // math.gcd(self.y * new.y)
        self.x = self.x * (nok // self.y) + new.x * (nok // new.y)
        self.y = nok
        self.reduce()

    def sub(self, new):
        new_y = (self.y * new.y) // math.gcd(self.y * new.y)
        new_x = self.x * (new_y // self.y) - new.x * (new_y // new.y)
        n = RationalFraction(new_x, new_y)
        n.reduce()
        return n

    def sub2(self, new):
        nok = (self.y * new.y) // math.gcd(self.y * new.y)
        self.x = self.x * (nok // self.y) - new.x * (nok // new.y)
        self.y = nok
        self.reduce()

    def mult(self, new):
        new_x = self.x * new.x
        new_y = self.y * new.y
        n = RationalFraction(new_x, new_y)
        n.reduce()
        return n

    def mult2(self, new):
        self.x *= new.x
        self.y *= new.y
        self.reduce()

    def div(self, new):
        new_x = self.x * new.y
        new_y = self.y * new.x
        n = RationalFraction(new_x, new_y)
        n.reduce()
        return n

    def div2(self, new):
        self.x *= new.y
        self.y *= new.x
        self.reduce()

    def __str__(self):
        return str(self.x) + '/' + str(self.y)

    def value(self):
        return self.x / self.y

    def equals(self, new):
        print(self.__str__(), '?', new.__str__())
        self.reduce()
        new.reduce()
        nok = (self.y * new.y) // math.gcd(self.y * new.y)
        new_x1 = self.x * (nok // self.y)
        new_x2 = new.x * (nok // new.y)
        if new_x1 > new_x2:
            print('    >    ')
        elif new_x2 > new_x1:
            print('    <    ')
        else:
            print('    =    ')

    def numberPart(self):
        print(self.x//self.y)

