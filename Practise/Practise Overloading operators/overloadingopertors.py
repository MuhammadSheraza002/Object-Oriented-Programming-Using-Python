class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x, y)

    def __pow__(self, other):
        x = self.x ** other.x
        y = self.y ** other.y
        return Point(x, y)

    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return Point(x, y)

    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return Point(x, y)

    def __le__(self, other):
        self_mag = self.x**2 * self.y**2
        other_mag = other.x**2 * other.y**2
        return self_mag<=other_mag

def main():
    p1 = Point(3,4)
    p2 = Point(2,3)
    print(p1+p2)
    print(p1-p2)
    print(p1 * p2)
    print(p1 / p2)
    print(p1 ** p2)
    print(p1 // p2)
    print(p1 % p2)
    print(p1 <= p2)

main()