class Point:
    def __init__(self,x , y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __del__(self):
        print (f'del function called for ({self.x}, {self.y})')
