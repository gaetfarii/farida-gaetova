class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, new):
        new_x = self.x + new.x
        new_y = self.y + new.y
        return Vector2D(new_x, new_y)

    def add2(self, new):
        self.x += new.x
        self.y += new.y

    def sub(self, new):
        new_x = self.x - new.x
        new_y = self.y - new.y
        return Vector2D(new_x, new_y)

    def sub2(self, new):
        self.x -= new.x
        self.y -= new.y

    def mult(self, a):
        new_x = self.x * a
        new_y = self.y * a
        return Vector2D(new_x, new_y)

    def mult2(self, a):
        self.x *= a
        self.y *= a

    def __str__(self):
        return 'Vector2D(x = ' + str(self.x) + ', y = ' + str(self.y) + ')'

    def len_(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def scalarProduct(self, new):
        return self.x * new.x + self.y * new.y

    def cos(self, new):
        return (self.x * new.x + self.y * new.y) / ((self.x ** 2 + self.y ** 2) * (new.x ** 2 + new.y ** 2))

    def equals(self, new):
        len1 = (self.x ** 2 + self.y ** 2) ** 0.5
        len2 = (new.x ** 2 + new.y ** 2) ** 0.5
        if len1 > len2:
            return print('Первый вектор длиннее второго')
        elif len2 > len1:
            return print('Второй вектор длиннее первого')
        else:
            return print('Векторы равны')





s = Vector2D(1, 4)

w = Vector2D(3, 7)
print(s.mult(2))

