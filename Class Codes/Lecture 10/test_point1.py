import Point1

def main():
    p1=Point1.Point(2,3)
    p1.show()
    p2=Point1.Point(3,1)
    p2.show()
    p1.set(2,3)
    p2.set(4,1)
    p1.show()
    p2.show()
    p1.x=-6 #data member is public by default and accessible outside the class
    p1.show()


main()
