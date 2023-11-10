import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print (f'X: {self.x}, Y: {self.y}')

    def reverse_point(self):
        self.x=-self.x
        self.y = -self.y

    def check_quadrant(self):
        if self.x > 0:
            if self.y > 0:
                print(f'point lies in 1st Quadrant')
            else:
                print(f'point lies in 3rd Quadrant')

        elif self.x < 0:
            if self.y > 0:
                print(f'point lies in 2nd Quadrant')
            else:
                print(f'point lies in 3rd Quadrant')
        else:
            print(f'point lies on origin')

    def rotate_point(self,theta):
        x = 2
        y = 3
        X = x * math.cos(theta*math.pi/180) + y * math.sin(theta*math.pi/180)
        Y = -x * math.sin(theta*math.pi/180) + y * math.cos(theta*math.pi/180)
        return Point(int(X),int(Y))

    def compare_rotation(self,p):
        return (((p.x - p.x)**2) + ((self.y - self.y)**2))**(1/2)

    def __str__(self):
        return f'({self.x},{self.y})'

