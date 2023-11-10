import Point3


def main():
    p1=Point3.Point(2,3)
    #p1.show()          #There is no show method in class Point
    #p1.__show()       #Again, there is no __show method in class Point;
    # actually it is there but private
    p1.display()        #calling __show function through diaplay function

main()
