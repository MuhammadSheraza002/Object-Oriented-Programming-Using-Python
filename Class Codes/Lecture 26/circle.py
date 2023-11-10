class Circle:
    def __init__(self, **kwargs):
        self.x, self.y, self.r = 0, 0, 10
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
        if 'r' in kwargs:
            self.r = kwargs['r']
    def __str__(self):
        return f'Center: ({self.x}, {self.y})\t Radius: {self.r}'

c1 = Circle()
print (c1)
c2 = Circle(x=3)
print (c2)
c3 = Circle(x=4, y=6)
print (c3)
c4 = Circle(r=20, y=10, x=30)
print (c4)