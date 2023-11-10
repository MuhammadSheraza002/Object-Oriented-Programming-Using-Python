class P:
    def __init__(self):
        print('Init function from parent is called')
        self.__x = 0
        self.y = 1

    def get_x(self):
        return self.__x

class C(P):
    def __init__(self):
        P.__init__(self)
        print('Init function from child is called')
        print(self.y) #it will work also
def main():
    object = C()
    print (object.get_x())

main()

