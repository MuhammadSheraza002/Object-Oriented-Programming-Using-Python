class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print (f'X: {self.x}, Y: {self.y}')
