class Point:
    def __init__(self, x, y):
        '''self.x = x
        self.y = y'''
        self.set(x,y)
    def set(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print (f'X: {self.x}, Y: {self.y}')
