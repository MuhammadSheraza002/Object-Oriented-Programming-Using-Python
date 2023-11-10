import Point2


def main():
    p1=Point2.Point(2,3)
    p1.show()
    p2=Point2.Point(1,4)
    p2.show()
    p1.set(2,3)
    p2.set(4,1)
    p1.show()
    p2.show()
    #print(p1.__x)  #Here we have error object has no attribute __x, because it is hidden from outside
    p1.__x=-5
    p1.show()       #No effect of previous statement.

main()
